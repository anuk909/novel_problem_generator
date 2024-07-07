import argparse
import logging
import os
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Any, List

from tqdm import tqdm

from novel_problem_generator.problem_generator import ProblemGenerator


def load_config() -> Dict[str, Any]:
    azure_openai_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    azure_openai_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    if not azure_openai_api_key or not azure_openai_endpoint:
        raise ValueError("AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT must be set.")
    return {
        "AZURE_OPENAI_API_KEY": azure_openai_api_key,
        "AZURE_OPENAI_ENDPOINT": azure_openai_endpoint,
        "AZURE_OPENAI_API_VERSION": "2024-04-01-preview",
        "OPENAI_MODEL": "gpt-4-turbo-2024-04-09",
        "EXAMPLE_PROBLEM_PATH": "resources/example_hard_problem.json",
        "COVER_STORY_PATH": "resources/cover_story_words.json",
        "TOPICS_PATH": "resources/topics.json",
        "ATTEMPTS": 1,
        "OUTPUT_DIR": "problems",
        "OUTPUT_BASE_NAME": "new_problems",
        "IMPROVE_AFTER_FIRST_TRY": False,
        "CHECK_GPT_FEEDBACK": False,
        "ADD_TIMESTAMP": False,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate and validate problems.")
    parser.add_argument(
        "--attempts",
        type=int,
        help="Number of attempts to generate problems.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        help="Directory to save the generated problems.",
    )
    parser.add_argument(
        "--output-base-name",
        type=str,
        help="Name of the output file for the generated problems.",
    )
    parser.add_argument(
        "--check-gpt-feedback",
        action="store_true",
        help="Flag to check the GPT feedback for the generated problems.",
    )
    parser.add_argument(
        "--improve-after-first-try",
        action="store_true",
        help="Flag to improve problem after the first try if the validation fails.",
    )
    parser.add_argument(
        "--add-timestamp",
        action="store_true",
        help="Flag to add a timestamp to the output file names.",
    )
    return parser.parse_args()


def update_config_with_args(config: Dict[str, Any], args: argparse.Namespace) -> None:
    if args.attempts is not None:
        config["ATTEMPTS"] = args.attempts
    if args.output_dir is not None:
        config["OUTPUT_DIR"] = args.output_dir
    if args.output_base_name is not None:
        config["OUTPUT_BASE_NAME"] = args.output_base_name
    if args.improve_after_first_try is not None:
        config["IMPROVE_AFTER_FIRST_TRY"] = args.improve_after_first_try
    if args.check_gpt_feedback is not None:
        config["CHECK_GPT_FEEDBACK"] = args.check_gpt_feedback
    if args.add_timestamp is not None:
        config["ADD_TIMESTAMP"] = args.add_timestamp


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
