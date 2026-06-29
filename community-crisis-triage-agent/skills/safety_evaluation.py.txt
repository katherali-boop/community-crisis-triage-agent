# skills/safety_evaluation.py

def evaluate_safety(intake_data: dict, crisis_info: dict) -> dict:
    text = intake_data["raw_text"].lower()

    danger_keywords = ["hurt myself", "suicide", "kill myself", "end my life"]
    danger = any(kw in text for kw in danger_keywords)

    message = (
        "If you are in immediate danger or thinking of harming yourself, "
        "please contact emergency services or a crisis hotline right now."
        if danger else
        "This agent does not replace professional help. Consider reaching out "
        "to local services for additional support."
    )

    return {
        "is_emergency": danger,
        "message": message,
    }
