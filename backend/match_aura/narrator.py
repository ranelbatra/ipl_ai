"""
Match Narrator
--------------
Generates a human-readable story from the analytics.
"""


class MatchNarrator:

    def __init__(
        self,
        match_details,
        timeline,
        momentum,
        drama,
        events
    ):

        self.match = match_details
        self.timeline = timeline
        self.momentum = momentum
        self.drama = drama
        self.events = events

    # -----------------------------------------------------
    # Opening
    # -----------------------------------------------------

    def opening(self):

        return (
            f"{self.match['team1']} faced "
            f"{self.match['team2']} at "
            f"{self.match['venue']}."
        )

    # -----------------------------------------------------
    # Momentum Summary
    # -----------------------------------------------------

    def momentum_summary(self):

        swings = self.momentum["momentum_swings"]

        if swings == 0:

            return (
                "One team remained in control "
                "throughout the match."
            )

        elif swings <= 2:

            return (
                "The momentum shifted a few times "
                "before one team gained control."
            )

        else:

            return (
                "The match witnessed multiple momentum "
                "swings and remained unpredictable."
            )

    # -----------------------------------------------------
    # Drama Summary
    # -----------------------------------------------------

    def drama_summary(self):

        score = self.drama["drama_score"]

        if score >= 90:

            return (
                "It turned into an absolute thriller."
            )

        elif score >= 70:

            return (
                "The match remained highly entertaining."
            )

        elif score >= 50:

            return (
                "Both teams exchanged momentum regularly."
            )

        return (
            "The contest remained fairly one-sided."
        )

    # -----------------------------------------------------
    # Key Events
    # -----------------------------------------------------

    def key_events(self):

        if len(self.events) == 0:

            return (
                "No major turning points were detected."
            )

        sentences = []

        for event in self.events[:5]:

            sentences.append(
                event["description"]
            )

        return " ".join(sentences)

    # -----------------------------------------------------
    # Ending
    # -----------------------------------------------------

    def ending(self):

        return (
            f"{self.match['winner']} eventually "
            "emerged victorious after a fascinating contest."
        )

    # -----------------------------------------------------
    # Full Narrative
    # -----------------------------------------------------

    def generate(self):

        return " ".join([

            self.opening(),

            self.momentum_summary(),

            self.drama_summary(),

            self.key_events(),

            self.ending()

        ])