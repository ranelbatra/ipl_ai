from intents import detect_intent

questions = [
    "Compare RCB vs CSK",
    "Who scored the most runs in IPL 2025?",
    "Explain DLS rule",
    "Which team has the best bowling attack?",
    "Give me the match summary",
    "Predict tomorrow's winner",
    "What should the captain do now?"
]

for q in questions:
    intent = detect_intent(q)
    print(f"Question: {q}")
    print(f"Intent: {intent.value}")
    print("-" * 50)
