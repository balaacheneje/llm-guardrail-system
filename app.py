import os
from dotenv import load_dotenv
import requests
from guardrails.validator import validate_output

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_llm(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    return response.json()["choices"][0]["message"]["content"]


def main():
    user_input = input("Enter prompt: ")

    llm_output = call_llm(user_input)

    result = validate_output(user_input, llm_output)

    print("\n--- FINAL OUTPUT ---")
    print(result)


if __name__ == "__main__":
    main()
