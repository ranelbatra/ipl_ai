"""
Momentum Timeline
-----------------
Determines which team controlled each phase of the match.
"""


def phase_winner(team1_runs, team2_runs):
    """
    Returns the team that dominated a phase.
    """

    if team1_runs > team2_runs:
        return "Team 1"

    elif team2_runs > team1_runs:
        return "Team 2"

    return "Balanced"


def generate_momentum_timeline(
    team1_name,
    team2_name,
    powerplay,
    middle_overs,
    death_overs,
):
    """
    powerplay = (team1_runs, team2_runs)
    middle_overs = (team1_runs, team2_runs)
    death_overs = (team1_runs, team2_runs)

    Returns a timeline showing control in each phase.
    """

    timeline = []

    # -----------------------------
    # Powerplay
    # -----------------------------

    winner = phase_winner(powerplay[0], powerplay[1])

    if winner == "Team 1":
        timeline.append(f"⚡ Powerplay: {team1_name}")

    elif winner == "Team 2":
        timeline.append(f"⚡ Powerplay: {team2_name}")

    else:
        timeline.append("⚡ Powerplay: Balanced")

    # -----------------------------
    # Middle Overs
    # -----------------------------

    winner = phase_winner(middle_overs[0], middle_overs[1])

    if winner == "Team 1":
        timeline.append(f"🎯 Middle Overs: {team1_name}")

    elif winner == "Team 2":
        timeline.append(f"🎯 Middle Overs: {team2_name}")

    else:
        timeline.append("🎯 Middle Overs: Balanced")

    # -----------------------------
    # Death Overs
    # -----------------------------

    winner = phase_winner(death_overs[0], death_overs[1])

    if winner == "Team 1":
        timeline.append(f"🔥 Death Overs: {team1_name}")

    elif winner == "Team 2":
        timeline.append(f"🔥 Death Overs: {team2_name}")

    else:
        timeline.append("🔥 Death Overs: Balanced")

    return timeline