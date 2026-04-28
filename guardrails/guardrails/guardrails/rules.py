def check_injection(text):
    suspicious_patterns = [
        "ignore previous instructions",
        "system override",
        "bypass safety"
    ]

    for pattern in suspicious_patterns:
        if pattern.lower() in text.lower():
            return True

    return False


def check_logic(text):
    # VERY basic placeholder
    if len(text) < 5:
        return False
    return True
