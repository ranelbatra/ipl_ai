from data.loader import get_all_matches


def get_matches_by_team(team):
    """
    Return all matches played by a team.
    """
    df = get_all_matches()

    return df[
        (df["team_1"] == team) |
        (df["team_2"] == team)
    ]


def get_matches_by_season(season):
    """
    Return all matches for a season.
    """
    df = get_all_matches()

    return df[
        df["season"] == str(season)
    ]


def get_match(match_id):
    """
    Return a single match using match_id.
    """
    df = get_all_matches()

    match = df[
        df["match_id"] == match_id
    ]

    if match.empty:
        return None

    return match.iloc[0]


def get_all_teams():
    """
    Return all unique teams.
    """
    df = get_all_matches()

    teams = sorted(
        set(df["team_1"]).union(df["team_2"])
    )

    return teams


def get_all_venues():
    """
    Return all unique venues.
    """
    df = get_all_matches()

    return sorted(df["venue"].dropna().unique())