import json
import logging
from typing import Dict, Any, List

import openai
from human_eval.execution import check_correctness


class ProblemValidator:
    def __init__(
        self, example_problem: str, client: openai.AzureOpenAI, config: Dict[str, Any]
    ):
        self.example_problem_dict = json.loads(example_problem)
        self.client = client
        self.config = config

    @property
    def problem_keys(self) -> set:
        return set(self.example_problem_dict.keys())

    def validate_problem(self, problem: Dict[str, Any]) -> Dict[str, Any]:
        validation_result = {"valid": True, "reason": "", "warnings": []}

        if not self.problem_keys.issubset(problem.keys()):
            return {"valid": False, "reason": "Problem keys mismatch.", "warnings": []}

        self._check_problem_structure(problem, validation_result)
        self._check_correctness(problem, validation_result)
        validation_result["warnings"].extend(self._check_gpt_feedback(problem))

        return validation_result

    def _check_problem_structure(
        self, problem: Dict[str, Any], validation_result: Dict[str, Any]
    ) -> None:
        prompt, test = problem["prompt"].strip(), problem["test"].strip()

        if not prompt.startswith("def "):
            validation_result["warnings"].append("Prompt does not start with 'def '.")
        if not test.startswith("def "):
            validation_result["warnings"].append("Test does not start with 'def '.")
        if (test_case_count := test.count("assert")) < 5:
            validation_result["warnings"].append(
                f"Only {test_case_count} test cases found. Minimum recommended is 5."
            )
        if len(prompt) < 50:
            validation_result["warnings"].append("Prompt seems too short.")
        if len(problem["canonical_solution"]) < 10:
            validation_result["warnings"].append("Canonical solution seems too short.")

    def _check_correctness(
        self, problem: Dict[str, Any], validation_result: Dict[str, Any]
    ) -> None:
        try:
            correctness_result = check_correctness(
                problem, problem["canonical_solution"], timeout=15
            )
            if not correctness_result["passed"]:
                validation_result["warnings"].append(
                    "Solution failed correctness check."
                )
        except Exception as error:
            validation_result.update(
                {"valid": False, "reason": f"Error during validation: {error}"}
            )

    def _check_gpt_feedback(self, problem: Dict[str, Any]) -> List[str]:
        system_message = {
            "role": "system",
            "content": (
                "You are an expert in analyzing and critiquing problem statements, especially for coding competitions. "
                "Please find and report any potential flaws in this problem. Focus on significant issues that make the problem unusable. "
                "The output format should be 'severity, flaw_name: description' with each flaw on a new line, severity is between 1 to 5 with 5 being the highest severity."
            ),
        }
        user_message = {"role": "user", "content": json.dumps(problem, indent=2)}

        try:
            completion = self.client.chat.completions.create(
                model=self.config["OPENAI_MODEL"],
                messages=[system_message, user_message],
            )
            gpt_feedback = completion.choices[0].message.content.split("\n")

            feedbacks = []
            for line in gpt_feedback:
                line = line.strip()
                if line:
                    try:
                        severity = int(line[: line.find(",")])
                        if severity >= 4:
                            feedbacks.append(line)
                    except (IndexError, ValueError) as parse_error:
                        logging.warning(
                            f"Unable to parse feedback line: '{line}', Error: {parse_error}"
                        )
            return feedbacks
        except openai.OpenAIError as error:
            return [f"Error getting GPT feedback: {error}"]

    def follow_up_prompt(
        self, problem: Dict[str, Any], followup_reason: str, warnings: List[str]
    ) -> Dict[str, Any]:
        system_message = {
            "role": "system",
            "content": (
                f"You are an expert problem setter for advanced coding competitions. You previously created a problem that had the following issues: "
                f"{followup_reason}. Here are some additional issues identified: {warnings}.\n"
                "Please revise and improve the problem statement to fix these issues and return JSON with same keys as the original problem."
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
