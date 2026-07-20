"""
Team DNA Personality Engine
---------------------------
Determines the team's playing identity.
"""


def determine_personality(features):

    aggression = features["batting_aggression"]
    bowling = features["bowling_strength"]
    finishing = features["finishing"]
    consistency = features["batting_consistency"]
    pace = features["pace_attack"]
    spin = features["spin_attack"]

    # -----------------------------------
    # Aggressive Batting
    # -----------------------------------

    if aggression >= 85 and finishing >= 80:
        return "Fearless Finishers"

    # -----------------------------------
    # Pace Dominated
    # -----------------------------------

    if bowling >= 85 and pace >= spin:
        return "Pace Powerhouse"

    # -----------------------------------
    # Spin Dominated
    # -----------------------------------

    if bowling >= 85 and spin > pace:
        return "Spin Masters"

    # -----------------------------------
    # Consistent Team
    # -----------------------------------

    if consistency >= 80:
        return "Consistent Contenders"

    # -----------------------------------
    # Big Hitters
    # -----------------------------------

    if aggression >= 80:
        return "Power Hitters"

    # -----------------------------------
    # Bowling Team
    # -----------------------------------

    if bowling >= 80:
        return "Bowling Dominators"

    # -----------------------------------
    # Balanced
    # -----------------------------------

    return "Balanced Challengers"