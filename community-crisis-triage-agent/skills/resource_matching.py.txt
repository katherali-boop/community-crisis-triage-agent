# skills/resource_matching.py

def match_resources(crisis_info: dict, resources: dict) -> list:
    """
    Build a simple action plan from resources.
    """
    plan = []
    crisis_type = crisis_info.get("crisis_type", "unknown")

    for category, items in resources.items():
        for item in items:
            name = item.get("name", "service")
            phone = item.get("phone", "N/A")
            step_text = f"Contact {name} ({category}), phone: {phone}"
            plan.append({
                "step": step_text,
                "category": category,
                "details": item,
                "crisis_type": crisis_type,
            })

    if not plan:
        plan.append({
            "step": "Visit your nearest community center for general support.",
            "category": "community_centers",
            "details": {},
            "crisis_type": crisis_type,
        })

    return plan
