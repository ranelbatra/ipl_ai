"""
Event Detection Engine
----------------------
Detects important cricket events using the over-by-over timeline.
"""

import pandas as pd


class EventDetector:

    def __init__(self, timeline_df: pd.DataFrame):

        self.timeline = timeline_df.copy()

    # =====================================================
    # Detect Events
    # =====================================================

    def detect(self):

        events = []

        # -------------------------------------------------
        # Explosive Overs
        # -------------------------------------------------

        explosive = self.timeline[
            self.timeline["explosive_over"]
        ]

        for _, row in explosive.iterrows():

            events.append({

                "type": "🚀 Explosive Over",

                "severity": "High",

                "innings": row["innings"],

                "over": row["over"],

                "description":
                    f"{row['team']} smashed {row['runs']} runs in Over {row['over']}."

            })

        # -------------------------------------------------
        # Pressure Overs
        # -------------------------------------------------

        pressure = self.timeline[
            self.timeline["pressure_over"]
        ]

        for _, row in pressure.iterrows():

            events.append({

                "type": "🛡 Pressure Over",

                "severity": "Medium",

                "innings": row["innings"],

                "over": row["over"],

                "description":
                    f"{row['team']} scored only {row['runs']} runs in Over {row['over']}."

            })

        # -------------------------------------------------
        # Wicket Overs
        # -------------------------------------------------

        wickets = self.timeline[
            self.timeline["wicket_over"]
        ]

        for _, row in wickets.iterrows():

            events.append({

                "type": "🎯 Breakthrough",

                "severity": "High",

                "innings": row["innings"],

                "over": row["over"],

                "description":
                    f"{row['team']} lost {row['wickets']} wicket(s) in Over {row['over']}."

            })

        # -------------------------------------------------
        # Big Momentum Swings
        # -------------------------------------------------

        shifts = self.timeline[
            self.timeline["big_shift"]
        ]

        for _, row in shifts.iterrows():

            events.append({

                "type": "⚡ Momentum Shift",

                "severity": "High",

                "innings": row["innings"],

                "over": row["over"],

                "description":
                    f"Momentum changed significantly during Over {row['over']}."

            })

        # -------------------------------------------------
        # Death Overs Assault
        # -------------------------------------------------

        death = self.timeline[

            self.timeline["phase"] == "Death Overs"

        ]

        if not death.empty:

            avg = death["runs"].mean()

            if avg >= 12:

                team = (

                    death

                    .groupby("team")["runs"]

                    .sum()

                    .idxmax()

                )

                events.append({

                    "type": "💥 Death Overs Assault",

                    "severity": "High",

                    "description":
                        f"{team} dominated the death overs."

                })

        # -------------------------------------------------
        # Powerplay Domination
        # -------------------------------------------------

        powerplay = self.timeline[

            self.timeline["phase"] == "Powerplay"

        ]

        if not powerplay.empty:

            pp = (

                powerplay

                .groupby("team")["momentum"]

                .sum()

            )

            if len(pp) == 2:

                winner = pp.idxmax()

                events.append({

                    "type": "⚡ Powerplay Domination",

                    "severity": "Medium",

                    "description":
                        f"{winner} controlled the Powerplay."

                })

        # -------------------------------------------------
        # Batting Collapse
        # -------------------------------------------------

        collapse = self.timeline[

            (self.timeline["wickets"] >= 2)

            &

            (self.timeline["runs"] <= 5)

        ]

        for _, row in collapse.iterrows():

            events.append({

                "type": "🧨 Batting Collapse",

                "severity": "High",

                "description":
                    f"{row['team']} suffered a collapse in Over {row['over']}."

            })

        # -------------------------------------------------
        # Boundary Carnage
        # -------------------------------------------------

        carnage = self.timeline[

            self.timeline["boundaries"] >= 4

        ]

        for _, row in carnage.iterrows():

            events.append({

                "type": "🔥 Boundary Barrage",

                "severity": "Medium",

                "description":
                    f"{row['team']} hit {row['boundaries']} boundaries in Over {row['over']}."

            })

        # -------------------------------------------------
        # Sort Events
        # -------------------------------------------------

        severity_order = {

            "High": 3,

            "Medium": 2,

            "Low": 1

        }

        events = sorted(

            events,

            key=lambda x: severity_order[x["severity"]],

            reverse=True

        )

        return events