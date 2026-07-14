from .score_parser import (
    parse_phase,
    compare_phase
)


# --------------------------------------------------
# Overs in each phase
# --------------------------------------------------

POWERPLAY_OVERS = 6
MIDDLE_OVERS = 10
DEATH_OVERS = 4


# --------------------------------------------------
# Run Rate Calculator
# --------------------------------------------------

def run_rate(runs, overs):

    if overs == 0:
        return 0

    return round(runs / overs, 2)


# --------------------------------------------------
# Calculate run rates for every phase
# --------------------------------------------------

def calculate_run_rates(match):

    phases = {

        "Powerplay": (
            match["powerplay"],
            POWERPLAY_OVERS
        ),

        "Middle Overs": (
            match["middle"],
            MIDDLE_OVERS
        ),

        "Death Overs": (
            match["death"],
            DEATH_OVERS
        )

    }

    result = {}

    for phase_name, (phase, overs) in phases.items():

        parsed = parse_phase(phase)

        result[phase_name] = {}

        for team, score in parsed.items():

            result[phase_name][team] = {

                "runs": score["runs"],

                "wickets": score["wickets"],

                "run_rate": run_rate(
                    score["runs"],
                    overs
                )

            }

    return result


# --------------------------------------------------
# Phase Winners
# --------------------------------------------------

def calculate_phase_winners(match):

    winners = {}

    winners["Powerplay"] = compare_phase(
        match["powerplay"]
    )

    winners["Middle Overs"] = compare_phase(
        match["middle"]
    )

    winners["Death Overs"] = compare_phase(
        match["death"]
    )

    return winners


# --------------------------------------------------
# Required Run Rate
# --------------------------------------------------

def calculate_required_rate(match):

    if "rrr" not in match:
        return "N/A"

    return match["rrr"]


# --------------------------------------------------
# Net Run Difference
# --------------------------------------------------

def net_run_difference(match):

    parsed = parse_phase(match["death"])

    teams = list(parsed.keys())

    if len(teams) != 2:
        return 0

    t1 = teams[0]
    t2 = teams[1]

    return abs(

        parsed[t1]["runs"] -

        parsed[t2]["runs"]

    )


# --------------------------------------------------
# Total wickets lost
# --------------------------------------------------

def total_wickets(match):

    result = {}

    for phase in [

        match["powerplay"],

        match["middle"],

        match["death"]

    ]:

        parsed = parse_phase(phase)

        for team, score in parsed.items():

            result.setdefault(team, 0)

            result[team] += score["wickets"]

    return result


# --------------------------------------------------
# Dominance Score
# --------------------------------------------------

def dominance_score(match):

    winners = calculate_phase_winners(match)

    score = {}

    for phase in winners.values():

        if phase is None:
            continue

        winner = phase["winner"]

        if winner == "Tie":
            continue

        score.setdefault(winner, 0)

        score[winner] += 1

    return score


# --------------------------------------------------
# Collapse Index
# --------------------------------------------------

def collapse_index(match):

    wickets = total_wickets(match)

    collapse = {}

    for team, wkts in wickets.items():

        if wkts >= 8:

            collapse[team] = "Severe"

        elif wkts >= 6:

            collapse[team] = "High"

        elif wkts >= 4:

            collapse[team] = "Medium"

        else:

            collapse[team] = "Low"

    return collapse


# --------------------------------------------------
# Pressure Index
# --------------------------------------------------

def pressure_index(match):

    if "rrr" not in match:
        return "Unknown"

    try:

        value = float(

            match["rrr"]

            .split()[0]

        )

    except:

        return "Unknown"

    if value >= 12:

        return "Extreme"

    elif value >= 10:

        return "High"

    elif value >= 8:

        return "Medium"

    else:

        return "Low"


# --------------------------------------------------
# Match Summary
# --------------------------------------------------

def match_summary(match):

    return {

        "run_rates":

            calculate_run_rates(match),

        "phase_winners":

            calculate_phase_winners(match),

        "required_rate":

            calculate_required_rate(match),

        "wickets":

            total_wickets(match),

        "collapse":

            collapse_index(match),

        "dominance":

            dominance_score(match),

        "pressure":

            pressure_index(match)

    }


# --------------------------------------------------
# Testing
# --------------------------------------------------

if __name__ == "__main__":

    sample = {

        "powerplay":

            "KKR:61/1,RCB:26/4",

        "middle":

            "KKR:101/1,RCB:41/5",

        "death":

            "KKR:60/1,RCB:28/1",

        "rrr":

            "10.75 rpo"

    }

    from pprint import pprint

    pprint(

        match_summary(sample)

    )