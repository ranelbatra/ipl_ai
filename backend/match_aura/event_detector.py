"""
Event Detection Engine
----------------------
Detects important cricket events from extracted features.
"""


class EventDetector:

    def __init__(self, features_team1, features_team2):

        self.team1 = features_team1
        self.team2 = features_team2

    # -------------------------------------------------
    # Close Finish
    # -------------------------------------------------

    def close_finish(self):

        margin = abs(
            self.team1["total_runs"] -
            self.team2["total_runs"]
        )

        return margin <= 10

    # -------------------------------------------------
    # High Scoring Match
    # -------------------------------------------------

    def high_scoring_match(self):

        return (
            self.team1["total_runs"] >= 180
            and
            self.team2["total_runs"] >= 180
        )

    # -------------------------------------------------
    # Explosive Match
    # -------------------------------------------------

    def explosive_match(self):

        return (
            self.team1["boundaries"] +
            self.team2["boundaries"]
        ) >= 40

    # -------------------------------------------------
    # Dominating Victory
    # -------------------------------------------------

    def domination(self):

        margin = abs(
            self.team1["total_runs"] -
            self.team2["total_runs"]
        )

        return margin >= 50

    # -------------------------------------------------
    # Collect Events
    # -------------------------------------------------

    def detect_events(self):

        events = []

        if self.close_finish():
            events.append("🔥 Close Finish")

        if self.high_scoring_match():
            events.append("💥 Run Fest")

        if self.explosive_match():
            events.append("🚀 Boundary Storm")

        if self.domination():
            events.append("👑 Statement Win")

        return events