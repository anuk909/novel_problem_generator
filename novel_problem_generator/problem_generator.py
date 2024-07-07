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
        self.validator = ProblemValidator(self.example_problem, self.client, config)
        self._validate_example_problem()
        self.output_paths = self._setup_output_paths()

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
            json.loads(self.example_problem)
        )
        if not example_validation["valid"]:
            raise ValueError(
                f"Example problem is invalid, reason: {example_validation['reason']}"
            )
        if example_validation.get("warnings"):
            logging.warning(
                f"Example problem has warnings: {example_validation['warnings']}"
            )

    def _setup_output_paths(self) -> Dict[str, str]:
        timestamp = int(time.time())
        return {
            "new_problems": os.path.join(
                self.config["OUTPUT_DIR"], f"new_problems_{timestamp}.jsonl"
            ),
            "invalid_problems": os.path.join(
                self.config["OUTPUT_DIR"], f"invalid_problems_{timestamp}.jsonl"
            ),
        }

    @property
    def task_id_class(self) -> str:
        task_id = json.loads(self.example_problem).get("task_id")
        return task_id.split("/")[0] if task_id else ""

    def generate_problem(self, task_id: str) -> Dict[str, Any]:
        cover_story_words, topics = random.sample(
            self.cover_story_words, 2
        ), random.sample(self.topics, 2)
        messages = (
            self._get_system_message(),
            self._get_user_message(cover_story_words, topics),
        )

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
            "cleaned_prompt": problem_dict.pop("cleaned_prompt", ""),
        }
        return problem_dict

    def _get_system_message(self) -> ChatCompletionSystemMessageParam:
        return {
            "role": "system",
            "content": (
                "You are an expert problem setter for advanced coding competitions. Create highly novel and complex problems "
                "for the HumanEval Dataset. Requirements:\n"
                f"1. JSON format with keys: {self.validator.problem_keys}.\n"
                f"2. Example: {self.example_problem}\n"
                "3. Prompt must start with 'def' and include examples that will help understanding the problem.\n"
                "4. Test cases must start with 'def' and include at least five complex cases.\n"
                "5. Solution must pass test cases and complete the prompt code without redefining the entry_point function from the prompt.\n"
                "6. Combine multiple concepts uniquely and efficiently.\n"
                "7. Include constraints or twists, and consider time/space complexity requirements.\n"
                "8. The problem should require at least 30 lines to solve.\n"
                "9. Include a 'cleaned_prompt' field that matches the problem prompt but without all the cover story around it, "
                "make sure that the core concept of the questions stays the same and there are some examples and explanations that "
                "makes it easy to understand."
            ),
        }

    def _get_user_message(
        self, cover_story_words: List[str], topics: List[str]
    ) -> ChatCompletionUserMessageParam:
        cover_story_str = " and ".join(cover_story_words)
        topics_str = " and ".join(topics)
        return {
            "role": "user",
            "content": (
                f"Create a problem with a cover story about {cover_story_str} and involving the topics: {topics_str}. "
                "Use concepts from machine learning and ensure complexity and novelty."
            ),
        }

    def save_problem(
        self, problem: Dict[str, Any], is_valid: bool, reason: str = ""
    ) -> None:
        path = self.output_paths["new_problems" if is_valid else "invalid_problems"]
        if not is_valid:
            problem["invalid_reason"] = reason
        FileHandler.save_jsonl(path, problem)
