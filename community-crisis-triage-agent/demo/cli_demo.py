# demo/cli_demo.py

from agents.intake_agent import IntakeAgent
from agents.classification_agent import ClassificationAgent
from agents.safety_agent import SafetyAgent
from agents.routing_agent import RoutingAgent

def main():
    print("Community Crisis Triage Agent (CLI Demo)")
    print("----------------------------------------")
    user_input = input("Describe your situation: ")

    intake = IntakeAgent()
    classification = ClassificationAgent()
    safety = SafetyAgent()
    routing = RoutingAgent()

    intake_data = intake.extract_details(user_input)
    crisis_info = classification.classify(intake_data)
    safety_info = safety.check(intake_data, crisis_info)
    routing_info = routing.route(crisis_info)

    print("\n--- Intake Data ---")
    print(intake_data)

    print("\n--- Crisis Classification ---")
    print(crisis_info)

    print("\n--- Safety Check ---")
    print(safety_info["message"])

    print("\n--- Recommended Action Plan ---")
    for step in routing_info["action_plan"]:
        print(f"- {step['step']}")

if __name__ == "__main__":
    main()
