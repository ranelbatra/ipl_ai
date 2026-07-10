from score_parser import parse_phase, get_team_score

POWERPLAY_OVERS = 6
MIDDLE_OVERS = 15
TOTAL_OVERS = 20


def current_run_rate(runs, overs):
    if overs == 0:
        return 0

    return round(runs / overs, 2)


def required_run_rate(target, current_runs, overs_remaining):

    if overs_remaining <= 0:
        return 0

    runs_required = target - current_runs

    if runs_required <= 0:
        return 0

    return round(runs_required / overs_remaining, 2)


def phase_comparison(team1_name, team2_name, phase_data, overs):

    team1 = get_team_score(phase_data, team1_name)
    team2 = get_team_score(phase_data, team2_name)

    team1_rr = current_run_rate(team1["runs"], overs)
    team2_rr = current_run_rate(team2["runs"], overs)

    run_difference = abs(team1["runs"] - team2["runs"])
    wicket_difference = abs(team1["wickets"] - team2["wickets"])

    winner = None

    if team1["runs"] > team2["runs"]:
        winner = team1_name

    elif team2["runs"] > team1["runs"]:
        winner = team2_name

    else:

        if team1["wickets"] < team2["wickets"]:
            winner = team1_name

        elif team2["wickets"] < team1["wickets"]:
            winner = team2_name

        else:
            winner = "Equal"

    return {

        team1_name: {
            "runs": team1["runs"],
            "wickets": team1["wickets"],
            "run_rate": team1_rr
        },

        team2_name: {
            "runs": team2["runs"],
            "wickets": team2["wickets"],
            "run_rate": team2_rr
        },

        "run_difference": run_difference,

        "wicket_difference": wicket_difference,

        "phase_winner": winner

    }


def analyze_match(request):

    powerplay = parse_phase(request.powerplay)
    middle = parse_phase(request.middleOvers)
    death = parse_phase(request.deathOvers)

    analytics = {

        "winning_team": request.winner,

        "losing_team":
            request.team1 if request.winner == request.team2 else request.team2,

        "powerplay":
            phase_comparison(
                request.team1,
                request.team2,
                powerplay,
                POWERPLAY_OVERS
            ),

        "middle_overs":
            phase_comparison(
                request.team1,
                request.team2,
                middle,
                MIDDLE_OVERS
            ),

        "death_overs":
            phase_comparison(
                request.team1,
                request.team2,
                death,
                TOTAL_OVERS
            )
    }

    # -------------------------
    # Determine Best Phase
    # -------------------------

    phase_scores = {

        "Powerplay": analytics["powerplay"]["run_difference"],

        "Middle Overs": analytics["middle_overs"]["run_difference"],

        "Death Overs": analytics["death_overs"]["run_difference"]

    }

    analytics["best_phase"] = max(
        phase_scores,
        key=phase_scores.get
    )

    analytics["largest_run_difference"] = max(
        phase_scores.values()
    )

    # -------------------------
    # Momentum Winner
    # -------------------------

    wins = {

        request.team1: 0,

        request.team2: 0

    }

    for phase in [

        analytics["powerplay"],

        analytics["middle_overs"],

        analytics["death_overs"]

    ]:

        winner = phase["phase_winner"]

        if winner != "Equal":

            wins[winner] += 1

    analytics["momentum_winner"] = max(
        wins,
        key=wins.get
    )

    # -------------------------
    # Match Control Index
    # -------------------------

    analytics["match_control_index"] = (

        analytics["powerplay"]["run_difference"]

        + analytics["middle_overs"]["run_difference"]

        + analytics["death_overs"]["run_difference"]

    )

    # -------------------------
    # Pressure Team
    # -------------------------

    analytics["pressure_team"] = analytics["losing_team"]

    return analytics