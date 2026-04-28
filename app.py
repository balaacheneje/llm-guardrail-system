import requests
from guardrails.validator import validate_output

API_KEY = "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"

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
