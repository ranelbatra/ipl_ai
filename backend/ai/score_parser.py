import re


def parse_score(score: str):
    """
    Converts a score string into structured data.

    Supports:

    KKR:61/1
    KKR:101/1 (Overs 6-15)
    RCB:All Out
    N/A
    """

    if score is None:
        return None

    score = score.strip()

    if score.upper() == "N/A":
        return None

    if ":" not in score:
        return None

    team, value = score.split(":", 1)

    team = team.strip()
    value = value.strip()

    # Remove anything inside brackets
    value = re.sub(r"\(.*?\)", "", value).strip()

    if value.lower() == "all out":
        return {
            "team": team,
            "runs": 0,
            "wickets": 10,
            "all_out": True
        }

    match = re.search(r"(\d+)\s*/\s*(\d+)", value)

    if not match:
        return {
            "team": team,
            "runs": 0,
            "wickets": 0,
            "all_out": False
        }

    runs = int(match.group(1))
    wickets = int(match.group(2))

    return {
        "team": team,
        "runs": runs,
        "wickets": wickets,
        "all_out": wickets == 10
    }


def parse_phase(phase: str):
    """
    Parses an entire phase.

    Example:

    KKR:61/1, RCB:26/4

    Returns

    {
        "KKR": {...},
        "RCB": {...}
    }
    """

    if phase is None:
        return {}

    phase = phase.strip()

    if phase.upper() == "N/A":
        return {}

    scores = phase.split(",")

    result = {}

    for score in scores:

        parsed = parse_score(score)

        if parsed is not None:
            result[parsed["team"]] = parsed

    return result


def get_team_score(phase: str, team: str):
    """
    Returns only one team's score from a phase.
    """

    parsed = parse_phase(phase)

    return parsed.get(team)


def get_runs(phase: str, team: str):

    score = get_team_score(phase, team)

    if score is None:
        return 0

    return score["runs"]


def get_wickets(phase: str, team: str):

    score = get_team_score(phase, team)

    if score is None:
        return 0

    return score["wickets"]


def compare_phase(phase: str):
    """
    Determines which team won a phase.

    Returns

    {
        winner,
        margin,
        team1,
        team2
    }
    """

    parsed = parse_phase(phase)

    if len(parsed) != 2:
        return None

    teams = list(parsed.keys())

    t1 = teams[0]
    t2 = teams[1]

    r1 = parsed[t1]["runs"]
    r2 = parsed[t2]["runs"]

    if r1 > r2:
        winner = t1
        margin = r1 - r2

    elif r2 > r1:
        winner = t2
        margin = r2 - r1

    else:
        winner = "Tie"
        margin = 0

    return {
        "winner": winner,
        "margin": margin,
        "team1": parsed[t1],
        "team2": parsed[t2]
    }


# --------------------------------------------------------
# TESTING
# --------------------------------------------------------

if __name__ == "__main__":

    phase = "KKR:61/1, RCB:26/4"

    print(parse_phase(phase))

    print(compare_phase(phase))

    print(get_runs(phase, "KKR"))

    print(get_wickets(phase, "RCB"))