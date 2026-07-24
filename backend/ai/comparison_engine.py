import pandas as pd


# =====================================================
# Match Comparison
# =====================================================

def compare_matches(match1, match2):

    d1 = match1["deliveries"]
    d2 = match2["deliveries"]
    print(match1["deliveries"].columns.tolist())
    return [

        {
            "Match": match1["match"],
            "Winner": match1["winner"],
            "Venue": match1["venue"],
            "Runs": int(d1["runs_total"].sum()),
            "Wickets": d1[
    (d1["player_out"].notna()) &
    (~d1["wicket_type"].isin([
        "run out",
        "retired hurt",
        "obstructing the field"
    ]))
].shape[0],
            "Sixes": int((d1["runs_batter"] == 6).sum()),
            "Fours": int((d1["runs_batter"] == 4).sum())
        },

        {
            "Match": match2["match"],
            "Winner": match2["winner"],
            "Venue": match2["venue"],
            "Runs": int(d2["runs_total"].sum()),
            "Wickets": d2[
    (d2["player_out"].notna()) &
    (~d2["wicket_type"].isin([
        "run out",
        "retired hurt",
        "obstructing the field"
    ]))
].shape[0],
            "Sixes": int((d2["runs_batter"] == 6).sum()),
            "Fours": int((d2["runs_batter"] == 4).sum())
        }

    ]


# =====================================================
# Team Comparison
# =====================================================

# =====================================================
# Team Comparison
# =====================================================

def compare_teams(deliveries, team1, team2):

    def team_stats(team):

        # --------------------
        # Batting
        # --------------------

        batting = deliveries[
            deliveries["team"] == team
        ].copy()

        batting_balls = len(batting)
        batting_overs = batting_balls / 6 if batting_balls else 1

        runs = int(batting["runs_total"].sum())

        wickets_lost = batting["player_out"].notna().sum()

        # --------------------
        # Bowling
        # --------------------

        bowling = deliveries[
            deliveries["bowler"].notna()
        ].copy()

        bowling = bowling[
            bowling["team"] != team
        ]

        bowling_balls = len(bowling)
        bowling_overs = bowling_balls / 6 if bowling_balls else 1

        runs_conceded = int(
            bowling["runs_total"].sum()
        )

        wickets_taken = bowling["player_out"].notna().sum()

        economy = round(
            runs_conceded / bowling_overs,
            2
        ) if bowling_overs else 0

        return {

            "Team": team,

            "Runs": runs,

            "Run Rate": round(
                runs / batting_overs,
                2
            ),

            "Boundaries": int(
                (batting["runs_batter"] == 4).sum()
            ),

            "Sixes": int(
                (batting["runs_batter"] == 6).sum()
            ),

            "Dot Balls": int(
                (batting["runs_total"] == 0).sum()
            ),

            "Wickets": wickets_lost,

            "Runs Conceded": runs_conceded,

            "Wickets Taken": wickets_taken,

            "Economy": economy
        }

    return [
        team_stats(team1),
        team_stats(team2)
    ]


# =====================================================
# Player Comparison
# =====================================================

def compare_players(deliveries, player1, player2):

    def player_stats(player):

        # Bowling statistics
        bowling = deliveries[
    deliveries["bowler"] == player
].copy()

        balls_bowled = len(bowling)

        overs = round(balls_bowled / 6, 1) if balls_bowled else 0

        runs_conceded = int(bowling["runs_total"].sum())

        wickets = bowling[
    (bowling["player_out"].notna()) &
    (~bowling["wicket_type"].isin(["run out", "retired hurt", "obstructing the field"]))
].shape[0]

        economy = round(
    runs_conceded / (balls_bowled / 6),
    2
) if balls_bowled else 0

        df = deliveries[
            deliveries["batter"] == player
        ].copy()

        if df.empty:

            return {

                "Player": player,

                "Runs": 0,

                "Balls": 0,

                "Fours": 0,

                "Sixes": 0,

                "Strike Rate": 0,

                "Dismissals": 0,

                "Average": 0
            }

        runs = int(df["runs_batter"].sum())

        balls = len(df)

        fours = int(
            (df["runs_batter"] == 4).sum()
        )

        sixes = int(
            (df["runs_batter"] == 6).sum()
        )

        dismissals = int(
            df[
                df["player_out"] == player
            ].shape[0]
        )

        strike_rate = round(
            (runs / balls) * 100,
            2
        ) if balls else 0

        average = (
            round(runs / dismissals, 2)
            if dismissals
            else runs
        )

        return {

            "Player": player,

            "Runs": runs,

            "Balls": balls,

            "Fours": fours,

            "Sixes": sixes,

            "Strike Rate": strike_rate,

            "Dismissals": dismissals,

            "Average": average,

            # Bowling
    "Overs": overs,
    "Runs Conceded": runs_conceded,
    "Wickets": wickets,
    "Economy": economy,
        }

    return [
        player_stats(player1),
        player_stats(player2)
    ]