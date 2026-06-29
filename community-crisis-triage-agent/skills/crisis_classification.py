# skills/crisis_classification.py

def classify_crisis(intake_data: dict) -> dict:
    """
    Simple rule-based crisis classification.
    Replace with more advanced logic if desired.
    """
    text = intake_data["raw_text"].lower()
    needs = intake_data.get("needs", [])

    if "housing" in needs:
        crisis_type = "housing"
        urgency = "high"
    elif "food" in needs:
        crisis_type = "food"
        urgency = "medium"
    elif "mental_health" in needs:
        crisis_type = "mental_health"
        urgency = "medium"
    else:
        crisis_type = "unknown"
        urgency = "unknown"

    risk_indicators = []
    if any(word in text for word in ["violence", "abuse", "threat"]):
        risk_indicators.append("potential_safety_issue")

    return {
        "crisis_type": crisis_type,
        "urgency": urgency,
        "risk_indicators": risk_indicators,
    }
