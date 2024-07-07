import logging
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Any, List

from tqdm import tqdm

from novel_problem_generator.problem_generator import ProblemGenerator
from novel_problem_generator.config import (
    load_config,
    parse_args,
    update_config_with_args,
)


def generate_and_validate(
    problem_generator: ProblemGenerator,
    task_id: str,
    config: Dict[str, Any],
) -> Dict[str, Any]:
    try:
        new_problem = problem_generator.generate_problem(task_id)
    except Exception as error:
        logging.error(f"Error generating problem for task_id {task_id}: {error}")
        return {"task_id": task_id, "valid": False, "reason": str(error)}

    validation_result = problem_generator.validator.validate_problem(
        new_problem, config["CHECK_GPT_FEEDBACK"]
    )
    if validation_result["valid"]:
        warnings = validation_result.get("warnings", [])
        if warnings and config["IMPROVE_AFTER_FIRST_TRY"]:
            improved_problem = try_improving_problem(
                problem_generator,
                new_problem,
                "Problem is valid but has warnings.",
                warnings,
            )
            return validate_final_problem(
                problem_generator, improved_problem, config, task_id
            )
        else:
            new_problem["valid"] = True
            new_problem["extra_info"]["warnings"] = warnings
            return new_problem
    else:
        reason = validation_result["reason"]
        warnings = validation_result.get("warnings", [])
        if config["IMPROVE_AFTER_FIRST_TRY"]:
            improved_problem = try_improving_problem(
                problem_generator, new_problem, reason, warnings
            )
            return validate_final_problem(
                problem_generator, improved_problem, config, task_id
            )
        else:
            new_problem["valid"] = False
            new_problem["reason"] = reason
            new_problem["extra_info"]["warnings"] = warnings
            return new_problem


def try_improving_problem(
    problem_generator: ProblemGenerator,
    problem: Dict[str, Any],
    followup_reason: str,
    warnings: List[str],
) -> Dict[str, Any]:
    try:
        extra_info = problem.pop("extra_info", {})
        problem["extra_info"] = extra_info
        problem["extra_info"]["warnings"] = warnings
        return problem_generator.follow_up_prompt(problem, followup_reason, warnings)
    except Exception as error:
        logging.error(f"Error improving problem: {error}")
        problem["valid"] = False
        problem["reason"] = f"{followup_reason}; Warnings: {warnings}"
        return problem


def validate_final_problem(
    problem_generator: ProblemGenerator,
    problem: Dict[str, Any],
    config: Dict[str, Any],
    task_id: str,
) -> Dict[str, Any]:
    validation_result = problem_generator.validator.validate_problem(
        problem, config["CHECK_GPT_FEEDBACK"]
    )
    warnings = validation_result.get("warnings", [])
    if validation_result["valid"]:
        if warnings:
            logging.info(
                f"Improved problem for task_id {task_id} valid with warnings: {warnings}"
            )
            problem["extra_info"]["warnings"] = warnings
        problem["valid"] = True
    else:
        problem["valid"] = False
        problem["reason"] = validation_result["reason"]
        problem["extra_info"]["warnings"] = warnings
    return problem


class TaskHandler:
    def __init__(
        self,
        problem_generator: ProblemGenerator,
        config: Dict[str, Any],
    ):
        self.problem_generator = problem_generator
        self.config = config

    def handle_task(self, attempt: int) -> Dict[str, Any]:
        task_id = f"{self.problem_generator.task_id_class}/{attempt + 1}"
        return generate_and_validate(
            self.problem_generator,
            task_id,
            self.config,
        )


def main() -> None:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    args = parse_args()
    config = load_config()
    update_config_with_args(config, args)

    problem_generator = ProblemGenerator(config)

    valid_problems = []
    invalid_problems_counter = defaultdict(int)
    task_handler = TaskHandler(problem_generator, config)

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(task_handler.handle_task, attempt)
            for attempt in range(config["ATTEMPTS"])
        ]
        for future in tqdm(
            as_completed(futures), total=config["ATTEMPTS"], desc="Generating problems"
        ):
            try:
                problem = future.result()
                if problem.pop("valid"):

                    problem_generator.save_problem(problem, is_valid=True)
                    valid_problems.append(problem)
                else:
                    problem_generator.save_problem(
                        problem,
                        is_valid=False,
                        reason=problem.get("reason", "Unknown reason"),
                    )
                    invalid_problems_counter[
                        problem.get("reason", "Unknown reason")
                    ] += 1
            except Exception as error:
                logging.error(f"Unhandled exception: {error}")

    logging.info(
        f"Problem generation completed. Created {len(valid_problems)} valid problems from {config['ATTEMPTS']} attempts"
    )
    if invalid_problems_counter:
        logging.info(f"Validation failures: {dict(invalid_problems_counter)}")


if __name__ == "__main__":
    main()
