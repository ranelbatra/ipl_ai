"""
Match Aura Engine
-----------------
Master pipeline for generating Match Aura.
"""

from match_aura.feature_extractor import MatchFeatureExtractor
from match_aura.momentum import MomentumEngine
from match_aura.event_detector import EventDetector

from match_aura.metrics import (
    calculate_battle_meter,
    calculate_hype_meter,
    calculate_aura_score,
)

from match_aura.personality import determine_personality
from match_aura.achievements import generate_achievements
from match_aura.signature import determine_signature_moment

from match_aura.models import MatchAura


class MatchAuraEngine:

    def __init__(self, deliveries_df):

        self.df = deliveries_df

    # -------------------------------------------------
    # Generate Match Aura
    # -------------------------------------------------

    def generate(self):

        # -----------------------------------------
        # Split innings
        # -----------------------------------------

        innings1 = self.df[
            self.df["innings"] == 1
        ]

        innings2 = self.df[
            self.df["innings"] == 2
        ]

        # -----------------------------------------
        # Feature Extraction
        # -----------------------------------------

        team1 = MatchFeatureExtractor(
            innings1
        ).extract_all_features()

        team2 = MatchFeatureExtractor(
            innings2
        ).extract_all_features()

        # -----------------------------------------
        # Momentum
        # -----------------------------------------

        momentum = MomentumEngine(
            team1,
            team2
        ).match_flow()

        # -----------------------------------------
        # Events
        # -----------------------------------------

        events = EventDetector(
            team1,
            team2
        ).detect_events()

        # -----------------------------------------
        # Metrics
        # -----------------------------------------

        battle_meter = calculate_battle_meter(
            abs(
                team1["total_runs"] -
                team2["total_runs"]
            ),
            "runs"
        )

        hype_meter = calculate_hype_meter(
            team1["boundaries"] +
            team2["boundaries"],
            team1["sixes"] +
            team2["sixes"]
        )

        aura_score = calculate_aura_score(
            battle_meter,
            hype_meter
        )

        # -----------------------------------------
        # Personality
        # -----------------------------------------

        personality = determine_personality(
            aura_score,
            battle_meter,
            hype_meter,
            momentum["momentum_swings"]
        )

        # -----------------------------------------
        # Achievements
        # -----------------------------------------

        achievements = generate_achievements(
            total_boundaries=team1["boundaries"] + team2["boundaries"],
            total_sixes=team1["sixes"] + team2["sixes"],
            win_margin=abs(team1["total_runs"] - team2["total_runs"]),
            margin_type="runs",
            plot_twist_count=momentum["momentum_swings"]
        )

        # -----------------------------------------
        # Signature Moment
        # -----------------------------------------

        signature = determine_signature_moment(
            momentum["phase_winners"]["powerplay"],
            momentum["phase_winners"]["middle"],
            momentum["phase_winners"]["death"],
            abs(team1["total_runs"] - team2["total_runs"]),
            "runs",
            momentum["momentum_swings"]
        )

        # -----------------------------------------
        # Return Match Aura
        # -----------------------------------------

        return MatchAura(

            aura_score=aura_score,

            personality=personality,

            battle_meter=battle_meter,

            hype_meter=hype_meter,

            momentum_timeline=momentum,

            plot_twists=events,

            achievements=achievements,

            signature_moment=signature,

            ai_verdict="Coming in Sprint 2",

            ending = (
    f"This match had an Aura Score of {aura_score}/100 and was classified as a "
    f"'{personality}' encounter."
)

        )