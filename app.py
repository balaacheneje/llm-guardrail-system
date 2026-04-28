from guardrails.validator import validate_output

def main():
    user_input = input("Enter prompt: ")

    # Simulated LLM response
    llm_output = f"Generated response for: {user_input}"

    result = validate_output(user_input, llm_output)

    print("\n--- FINAL OUTPUT ---")
    print(result)

if __name__ == "__main__":
    main()
