# agents/safety_agent.py

from skills.safety_evaluation import evaluate_safety

class SafetyAgent:
    """
    SafetyAgent
    -----------
    - Evaluates risk.
    - Provides safety messaging.
    """

    def check(self, intake_data: dict, crisis_info: dict) -> dict:
        return evaluate_safety(intake_data, crisis_info)
