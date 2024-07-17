import os
from typing import Dict, Any, Optional, List
import openai
from openai.types.chat import ChatCompletion


def load_config() -> Dict[str, Any]:
    required_vars = ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT"]
    config = {var: os.environ.get(var) for var in required_vars}

    if not all(config.values()):
        missing = [var for var, value in config.items() if not value]
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}"
        )

    config.update(
        {
            "AZURE_OPENAI_API_VERSION": "2024-04-01-preview",
            "OPENAI_MODEL": "gpt-4-turbo-2024-04-09",
            "ATTEMPTS": 10,
            "OUTPUT_DIR": "problems/baseline/",
        }
    )

    return config


def get_openai_client(config: Dict[str, str]) -> openai.AzureOpenAI:
    try:
        return openai.AzureOpenAI(
            api_key=config["AZURE_OPENAI_API_KEY"],
            azure_endpoint=config["AZURE_OPENAI_ENDPOINT"],
            api_version=config["AZURE_OPENAI_API_VERSION"],
        )
    except openai.AuthenticationError as error:
        raise ValueError(f"Authentication failed: {error}") from error


def generate_problem(
    client: openai.AzureOpenAI, prompt: str, config: Dict[str, Any]
) -> Optional[List[str]]:
    try:
        completion: ChatCompletion = client.chat.completions.create(
            model=config["OPENAI_MODEL"], messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content.strip().split("\n")
    except openai.APIError as e:
        print(f"OpenAI API error: {e}")
    except Exception as e:
        print(f"Unexpected error generating problem: {e}")
    return None


def save_problem(problem: List[str], file_path: str) -> None:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write("\n".join(problem))


def main() -> None:
    try:
        config = load_config()
        client = get_openai_client(config)
        prompt = "Please generate a novel coding exercise and canonical python solution in leet code style"
        attempts = config["ATTEMPTS"]
        output_dir = config["OUTPUT_DIR"]

        for attempt in range(attempts):
            problem = generate_problem(client, prompt, config)
            if problem:
                print(f"Generated problem {attempt + 1}")
                file_path = os.path.join(output_dir, f"problem_{attempt + 1}.txt")
                save_problem(problem, file_path)
            else:
                print(f"Attempt {attempt + 1} failed. Retrying...")

        print(f"Generation complete. Problems saved in {output_dir}")

    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
