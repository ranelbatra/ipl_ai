"""
Timeline Builder
----------------
Creates a complete over-by-over analytics timeline.
This timeline becomes the single source of truth for:
- Match Aura
- AI Detective
- AI Documentary Generator
"""

import pandas as pd


class TimelineBuilder:

    def __init__(self, deliveries):

        self.df = deliveries.sort_values(
            ["innings", "over", "ball"]
        ).copy()

    # =====================================================
    # Phase Detector
    # =====================================================

    @staticmethod
    def get_phase(over):

        if over <= 6:
            return "Powerplay"

        elif over <= 15:
            return "Middle Overs"

        return "Death Overs"

    # =====================================================
    # Build Timeline
    # =====================================================

    def build(self):

        timeline = []

        grouped = self.df.groupby(
            ["innings", "over"],
            sort=True
        )

        cumulative_runs = {}
        cumulative_wickets = {}

        for (innings, over), data in grouped:

            team = data["team"].iloc[0]

            if innings not in cumulative_runs:

                cumulative_runs[innings] = 0
                cumulative_wickets[innings] = 0

            # -----------------------------------------
            # Over Statistics
            # -----------------------------------------

            runs = int(
                data["runs_total"].sum()
            )

            wickets = int(
                data["wicket"].sum()
            )

            boundaries = int(
                (data["runs_batter"] == 4).sum()
            )

            sixes = int(
                (data["runs_batter"] == 6).sum()
            )

            dot_balls = int(
                (data["runs_total"] == 0).sum()
            )

            extras = int(
                data["runs_extras"].sum()
            )

            balls = len(data)

            # -----------------------------------------
            # Running Totals
            # -----------------------------------------

            cumulative_runs[innings] += runs
            cumulative_wickets[innings] += wickets

            overs_completed = over

            run_rate = round(
                cumulative_runs[innings] / overs_completed,
                2
            )

            # -----------------------------------------
            # Momentum Score
            # -----------------------------------------

            momentum = runs

            momentum += boundaries * 2

            momentum += sixes * 3

            momentum -= wickets * 5

            # -----------------------------------------
            # Flags
            # -----------------------------------------

            explosive = runs >= 18

            pressure = runs <= 3

            wicket_over = wickets > 0

            # -----------------------------------------
            # Timeline Record
            # -----------------------------------------

            timeline.append({

                "innings": innings,

                "team": team,

                "over": over,

                "phase": self.get_phase(over),

                "runs": runs,

                "wickets": wickets,

                "boundaries": boundaries,

                "sixes": sixes,

                "dot_balls": dot_balls,

                "extras": extras,

                "balls": balls,

                "cumulative_runs":
                    cumulative_runs[innings],

                "cumulative_wickets":
                    cumulative_wickets[innings],

                "run_rate": run_rate,

                "momentum": momentum,

                "explosive_over": explosive,

                "pressure_over": pressure,

                "wicket_over": wicket_over

            })

        timeline = pd.DataFrame(timeline)

        # =============================================
        # Momentum Delta
        # =============================================

        timeline["momentum_change"] = (

            timeline
            .groupby("innings")["momentum"]
            .diff()
            .fillna(0)

        )

        # =============================================
        # Required by Drama Engine
        # =============================================

        timeline["big_shift"] = (

            timeline["momentum_change"].abs() >= 10

        )

        return timeline