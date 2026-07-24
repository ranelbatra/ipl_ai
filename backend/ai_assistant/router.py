from ai_assistant.intents import detect_intent, Intent
from ai_assistant.retriever import extract_entities


def process_question(question, analytics):

    intent = detect_intent(question)

    entities = extract_entities(question)


    if intent == Intent.COMPARISON:

        teams = entities["teams"]

        if len(teams) >= 2:

            return analytics.compare_teams(
                teams[0],
                teams[1]
            )


    elif intent == Intent.TEAM_STATS:

        teams = entities["teams"]

        if len(teams) >= 1:

            return analytics.team_profile(
                teams[0]
            )


    elif intent == Intent.PLAYER_STATS:

        # later connect player extraction
        return {
            "message": "Player analytics coming soon"
        }


    elif intent == Intent.MATCH_SUMMARY:

        return {
            "message": "Match summary coming soon"
        }


    elif intent == Intent.STRATEGY:

        return {
            "message": "Strategy analysis coming soon"
        }


    elif intent == Intent.PREDICTION:

        return {
            "message": "Prediction module coming soon"
        }


    return {
        "message": "I could not understand your question"
    }