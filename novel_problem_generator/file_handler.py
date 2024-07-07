import json
import logging

from typing import Any, Dict


class FileHandler:
    @staticmethod
    def load_file(path: str) -> str:
        try:
            with open(path, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise ValueError(f"File not found: {path}")

    @staticmethod
    def load_json_file(path: str) -> Any:
        try:
            return json.loads(FileHandler.load_file(path))
        except json.JSONDecodeError as error:
            raise ValueError(f"Error loading JSON file: {path}. Error: {error}")

    @staticmethod
    def save_jsonl(path: str, data: Dict[str, Any]) -> None:
        try:
            with open(path, "a") as file:
                json.dump(data, file)
                file.write("\n")
            logging.info(f"Data saved to {path}")
        except Exception as e:
            logging.error(f"Error saving data to {path}: {e}")
