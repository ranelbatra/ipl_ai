"""
Team DNA Feature Extractor
--------------------------
Calculates team-level analytics from player career stats.
"""

import pandas as pd


class TeamDNAFeatureExtractor:

    def __init__(self, player_stats: pd.DataFrame):

        self.df = player_stats.copy()

    # ------------------------------------
    # Batting Aggression
    # ------------------------------------

    def batting_aggression(self):

        if len(self.df) == 0:
            return 0

        score = (
            self.df["strike rate"].mean() * 0.7 +
            self.df["sixes"].mean() * 2 +
            self.df["fours"].mean()
        )

        return min(int(score), 100)

    # ------------------------------------
    # Batting Consistency
    # ------------------------------------

    def batting_consistency(self):

        if len(self.df) == 0:
            return 0

        score = self.df["runs"].mean() / 2

        return min(int(score), 100)

    # ------------------------------------
    # Bowling Strength
    # ------------------------------------

    def bowling_strength(self):

        if len(self.df) == 0:
            return 0

        score = self.df["wickets"].mean() * 4

        return min(int(score), 100)

    # ------------------------------------
    # Pace Attack
    # ------------------------------------

    def pace_attack(self):

        return self.bowling_strength()

    # ------------------------------------
    # Spin Attack
    # ------------------------------------

    def spin_attack(self):

        return int(self.bowling_strength() * 0.75)

    # ------------------------------------
    # Finishing Ability
    # ------------------------------------

    def finishing(self):

        if len(self.df) == 0:
            return 0

        finishers = self.df[
            self.df["strike rate"] >= 150
        ]

        score = len(finishers) * 20

        return min(score, 100)

    # ------------------------------------
    # Fielding
    # ------------------------------------

    def fielding(self):

        return 75

    # ------------------------------------
    # Experience
    # ------------------------------------

    def experience(self):

        if len(self.df) == 0:
            return 0

        score = len(self.df) * 10

        return min(score, 100)

    # ------------------------------------
    # Pipeline
    # ------------------------------------

    def extract_all_features(self):

        return {

            "batting_aggression": self.batting_aggression(),

            "batting_consistency": self.batting_consistency(),

            "bowling_strength": self.bowling_strength(),

            "pace_attack": self.pace_attack(),

            "spin_attack": self.spin_attack(),

            "finishing": self.finishing(),

            "fielding": self.fielding(),

            "experience": self.experience()

        }