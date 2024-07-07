import json
import logging
import os
import random
import time
from typing import Dict, Any, List, Tuple

import openai
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

from novel_problem_generator.file_handler import FileHandler
from novel_problem_generator.problem_validator import ProblemValidator


class ProblemGenerator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.client = self._setup_openai_client()
        self.example_problem = FileHandler.load_file(
            self.config["EXAMPLE_PROBLEM_PATH"]
        )
        self.cover_story_words = FileHandler.load_json_file(
            self.config["COVER_STORY_PATH"]
        )
        self.topics = FileHandler.load_json_file(self.config["TOPICS_PATH"])
        self.fields = FileHandler.load_json_file(self.config["FIELDS_PATH"])
        self.validator = ProblemValidator(self.example_problem, self.client, config)
        self._validate_example_problem()
        self.output_paths = self.get_output_file_paths()

    def _setup_openai_client(self) -> openai.AzureOpenAI:
        try:
            return openai.AzureOpenAI(
                api_key=self.config["AZURE_OPENAI_API_KEY"],
                azure_endpoint=self.config["AZURE_OPENAI_ENDPOINT"],
                api_version=self.config["AZURE_OPENAI_API_VERSION"],
            )
        except openai.AuthenticationError as error:
            logging.error(f"Authentication error: {error}")
            raise

    def _validate_example_problem(self) -> None:
        example_validation = self.validator.validate_problem(
            problem=json.loads(self.example_problem), check_gpt_feedback=False
        )
        if not example_validation["valid"]:
            raise ValueError(
                f"Example problem is invalid, reason: {example_validation['reason']}"
            )
        if example_validation.get("warnings"):
            logging.warning(
                f"Example problem has warnings: {example_validation['warnings']}"
            )

    def get_output_file_paths(self):
        output_dir = self.config["OUTPUT_DIR"]
        output_base_name = self.config["OUTPUT_BASE_NAME"]
        add_timestamp = self.config["ADD_TIMESTAMP"]

        if add_timestamp:
            timestamp = int(time.time())
            new_problems_file = f"{output_base_name}_{timestamp}.jsonl"
            invalid_problems_file = f"invalid_problems_{timestamp}.jsonl"
        else:
            new_problems_file = f"{output_base_name}.jsonl"
            invalid_problems_file = "invalid_problems.jsonl"

        return {
            "new_problems": os.path.join(output_dir, new_problems_file),
            "invalid_problems": os.path.join(output_dir, invalid_problems_file),
        }

    @property
    def task_id_class(self) -> str:
        task_id = json.loads(self.example_problem).get("task_id")
        return task_id.split("/")[0] if task_id else ""

    def generate_problem(self, task_id: str) -> Dict[str, Any]:
        use_cover_story = self.config.get("USE_COVER_STORY", False)
        use_topics = self.config.get("USE_TOPICS", False)
        use_field = self.config.get("USE_FIELD", False)
        require_30_lines = self.config.get("REQUIRE_30_LINES", False)

        cover_story_words, topics, field = [], [], ""
        if use_cover_story:
            cover_story_words = random.sample(self.cover_story_words, 2)
        if use_topics:
            topics = random.sample(self.topics, 2)
        if use_field:
            field = random.sample(self.fields, 1)

        messages = [
            self._get_system_message(require_30_lines),
            self._get_user_message(cover_story_words, topics, field),
        ]

        try:
            completion = self.client.chat.completions.create(
                model=self.config["OPENAI_MODEL"],
                messages=messages,
                response_format={"type": "json_object"},
            )
            problem_dict = json.loads(completion.choices[0].message.content)
        except (openai.OpenAIError, json.JSONDecodeError) as error:
            logging.error(f"Error generating problem: {error}")
            raise

        problem_dict["task_id"] = task_id
        problem_dict["extra_info"] = {
            "cover_story_words": cover_story_words,
            "topics": topics,
            "field": field,
            "cleaned_prompt": problem_dict.pop("cleaned_prompt", ""),
        }
        return problem_dict

    def _get_system_message(
        self, require_30_lines: bool
    ) -> ChatCompletionSystemMessageParam:
        constraints = [
            "Create highly novel and complex problems for the HumanEval Dataset. The initial constraints for the problem are:",
            f"JSON format with keys: {self.validator.problem_keys}.",
            f"Example: {self.example_problem}",
            "Prompt must start with 'def' and include examples that will help in understanding the problem.",
            "Test cases must start with 'def' and include at least five different cases.",
            "Canonical Solution must pass all test cases.",
            "Canonical Solution must start with tab and the implemention of the function from the prompt. It shouldn't (!!!) "
            "redefine the function from the prompt (and entry_point) in order to match the HumanEval execution format.",
        ]
        if require_30_lines:
            constraints.append(
                "The problem Should be hard to solve and require at least 30 lines to solve."
            )
        constraints.append(
            "Include a 'cleaned_prompt' field that matches the problem prompt but without all the cover story around it, while maintaining the core field and include examples and explanations that make it easy to understand."
        )

        constraints_str = "\n".join(constraints)
        return {
            "role": "system",
            "content": (
                "You are an expert problem setter for advanced coding competitions. Requirements:\n"
                f"{constraints_str}"
            ),
        }

    def _get_user_message(
        self, cover_story_words: List[str], topics: List[str], field: str
    ) -> ChatCompletionUserMessageParam:
        content_parts = ["Create a novel and complex problem"]
        if cover_story_words:
            content_parts.append(
                f"with cover story words: {', '.join(cover_story_words)}"
            )
        if topics:
            content_parts.append(f"related to the topics: {', '.join(topics)}")
        if field:
            content_parts.append(
                f"using concepts and algorithms from the field: {field}"
            )

        content = " ".join(content_parts)
        return {
            "role": "user",
            "content": content,
        }

    def follow_up_prompt(
        self, problem: Dict[str, Any], followup_reason: str, warnings: List[str]
    ) -> Dict[str, Any]:
        system_message = {
            "role": "system",
            "content": (
                f"You are an expert problem setter for advanced coding competitions. You previously created a problem that had the following issues: "
                f"{followup_reason}. Here are some additional issues identified: {warnings}.\n"
                "Please revise and improve the problem statement to fix these issues and return JSON with same keys as the original problem."
                f"The content of the system prompt to generate this problem were :{self._get_system_message(self.config['REQUIRE_30_LINES'])}"
            ),
        }
        user_message = {"role": "user", "content": json.dumps(problem, indent=2)}

        try:
            completion = self.client.chat.completions.create(
                model=self.config["OPENAI_MODEL"],
                messages=[system_message, user_message],
                response_format={"type": "json_object"},
            )
            return json.loads(completion.choices[0].message.content)
        except (json.JSONDecodeError, openai.OpenAIError) as error:
            logging.error(f"Error during follow-up: {error}")
            raise

    def save_problem(
        self, problem: Dict[str, Any], is_valid: bool, reason: str = ""
    ) -> None:
        path = self.output_paths["new_problems" if is_valid else "invalid_problems"]
        if not is_valid:
            problem["invalid_reason"] = reason
        FileHandler.save_jsonl(path, problem)
