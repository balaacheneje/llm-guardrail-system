from guardrails.critic import run_critic

def validate_output(user_input, llm_output):
    print("\n[Validator] Checking output...")

    critic_result = run_critic(user_input, llm_output)

    if critic_result["status"] == "approved":
        return llm_output
    else:
        return f"[BLOCKED] Reason: {critic_result['reason']}"
