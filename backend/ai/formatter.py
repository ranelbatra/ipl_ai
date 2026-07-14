def format_phase(phase_name, data):

    # Get both team names automatically
    teams = [key for key in data.keys() if isinstance(data[key], dict)]

    team1 = teams[0]
    team2 = teams[1]

    text = f"""
==============================
{phase_name.upper()}
==============================

{team1}
Runs: {data[team1]["runs"]}
Wickets Lost: {data[team1]["wickets"]}
Current Run Rate: {data[team1]["run_rate"]}

{team2}
Runs: {data[team2]["runs"]}
Wickets Lost: {data[team2]["wickets"]}
Current Run Rate: {data[team2]["run_rate"]}

Run Difference: {data["run_difference"]}
Wicket Difference: {data["wicket_difference"]}

Phase Winner: {data["phase_winner"]}

"""

    return text


def format_analytics(analytics):

    report = """
=========== BACKEND ANALYTICS ===========
These analytics are calculated by the backend.
Treat them as factual.
Do NOT recalculate any values.

"""

    report += format_phase(
        "Powerplay",
        analytics["powerplay"]
    )

    report += format_phase(
        "Middle Overs",
        analytics["middle_overs"]
    )

    report += format_phase(
        "Death Overs",
        analytics["death_overs"]
    )

    report += "\n=========== END OF ANALYTICS ==========="

    report += f"""

================ MATCH SUMMARY ================

Winning Team: {analytics["winning_team"]}

Losing Team: {analytics["losing_team"]}

Best Phase: {analytics["best_phase"]}

Momentum Winner: {analytics["momentum_winner"]}

Pressure Team: {analytics["pressure_team"]}

Largest Run Difference: {analytics["largest_run_difference"]}

Match Control Index: {analytics["match_control_index"]}

===============================================

"""

    return report