import logging
import os
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Any, Tuple, List

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
        "ATTEMPTS": 5,
        "EXAMPLE_PROBLEM_PATH": "resources/example_hard_problem.json",
        "COVER_STORY_PATH": "resources/cover_story_words.json",
        "TOPICS_PATH": "resources/topics.json",
        "OUTPUT_DIR": "data",
    }


def generate_and_validate(
    problem_generator: ProblemGenerator, task_id: str
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    try:
        new_problem = problem_generator.generate_problem(task_id)
    except Exception as error:
        logging.error(f"Error generating problem for task_id {task_id}: {error}")
        return None, None

    validation_result = problem_generator.validator.validate_problem(new_problem)
    if validation_result["valid"]:
        warnings = validation_result.get("warnings", [])
        if warnings:
            improved_problem = try_improving_problem(
                problem_generator,
                new_problem,
                "Problem is valid but has warnings.",
                warnings,
            )
            return validate_final_problem(problem_generator, improved_problem, task_id)
        else:
            return new_problem, None
    else:
        reason = validation_result["reason"]
        warnings = validation_result.get("warnings", [])
        improved_problem = try_improving_problem(
            problem_generator, new_problem, reason, warnings
        )
        return validate_final_problem(problem_generator, improved_problem, task_id)


def try_improving_problem(
    problem_generator: ProblemGenerator,
    problem: Dict[str, Any],
    followup_reason: str,
    warnings: List[str],
) -> Dict[str, Any]:
    try:
        extra_info = problem.pop("extra_info")
        problem["extra_info"] = extra_info
        problem["extra_info"]["warnings"] = warnings
        return problem_generator.validator.follow_up_prompt(
            problem, followup_reason, warnings
        )
    except Exception as error:
        logging.error(f"Error improving problem: {error}")
        problem["invalid_reason"] = f"{followup_reason}; Warnings: {warnings}"
        return problem


def validate_final_problem(
    problem_generator: ProblemGenerator, problem: Dict[str, Any], task_id: str
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    validation_result = problem_generator.validator.validate_problem(problem)
    if validation_result["valid"]:
        warnings = validation_result.get("warnings", [])
        if warnings:
            logging.info(
                f"Improved problem for task_id {task_id} valid with warnings: {warnings}"
            )
            problem["extra_info"]["warnings"] = warnings
        return problem, None
    else:
        problem["invalid_reason"] = validation_result["reason"]
        return None, problem


def handle_task(
    problem_generator: ProblemGenerator, attempt: int
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    task_id = f"{problem_generator.task_id_class}/{attempt + 1}"
    return generate_and_validate(problem_generator, task_id)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    config = load_config()
    problem_generator = ProblemGenerator(config)

    valid_problems = []
    invalid_problems_counter = defaultdict(int)

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(handle_task, problem_generator, attempt)
            for attempt in range(config["ATTEMPTS"])
        ]
        for future in tqdm(
            as_completed(futures), total=config["ATTEMPTS"], desc="Generating problems"
        ):
            try:
                new_problem, invalid_problem = future.result()
                if new_problem:
                    problem_generator.save_problem(new_problem, is_valid=True)
                    valid_problems.append(new_problem)
                elif invalid_problem:
                    problem_generator.save_problem(
                        invalid_problem,
                        is_valid=False,
                        reason=invalid_problem["invalid_reason"],
                    )
                    invalid_problems_counter[invalid_problem["invalid_reason"]] += 1
            except Exception as error:
                logging.error(f"Unhandled exception: {error}")

    logging.info(
        f"Problem generation completed. Created {len(valid_problems)} valid problems from {config['ATTEMPTS']} attempts"
    )
    if invalid_problems_counter:
        logging.info(f"Validation failures: {dict(invalid_problems_counter)}")


if __name__ == "__main__":
    main()
