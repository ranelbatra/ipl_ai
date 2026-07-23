from retriever import extract_entities

questions = [

    "Compare RCB vs CSK",

    "Who won IPL 2023?",

    "Compare Mumbai Indians and Chennai Super Kings",

    "RCB batting in 2022"

]

for q in questions:

    print(q)
    print(extract_entities(q))
    print()