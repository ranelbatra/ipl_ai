"""
Momentum Engine
---------------
Determines which team controlled each phase of the match.
"""


class MomentumEngine:

    def __init__(self, feature_team1, feature_team2):

        self.team1 = feature_team1
        self.team2 = feature_team2

    # -------------------------------------------------
    # Compare one metric
    # -------------------------------------------------

    def compare(self, metric):

        if self.team1[metric] > self.team2[metric]:
            return "Team 1"

        elif self.team2[metric] > self.team1[metric]:
            return "Team 2"

        return "Balanced"

    # -------------------------------------------------
    # Phase Winners
    # -------------------------------------------------

    def phase_winners(self):

        return {

            "powerplay":
                self.compare("powerplay_runs"),

            "middle":

                self.compare("middle_over_runs"),

            "death":

                self.compare("death_over_runs")

        }

    # -------------------------------------------------
    # Momentum Swings
    # -------------------------------------------------

    def momentum_swings(self):

        winners = list(
            self.phase_winners().values()
        )

        swings = 0

        for i in range(1, len(winners)):

            if winners[i] != winners[i - 1]:

                swings += 1

        return swings

    # -------------------------------------------------
    # Dominating Team
    # -------------------------------------------------

    def dominating_team(self):

        winners = self.phase_winners()

        count = {

            "Team 1": 0,

            "Team 2": 0,

            "Balanced": 0

        }

        for winner in winners.values():

            count[winner] += 1

        return max(
            count,
            key=count.get
        )

    # -------------------------------------------------
    # Match Flow
    # -------------------------------------------------

    def match_flow(self):

        return {

            "phase_winners":
                self.phase_winners(),

            "momentum_swings":
                self.momentum_swings(),

            "dominating_team":
                self.dominating_team()

        }