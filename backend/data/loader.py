import pandas as pd
import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "IPL_matches.csv"

_df = pd.read_csv(CSV_PATH)

REQUIRED_COLUMNS = [
    "match_id",
    "date",
    "season",
    "venue",
    "team_1",
    "team_2",
    "winner",
    "player_of_match"
]

missing = [col for col in REQUIRED_COLUMNS if col not in _df.columns]

if missing:
    raise ValueError(f"Missing required columns: {missing}")


# --------------------------------------------------------
# Return complete dataframe
# --------------------------------------------------------

def get_all_matches():
    return _df


def load_data():
    return get_all_matches()


# --------------------------------------------------------
# Return all seasons
# --------------------------------------------------------

def get_all_seasons():

    seasons = sorted(

        _df["season"].dropna().unique()

    )

    return list(seasons)


# --------------------------------------------------------
# Return matches for a season
# --------------------------------------------------------

def get_matches(season):

    temp = _df[

        _df["season"] == season

    ].copy()

    temp["match_name"] = (

        temp["team_1"]

        + " vs "

        + temp["team_2"]

    )

    return temp["match_name"].tolist()


# --------------------------------------------------------
# Return all information of one match
# --------------------------------------------------------

def get_match_details(season, match_name):

    team1, team2 = match_name.split(" vs ")

    row = _df[

        (_df["season"] == season)

        & (_df["team_1"] == team1)

        & (_df["team_2"] == team2)

    ]

    if row.empty:

        return None

    row = row.iloc[0]

    return {

        "match": match_name,

        "date": row["date"],

        "venue": row["venue"],

        "city": row["city"],

        "team1": row["team_1"],

        "team2": row["team_2"],

        "winner": row["winner"],

        "toss": f'{row["toss_winner"]} elected to {row["toss_decision"]}',

        "player_of_match": row["player_of_match"],

        "match_type": row["match_type"]

    }


# --------------------------------------------------------
# Testing
# --------------------------------------------------------

if __name__ == "__main__":

    print(get_all_seasons())

    season = get_all_seasons()[0]

    print(get_matches(season)[0])

    print(

        get_match_details(

            season,

            get_matches(season)[0]

        )

    )