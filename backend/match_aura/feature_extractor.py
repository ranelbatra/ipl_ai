"""
Feature Extraction Engine
-------------------------
Extracts cricket analytics from ball-by-ball deliveries.
"""

import pandas as pd


class MatchFeatureExtractor:

    def __init__(self, deliveries_df: pd.DataFrame):
        self.df = deliveries_df.copy()

    # =====================================================
    # BASIC MATCH FEATURES
    # =====================================================

    def total_runs(self):
        return int(self.df["runs_total"].sum())

    def total_boundaries(self):
        return int((self.df["runs_batter"] == 4).sum())

    def total_sixes(self):
        return int((self.df["runs_batter"] == 6).sum())

    def total_wickets(self):
        return int(self.df["wicket"].sum())

    def dot_balls(self):
        return int((self.df["runs_total"] == 0).sum())
    
# =====================================================
# PHASE RUNS
# =====================================================

    def powerplay_runs(self):

        phase = self.df[
            self.df["over"] <= 6
        ]

        return int(phase["runs_total"].sum())


    def middle_over_runs(self):

        return int(
            self.df[
                (self.df["over"] >= 7)
                &
                (self.df["over"] <= 15)
            ]["runs_total"].sum()
        )


    def death_over_runs(self):

        return int(
            self.df[
                self.df["over"] >= 16
            ]["runs_total"].sum()
        )
    
    # =====================================================
# PHASE WICKETS
# =====================================================

    def powerplay_wickets(self):

        return int(
            self.df[
                self.df["over"] <= 6
            ]["wicket"].sum()
        )


    def middle_over_wickets(self):

        return int(
            self.df[
                (self.df["over"] >= 7)
                &
                (self.df["over"] <= 15)
            ]["wicket"].sum()
        )


    def death_over_wickets(self):

        return int(
            self.df[
                self.df["over"] >= 16
            ]["wicket"].sum()
        )
    
    # =====================================================
# HIGHEST SCORING OVER
# =====================================================

    def highest_scoring_over(self):
        """
    Returns the over that produced the most runs.
    """

        over_runs = (
            self.df
            .groupby(["innings", "over"])["runs_total"]
            .sum()
        )

        highest_over = over_runs.idxmax()
        highest_runs = int(over_runs.max())

        return {
            "innings": int(highest_over[0]),
            "over": int(highest_over[1]),
            "runs": highest_runs
}
    def highest_scoring_over(self):

        over_runs = (
        self.df
        .groupby(["innings", "over"], as_index=False)["runs_total"]
        .sum()
    )

        highest = over_runs.loc[over_runs["runs_total"].idxmax()]

        return {
        "innings": int(highest["innings"]),
        "over": int(highest["over"]),
        "runs": int(highest["runs_total"])
    }
    
    # =====================================================
# MOST EXPENSIVE OVER
# =====================================================

    def most_expensive_over(self):

        over_runs = (
        self.df
        .groupby(["innings", "over"], as_index=False)["runs_total"]
        .sum()
    )

        highest = over_runs.loc[over_runs["runs_total"].idxmax()]

        return {
        "innings": int(highest["innings"]),
        "over": int(highest["over"]),
        "runs": int(highest["runs_total"])
    }
    
    # =====================================================
# RUN RATE
# =====================================================

    def run_rate(self):

        total_runs = self.total_runs()

        balls = len(self.df)

        overs = balls / 6

        if overs == 0:
            return 0

        return round(total_runs / overs, 2)
    
# =====================================================
# DOT BALL %
# =====================================================

    def dot_ball_percentage(self):

        total_balls = len(self.df)

        if total_balls == 0:
            return 0

        return round(
            (self.dot_balls() / total_balls) * 100,
            2
        )
    
# =====================================================
# COLLAPSE DETECTOR
# =====================================================

    def detect_collapse(self):
        """
    Detects batting collapses.

    Rule:
    4 wickets within 30 runs.
    """

        wickets = self.df[
            self.df["wicket"] == 1
        ]

        if len(wickets) < 4:
            return {
                "collapse": False
            }

        wicket_runs = []

        total = 0

        for _, row in self.df.iterrows():

            total += row["runs_total"]

            if row["wicket"] == 1:
                wicket_runs.append(total)

        for i in range(len(wicket_runs) - 3):

            if wicket_runs[i + 3] - wicket_runs[i] <= 30:

                return {
                    "collapse": True,
                    "runs": wicket_runs[i + 3] - wicket_runs[i]
                }

        return {
            "collapse": False
        }
    
    # =====================================================
# EXPLOSIVE OVER
# =====================================================

    def explosive_over(self):

        over = self.highest_scoring_over()

        if over["runs"] >= 25:

            return {

                "explosive": True,

                "over": over["over"],

                "runs": over["runs"]

            }

        return {

            "explosive": False

        }
    
# =====================================================
# FEATURE PIPELINE
# =====================================================

    def extract_all_features(self):
        """
    Returns every feature required by the Match Aura Engine.
    """

        return {

        # -------------------------
        # Match
        # -------------------------

            "total_runs": self.total_runs(),
            "total_wickets": self.total_wickets(),

        # -------------------------
        # Batting
        # -------------------------

            "boundaries": self.total_boundaries(),
            "sixes": self.total_sixes(),
            "dot_balls": self.dot_balls(),
            "dot_ball_percentage": self.dot_ball_percentage(),

        # -------------------------
        # Run Rate
        # -------------------------

            "run_rate": self.run_rate(),

        # -------------------------
        # Match Phases
        # -------------------------

            # -------------------------
# Match Phases
# -------------------------

"powerplay_runs": self.powerplay_runs(),
"middle_over_runs": self.middle_over_runs(),
"death_over_runs": self.death_over_runs(),

"powerplay_wickets": self.powerplay_wickets(),
"middle_over_wickets": self.middle_over_wickets(),
"death_over_wickets": self.death_over_wickets(),

"phase_stats": {

    "powerplay": {

        "runs": self.powerplay_runs(),

        "wickets": self.powerplay_wickets()

    },

    "middle": {

        "runs": self.middle_over_runs(),

        "wickets": self.middle_over_wickets()

    },

    "death": {

        "runs": self.death_over_runs(),

        "wickets": self.death_over_wickets()

    }

},

        # -------------------------
        # Highlights
        # -------------------------

            "highest_scoring_over": self.highest_scoring_over(),
            "most_expensive_over": self.most_expensive_over()

        }