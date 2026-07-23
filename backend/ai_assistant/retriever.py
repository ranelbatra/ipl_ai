"""
Entity Retriever
----------------
Extracts cricket entities (teams, players, seasons, venues)
from a user's question.
"""

import re

# IPL Teams
TEAMS = {
    "CSK": "Chennai Super Kings",
    "MI": "Mumbai Indians",
    "RCB": "Royal Challengers Bangalore",
    "KKR": "Kolkata Knight Riders",
    "DC": "Delhi Capitals",
    "PBKS": "Punjab Kings",
    "RR": "Rajasthan Royals",
    "SRH": "Sunrisers Hyderabad",
    "GT": "Gujarat Titans",
    "LSG": "Lucknow Super Giants"
}


def extract_entities(question: str):
    """
    Returns all detected entities.

    Example
    -------
    {
        "teams": [...],
        "season": "2023",
        "players": [],
        "venues": []
    }
    """

    q = question.lower()

    entities = {
        "teams": [],
        "players": [],
        "season": None,
        "venues": []
    }

    # -------- Teams --------

    for short, full in TEAMS.items():

        if short.lower() in q or full.lower() in q:
            entities["teams"].append(full)

    # -------- Season --------

    season = re.findall(r"\b20\d{2}\b", q)

    if season:
        entities["season"] = season[0]

    return entities