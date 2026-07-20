"""
Signature Moment Engine
-----------------------
Identifies the single defining moment of a match.
"""


def determine_signature_moment(
    powerplay_winner,
    middle_winner,
    death_winner,
    win_margin,
    margin_type,
    plot_twist_count
):
    """
    Returns the defining moment of the match.
    """

    # ------------------------------------
    # Last-over thriller
    # ------------------------------------

    if (
        margin_type == "runs" and win_margin <= 10
    ) or (
        margin_type == "wickets" and win_margin <= 2
    ):
        return "🔥 Last-over thriller sealed the match."

    # ------------------------------------
    # Crazy momentum shifts
    # ------------------------------------

    if plot_twist_count >= 3:
        return "🎢 Momentum completely shifted during the middle overs."

    # ------------------------------------
    # Powerplay domination
    # ------------------------------------

    if (
        powerplay_winner == death_winner
        and powerplay_winner != "Balanced"
    ):
        return f"⚡ {powerplay_winner} dominated from the Powerplay to the finish."

    # ------------------------------------
    # Death overs won the game
    # ------------------------------------

    if death_winner != "Balanced":
        return f"💥 {death_winner} owned the death overs."

    # ------------------------------------
    # Default
    # ------------------------------------

    return "🏏 A balanced contest with no single defining moment."