import argparse
import os
from typing import Dict, Any


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
        "FIELDS_PATH": "resources/fields.json",
        "ATTEMPTS": 1,
        "OUTPUT_DIR": "problems",
        "OUTPUT_BASE_NAME": "new_problems",
        "IMPROVE_AFTER_FIRST_TRY": False,
        "CHECK_GPT_FEEDBACK": False,
        "ADD_TIMESTAMP": False,
        "USE_COVER_STORY": True,
        "USE_TOPICS": True,
        "USE_FIELD": True,
        "REQUIRE_30_LINES": True,
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
    parser.add_argument(
        "--use-cover-story",
        action="store_true",
        help="Flag to use a cover story in the problem generation.",
    )
    parser.add_argument(
        "--use-topics",
        action="store_true",
        help="Flag to use topics in the problem generation.",
    )
    parser.add_argument(
        "--use-field",
        action="store_true",
        help="Flag to use field from specific computer science field in the problem generation.",
    )
    parser.add_argument(
        "--require-30-lines",
        action="store_true",
        help="Flag to require 30 lines in the solution for the problem generation.",
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
    if args.use_cover_story is not None:
        config["USE_COVER_STORY"] = args.use_cover_story
    if args.use_topics is not None:
        config["USE_TOPICS"] = args.use_topics
    if args.use_field is not None:
        config["USE_FIELD"] = args.use_field
    if args.require_30_lines is not None:
        config["REQUIRE_30_LINES"] = args.require_30_lines
