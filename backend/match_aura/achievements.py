"""
Match Achievement Engine
------------------------
Awards badges based on what happened during the match.
"""


def generate_achievements(
    total_boundaries,
    total_sixes,
    win_margin,
    margin_type,
    plot_twist_count,
    defended_low_total=False,
    chased_200=False
):
    """
    Returns a list of achievements unlocked during the match.
    """

    achievements = []

    # -----------------------------------
    # Boundary Barrage
    # -----------------------------------

    if total_boundaries >= 35:
        achievements.append("🏅 Boundary Barrage")

    # -----------------------------------
    # Six Machine
    # -----------------------------------

    if total_sixes >= 15:
        achievements.append("🚀 Six Machine")

    # -----------------------------------
    # Ice In The Veins
    # -----------------------------------

    if (
        (margin_type == "runs" and win_margin <= 10)
        or
        (margin_type == "wickets" and win_margin <= 2)
    ):
        achievements.append("🥶 Ice In The Veins")

    # -----------------------------------
    # Plot Twist
    # -----------------------------------

    if plot_twist_count >= 3:
        achievements.append("🎭 Plot Twist Master")

    # -----------------------------------
    # Fortress Defense
    # -----------------------------------

    if defended_low_total:
        achievements.append("🛡️ Fortress Defense")

    # -----------------------------------
    # Chase Master
    # -----------------------------------

    if chased_200:
        achievements.append("⚡ Chase Master")

    # -----------------------------------
    # Clean Victory
    # -----------------------------------

    if (
        margin_type == "runs"
        and win_margin >= 50
    ):
        achievements.append("👑 Statement Win")

    return achievements