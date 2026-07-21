"""
Aura Tags
---------

Generates descriptive tags for a match based on
its DNA profile, momentum, personality and match metrics.
"""


class AuraTagEngine:

    def __init__(

        self,

        dna,

        personality,

        battle_meter,

        hype_meter,

        momentum,

        team1,

        team2,

    ):

        self.dna = dna
        self.personality = personality
        self.battle_meter = battle_meter
        self.hype_meter = hype_meter
        self.momentum = momentum
        self.team1 = team1
        self.team2 = team2

    # ---------------------------------------------------
    # Generate Tags
    # ---------------------------------------------------

    def generate(self):

        tags = []

        # ==========================================
        # Match Intensity
        # ==========================================

        if self.battle_meter >= 90:
            tags.append("⚔ Nail-Biting Finish")

        elif self.battle_meter >= 75:
            tags.append("🔥 High Voltage")

        elif self.battle_meter >= 50:
            tags.append("⚡ Competitive Battle")

        else:
            tags.append("😎 One-Sided Contest")

        # ==========================================
        # Entertainment
        # ==========================================

        if self.dna.entertainment >= 90:
            tags.append("🎆 Crowd Favourite")

        elif self.dna.entertainment >= 75:
            tags.append("💥 Boundary Storm")

        # ==========================================
        # Aggression
        # ==========================================

        if self.dna.aggression >= 90:
            tags.append("🚀 Explosive Batting")

        elif self.dna.aggression >= 75:
            tags.append("🔥 Aggressive Cricket")

        # ==========================================
        # Momentum
        # ==========================================

        swings = self.momentum["momentum_swings"]

        if swings >= 5:
            tags.append("🎭 Momentum Rollercoaster")

        elif swings >= 3:
            tags.append("🔄 Momentum Swings")

        # ==========================================
        # Phase Dominance
        # ==========================================

        winners = self.momentum["phase_winners"]

        dominant = max(
            set(winners.values()),
            key=list(winners.values()).count
        )

        if list(winners.values()).count(dominant) == 3:
            tags.append("👑 Complete Dominance")

        elif list(winners.values()).count(dominant) == 2:
            tags.append("🎯 Phase Control")

        # ==========================================
        # Personality
        # ==========================================

        personality_tags = {

            "Fearless Chase": "🏃 Chase Masterclass",

            "Bowling Masterclass": "🎯 Bowling Clinic",

            "High-Scoring Thriller": "💥 Run Fest",

            "Last-Over Thriller": "⏱ Last Over Drama",

            "One-Sided Domination": "👑 Complete Control",

            "Balanced Contest": "⚖ Even Contest",

        }

        if self.personality in personality_tags:
            tags.append(
                personality_tags[self.personality]
            )

        # ==========================================
        # Pressure
        # ==========================================

        if self.dna.pressure >= 85:
            tags.append("🧠 High Pressure")

        # ==========================================
        # Comeback
        # ==========================================

        if self.dna.comeback >= 80:
            tags.append("📈 Incredible Comeback")

        elif self.dna.comeback >= 60:
            tags.append("🔁 Momentum Recovery")

        # ==========================================
        # Control
        # ==========================================

        if self.dna.control >= 90:
            tags.append("🛡 Clinical Execution")

        elif self.dna.control >= 75:
            tags.append("🎯 Tactical Discipline")

        # Remove duplicates while preserving order
        unique_tags = []

        for tag in tags:

            if tag not in unique_tags:
                unique_tags.append(tag)

        return unique_tags