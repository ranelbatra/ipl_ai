"""
Match DNA
---------

Generates a five-dimensional DNA profile describing
the character of an IPL match.

Dimensions
----------
- Aggression
- Pressure
- Control
- Entertainment
- Comeback
"""

from dataclasses import dataclass


@dataclass
class MatchDNA:

    aggression: int
    pressure: int
    control: int
    entertainment: int
    comeback: int


class AuraDNAEngine:

    def __init__(
        self,
        team1_features,
        team2_features,
        momentum,
        battle_meter,
        hype_meter,
    ):

        self.team1 = team1_features
        self.team2 = team2_features
        self.momentum = momentum
        self.battle_meter = battle_meter
        self.hype_meter = hype_meter

    # ---------------------------------------------------
    # Aggression
    # ---------------------------------------------------

    def aggression(self):

        boundaries = (
            self.team1["boundaries"]
            + self.team2["boundaries"]
        )

        sixes = (
            self.team1["sixes"]
            + self.team2["sixes"]
        )

        score = boundaries * 1.5 + sixes * 4

        return min(100, round(score))

    # ---------------------------------------------------
    # Pressure
    # ---------------------------------------------------

    def pressure(self):

        swings = self.momentum["momentum_swings"]

        score = (
            swings * 15
            + self.battle_meter * 0.5
        )

        return min(100, round(score))

    # ---------------------------------------------------
    # Control
    # ---------------------------------------------------

    def control(self):

        winners = self.momentum["phase_winners"]

        counts = {}

        for phase in winners.values():

            counts[phase] = counts.get(phase, 0) + 1

        dominant = max(counts.values())

        score = dominant * 33

        return min(100, score)

    # ---------------------------------------------------
    # Entertainment
    # ---------------------------------------------------

    def entertainment(self):

        score = (
            self.hype_meter * 0.6
            + self.battle_meter * 0.4
        )

        return min(100, round(score))

    # ---------------------------------------------------
    # Comeback
    # ---------------------------------------------------

    def comeback(self):

        swings = self.momentum["momentum_swings"]

        score = swings * 20

        return min(100, round(score))

    # ---------------------------------------------------
    # Generate DNA
    # ---------------------------------------------------

    def generate(self):

        return MatchDNA(

            aggression=self.aggression(),

            pressure=self.pressure(),

            control=self.control(),

            entertainment=self.entertainment(),

            comeback=self.comeback(),

        )