"""
Match Personality Engine
------------------------
Assigns a unique personality to every match
based on Match Aura metrics.
"""


def determine_personality(
    aura_score,
    battle_meter,
    hype_meter,
    plot_twist_count
):
    """
    Returns the Match Personality.
    """

    # ------------------------------------
    # Legendary Match
    # ------------------------------------

    if (
        aura_score >= 95
        and battle_meter >= 90
        and hype_meter >= 90
        and plot_twist_count >= 3
    ):
        return "🌟 Absolute Cinema"

    # ------------------------------------
    # Crazy Close Match
    # ------------------------------------

    elif (
        battle_meter >= 90
        and plot_twist_count >= 2
    ):
        return "🎢 Rollercoaster"

    # ------------------------------------
    # High Scoring
    # ------------------------------------

    elif hype_meter >= 90:
        return "🔥 Firefight"

    # ------------------------------------
    # One-sided domination
    # ------------------------------------

    elif (
        aura_score >= 90
        and battle_meter <= 45
    ):
        return "👑 Kingdom"

    # ------------------------------------
    # Very tactical game
    # ------------------------------------

    elif (
        hype_meter < 60
        and battle_meter >= 70
    ):
        return "🎯 Precision"

    # ------------------------------------
    # Average match
    # ------------------------------------

    elif aura_score >= 70:
        return "⚡ Competitive"

    # ------------------------------------
    # Low excitement
    # ------------------------------------

    return "🌥️ Balanced"