# agents/classification_agent.py

from skills.crisis_classification import classify_crisis

class ClassificationAgent:
    """
    ClassificationAgent
    --------------------
    - Classifies crisis type.
    - Assigns urgency.
    - Identifies basic risk indicators.
    """

    def classify(self, intake_data: dict) -> dict:
        return classify_crisis(intake_data)
