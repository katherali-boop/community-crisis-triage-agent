
---

## 🧠 agents/intake_agent.py

```python
# agents/intake_agent.py

class IntakeAgent:
    """
    IntakeAgent
    -----------
    - Collects the user's description.
    - Extracts basic details (needs, urgency).
    - Normalizes input for downstream agents.
    """

    def extract_details(self, user_input: str) -> dict:
        text = user_input.lower()
        needs = []

        if any(word in text for word in ["evict", "leave", "nowhere to go", "homeless"]):
            needs.append("housing")
        if any(word in text for word in ["hungry", "no food", "food"]):
            needs.append("food")
        if any(word in text for word in ["anxious", "depressed", "overwhelmed", "panic"]):
            needs.append("mental_health")

        return {
            "raw_text": user_input,
            "needs": needs,
            "urgency": "unknown",
        }
