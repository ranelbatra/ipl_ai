"""
Intent Detection Module
-----------------------
Determines what kind of cricket question the user is asking.
"""

from enum import Enum
import re


class Intent(Enum):
    COMPARISON = "comparison"
    PLAYER_STATS = "player_stats"
    TEAM_STATS = "team_stats"
    MATCH_SUMMARY = "match_summary"
    STRATEGY = "strategy"
    PREDICTION = "prediction"
    KNOWLEDGE = "knowledge"
    GENERAL = "general"


def detect_intent(question: str) -> Intent:
    """
    Detects the user's cricket-related intent.

    Parameters
    ----------
    question : str

    Returns
    -------
    Intent
    """

    q = question.lower()

    if any(word in q for word in ["compare", "vs", "versus"]):
        return Intent.COMPARISON

    if any(word in q for word in ["player", "runs", "wickets", "strike rate"]):
        return Intent.PLAYER_STATS

    if any(word in q for word in ["team", "franchise"]):
        return Intent.TEAM_STATS

    if any(word in q for word in ["summary", "recap", "what happened"]):
        return Intent.MATCH_SUMMARY

    if any(word in q for word in ["strategy", "captain", "coach"]):
        return Intent.STRATEGY

    if any(word in q for word in ["predict", "prediction", "winner"]):
        return Intent.PREDICTION

    if any(word in q for word in ["what is", "explain", "how does"]):
        return Intent.KNOWLEDGE

    return Intent.GENERAL