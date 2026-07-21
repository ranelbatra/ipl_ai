"""
Momentum Engine
---------------
Calculates match momentum using the over-by-over timeline.
"""

import pandas as pd


class MomentumEngine:

    def __init__(self, timeline_df: pd.DataFrame):

        self.timeline = timeline_df.copy()

    # =====================================================
    # Phase Winners
    # =====================================================

    def phase_winners(self):

        winners = {}

        phase_mapping = {
        "Powerplay": "powerplay",
        "Middle Overs": "middle",
        "Death Overs": "death"
    }

        for phase, key in phase_mapping.items():

            phase_df = self.timeline[
            self.timeline["phase"] == phase
        ]

            if phase_df.empty:
                winners[key] = "Balanced"
                continue

            team_scores = (
            phase_df
            .groupby("team")["momentum"]
            .sum()
        )

            if len(team_scores) == 1:
                winners[key] = team_scores.index[0]
                continue

            if team_scores.iloc[0] > team_scores.iloc[1]:
                winners[key] = team_scores.index[0]

            elif team_scores.iloc[1] > team_scores.iloc[0]:
                winners[key] = team_scores.index[1]

            else:
                winners[key] = "Balanced"

        return winners

    # =====================================================
    # Calculate Momentum
    # =====================================================

    def calculate(self):

        timeline = self.timeline.copy()

        running = {}

        momentum = []

        turning_points = []

        previous_difference = None

        previous_leader = None

        momentum_swings = 0

        # -------------------------------------------------
        # Running Momentum
        # -------------------------------------------------

        for _, row in timeline.iterrows():

            team = row["team"]

            if team not in running:

                running[team] = 0

            running[team] += row["momentum"]

            momentum.append(running[team])

        timeline["running_momentum"] = momentum

        # -------------------------------------------------
        # Compare Teams
        # -------------------------------------------------

        teams = list(

            timeline["team"].unique()

        )

        if len(teams) != 2:

            return {

                "timeline": timeline,

                "phase_winners": {},

                "momentum_swings": 0,

                "turning_points": [],

                "dominating_team": "Unknown"

            }

        team1 = teams[0]

        team2 = teams[1]

        running1 = 0

        running2 = 0

        records = []

        for _, row in timeline.iterrows():

            if row["team"] == team1:

                running1 = row["running_momentum"]

            else:

                running2 = row["running_momentum"]

            difference = running1 - running2

            if difference > 0:

                leader = team1

            elif difference < 0:

                leader = team2

            else:

                leader = "Balanced"

            # -----------------------------------------
            # Momentum Swing
            # -----------------------------------------

            if previous_leader is not None:

                if (

                    leader != previous_leader

                    and

                    leader != "Balanced"

                ):

                    momentum_swings += 1

                    turning_points.append({

                        "innings": row["innings"],

                        "over": row["over"],

                        "team": leader,

                        "reason": "Momentum Shift"

                    })

            # -----------------------------------------
            # Big Momentum Shift
            # -----------------------------------------

            if previous_difference is not None:

                if abs(

                    difference - previous_difference

                ) >= 15:

                    turning_points.append({

                        "innings": row["innings"],

                        "over": row["over"],

                        "team": row["team"],

                        "reason": "Massive Momentum Swing"

                    })

            previous_difference = difference

            previous_leader = leader

            records.append({

                "innings": row["innings"],

                "team": row["team"],

                "over": row["over"],

                "runs": row["runs"],

                "momentum": row["momentum"],

                "running_momentum": row["running_momentum"],

                "leader": leader

            })

        records = pd.DataFrame(records)

        # -------------------------------------------------
        # Dominating Team
        # -------------------------------------------------

        final_difference = running1 - running2

        if final_difference > 0:

            dominating = team1

        elif final_difference < 0:

            dominating = team2

        else:

            dominating = "Balanced"

        return {

            "timeline": records,

            "phase_winners": self.phase_winners(),

            "momentum_swings": momentum_swings,

            "turning_points": turning_points,

            "dominating_team": dominating

        }