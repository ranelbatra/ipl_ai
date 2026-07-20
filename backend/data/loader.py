import pandas as pd
from pathlib import Path

# ========================================================
# Paths
# ========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

EXCEL_PATH = BASE_DIR / "IPL_Data.xlsx"

# ========================================================
# Load all sheets once
# ========================================================

_matches = pd.read_excel(EXCEL_PATH, sheet_name="Matches")
_matches.columns = _matches.columns.str.strip()

print("Columns:")
print(_matches.columns.tolist())
_innings = pd.read_excel(EXCEL_PATH, sheet_name="Innings")
_deliveries = pd.read_excel(EXCEL_PATH, sheet_name="Deliveries")
_player_match_stats = pd.read_excel(EXCEL_PATH, sheet_name="Player_Match_Stats")
_player_career_stats = pd.read_excel(EXCEL_PATH, sheet_name="Player_Career_Stats")
_team_match_stats = pd.read_excel(EXCEL_PATH, sheet_name="Team_Match_Stats")
_team_dna = pd.read_excel(EXCEL_PATH, sheet_name="Team_DNA")
_match_aura = pd.read_excel(EXCEL_PATH, sheet_name="Match_Aura")

# ========================================================
# Validation
# ========================================================

REQUIRED_COLUMNS = [
    "match_id",
    "date",
    "season",
    "venue",
    "team1",
    "team2",
    "winner",
    "player_of_match"
]

missing = [col for col in REQUIRED_COLUMNS if col not in _matches.columns]

if missing:
    raise ValueError(f"Missing required columns in matches sheet: {missing}")

# ========================================================
# Existing Functions (kept for compatibility)
# ========================================================

def get_all_matches():
    return _matches.copy()


def load_data():
    return get_all_matches()


def get_all_seasons():
    seasons = (
        _matches["season"]
        .dropna()
        .astype(str)
        .unique()
    )

    return sorted(list(seasons))


def get_matches(season):

    temp = _matches[
        _matches["season"] == season
    ].copy()

    temp["match_name"] = (
        temp["team1"] +
        " vs " +
        temp["team2"]
    )

    return temp["match_name"].tolist()


def get_match_details(season, match_name):

    team1, team2 = match_name.split(" vs ")

    row = _matches[
        (_matches["season"] == season)
        &
        (_matches["team1"] == team1)
        &
        (_matches["team2"] == team2)
    ]

    if row.empty:
        return None

    row = row.iloc[0]

    return {

    "match_id": row["match_id"],

    "match": match_name,

    "date": row["date"],

    "season": row["season"],

    "venue": row["venue"],

    "city": row.get("city", None),

    "team1": row["team1"],

    "team2": row["team2"],

    "winner": row["winner"],

    "player_of_match": row["player_of_match"],

    "toss_winner": row.get("toss_winner", None),

    "toss_decision": row.get("toss_decision", None),

    "result": row.get("result", None),

    "match_type": row.get("match_type", None),

    "toss": (
    f"{row.get('toss_winner', 'Unknown')} "
    f"elected to "
    f"{row.get('toss_decision', 'Unknown')}"
)

}

# ========================================================
# New Match Aura Functions
# ========================================================

def get_match_deliveries(match_id):

    return _deliveries[
        _deliveries["match_id"] == match_id
    ].copy()


def get_match_innings(match_id):

    return _innings[
        _innings["match_id"] == match_id
    ].copy()


def get_team_match_stats(match_id):

    return _team_match_stats[
        _team_match_stats["match_id"] == match_id
    ].copy()


def get_player_match_stats(match_id):

    return _player_match_stats[
        _player_match_stats["match_id"] == match_id
    ].copy()


def get_player_career(player_name):

    return _player_career_stats[
        _player_career_stats["player"] == player_name
    ].copy()


def get_team_dna(team_name):

    row = _team_dna[
        _team_dna["team"] == team_name
    ]

    if row.empty:
        return None

    return row.iloc[0]


def get_match_aura(match_id):

    row = _match_aura[
        _match_aura["match_id"] == match_id
    ]

    if row.empty:
        return None

    return row.iloc[0]
def get_team_players(team_name):

    return _player_career_stats[
        _player_career_stats["team"] == team_name
    ].copy()

from team_dna.team_rosters import TEAM_ROSTERS


def get_team_players(team_name):

    players = TEAM_ROSTERS.get(team_name, [])

    return _player_career_stats[
        _player_career_stats["player"].isin(players)
    ].copy()

# ========================================================
# Testing
# ========================================================

if __name__ == "__main__":

    print("Loaded Successfully")

    print("Matches:", len(_matches))
    print("Deliveries:", len(_deliveries))
    print("Innings:", len(_innings))

    print(get_all_seasons()[:5])

from data.loader import get_team_players

df = get_team_players("Mumbai Indians")

print(df[["player", "runs", "wickets"]])