"""
Match Aura Metrics
------------------
Contains all numerical calculations used by the Match Aura Engine.
All returned values are scaled between 0 and 100.
"""


def clamp(value, minimum=0, maximum=100):
    """
    Ensures the metric stays between 0 and 100.
    """
    return max(minimum, min(value, maximum))


# --------------------------------------------------
# Battle Meter
# --------------------------------------------------

def calculate_battle_meter(win_margin, margin_type):
    """
    Calculates how competitive the match was.

    Higher score = closer match.
    """

    if margin_type == "runs":

        if win_margin <= 5:
            score = 100
        elif win_margin <= 15:
            score = 90
        elif win_margin <= 30:
            score = 75
        elif win_margin <= 50:
            score = 60
        else:
            score = 40

    elif margin_type == "wickets":

        if win_margin == 1:
            score = 100
        elif win_margin <= 3:
            score = 90
        elif win_margin <= 5:
            score = 75
        elif win_margin <= 7:
            score = 60
        else:
            score = 40

    else:
        score = 50

    return clamp(score)


# --------------------------------------------------
# Hype Meter
# --------------------------------------------------

def calculate_hype_meter(boundaries, sixes):
    """
    Measures how exciting the batting was.
    """

    score = (
        boundaries * 1.5 +
        sixes * 3
    )

    return clamp(round(score))


# --------------------------------------------------
# Aura Score
# --------------------------------------------------

def calculate_aura_score(
    battle_meter,
    hype_meter
):
    """
    Overall Match Aura.

    More metrics will be added in future versions.
    """

    score = (
        battle_meter * 0.5 +
        hype_meter * 0.5
    )

    return clamp(round(score))