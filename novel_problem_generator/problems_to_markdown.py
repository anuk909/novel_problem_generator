import json
import os
import argparse
import textwrap
import logging
import re
from typing import Dict, Any


def setup_logging():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def get_extra_info_str(extra_info: Dict[str, Any]):
    extra_info_str = "## Extra Info\n\n"
    if topics := extra_info.get("topics", None):
        extra_info_str += "## Topics\n\n"
        extra_info_str += f"{topics}\n\n"

    if field := extra_info.get("field", None):
        extra_info_str += "## Field\n\n"
        extra_info_str += f"{field}\n\n"

    if cover_story_words := extra_info.get("cover_story_words", None):
        extra_info_str += "## Cover Story\n\n"
        extra_info_str += f"{cover_story_words}\n\n"

    if cleaned_prompt := extra_info.get("cleaned_prompt", None):
        extra_info_str += (
            "## Cleaned Prompt\n\n" f"```python\n{cleaned_prompt}\n```\n\n"
        )

    if warnings := extra_info.get("warnings", None):
        extra_info_str += "## Warnings\n\n"
        extra_info_str += "\n".join(["- " + warning for warning in warnings])
    return extra_info_str


def json_to_markdown(json_data: Dict[str, Any]) -> str:
    task_id = json_data["task_id"]
    prompt = json_data["prompt"]
    canonical_solution = json_data["canonical_solution"]
    test_cases = json_data["test"]
    entry_point = json_data["entry_point"]
    extra_info = json_data.get("extra_info", {})

    markdown = f"# Task ID: {task_id}\n\n"
    markdown += "## Prompt\n\n" f"```python\n{prompt}\n```\n\n"

    markdown += (
        "## Canonical Solution\n\n"
        f"```python\n{canonical_solution}\n```\n\n"
        "## Test Cases\n\n"
        f"```python\n{test_cases}\n```\n\n"
        "## Entry Point\n\n"
        f"`{entry_point}`\n\n"
    )

    if extra_info:
        markdown += get_extra_info_str(extra_info)
        markdown += "\n\n"

    return markdown


def sanitize_filename(filename: str) -> str:
    return re.sub(r"[^\w\-_\. ]", "_", filename)


def convert_jsonl_to_markdown(
    input_file: str, output_dir: str, include_invalid: bool = False
) -> None:
    output_dir = os.path.join(output_dir, os.path.basename(input_file).split(".")[0])
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, "r") as file:
        for line_counter, line in enumerate(file, start=1):
            try:
                json_data = json.loads(line)
            except json.JSONDecodeError as e:
                logging.error(f"Error decoding JSON on line {line_counter}: {e}")
                continue

            is_invalid = "problem" in json_data and "reason" in json_data

            if is_invalid and not include_invalid:
                continue  # Skip invalid problems if not included

            problem_json = json_data if not is_invalid else json_data["problem"]
            reason = json_data["reason"] if is_invalid else ""

            markdown_content = json_to_markdown(problem_json)

            if is_invalid:
                reason_md = (
                    f"## Reason\n\n```\n{textwrap.dedent(reason).strip()}\n```\n\n"
                )
                markdown_content += reason_md
                output_file = os.path.join(
                    output_dir, f"line_{line_counter}_invalid.md"
                )
            else:
                task_id = problem_json["task_id"]
                sanitized_task_id = sanitize_filename(task_id)
                output_file = os.path.join(output_dir, f"{sanitized_task_id}.md")

            try:
                with open(output_file, "w") as output:
                    output.write(markdown_content)
                logging.info(f"Markdown file '{output_file}' created successfully.")
            except IOError as e:
                logging.error(f"Error writing to file '{output_file}': {e}")


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Convert JSONL to Markdown files")
    parser.add_argument("input_file", help="Path to the input JSONL file")
    parser.add_argument(
        "output_dir", help="Path to the output directory for Markdown files"
    )
    parser.add_argument(
        "--include-invalid",
        action="store_true",
        help="Include invalid problems in the output",
    )
    args = parser.parse_args()

    convert_jsonl_to_markdown(args.input_file, args.output_dir, args.include_invalid)


if __name__ == "__main__":
    main()
