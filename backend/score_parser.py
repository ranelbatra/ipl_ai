import re


def parse_score(score):
    """
    Converts a score like:

    44/2

    into

    {
        "runs":44,
        "wickets":2
    }
    """

    score = score.strip()

    pattern = r"(\d+)\s*/\s*(\d+)"

    match = re.match(pattern, score)

    if not match:
        raise ValueError(
            f"Invalid score format: {score}. Expected format: Runs/Wickets"
        )

    runs = int(match.group(1))
    wickets = int(match.group(2))

    return {
        "runs": runs,
        "wickets": wickets
    }


def parse_phase(phase_text):
    """
    Converts

    RCB: 44/2, PBKS: 62/0

    into

    {
        "RCB":{
            "runs":44,
            "wickets":2
        },
        "PBKS":{
            "runs":62,
            "wickets":0
        }
    }
    """

    phase = {}

    teams = phase_text.split(",")

    for item in teams:

        if ":" not in item:
            continue

        team, score = item.split(":")

        phase[team.strip()] = parse_score(score)

    return phase


def get_team_score(phase_data, team):
    """
    Returns the score of a particular team.

    Example

    get_team_score(data,"RCB")

    Returns

    {
        "runs":44,
        "wickets":2
    }
    """

    return phase_data.get(team, {
        "runs": 0,
        "wickets": 0
    })


if __name__ == "__main__":

    sample = "RCB: 44/2, PBKS: 62/0"

    parsed = parse_phase(sample)

    print(parsed)