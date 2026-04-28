from guardrails.rules import check_injection, check_logic

def run_critic(user_input, llm_output):
    print("[Critic] Running checks...")

    if check_injection(llm_output):
        return {
            "status": "rejected",
            "reason": "Possible prompt injection detected"
        }

    if not check_logic(llm_output):
        return {
            "status": "rejected",
            "reason": "Logical inconsistency detected"
        }

    return {"status": "approved"}
