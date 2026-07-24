"""
Match Aura Engine
-----------------
Master pipeline for generating Match Aura.
"""

from match_aura.feature_extractor import MatchFeatureExtractor
from match_aura.timeline import TimelineBuilder
from match_aura.momentum import MomentumEngine
from match_aura.drama import DramaEngine
from match_aura.event_detector import EventDetector
from match_aura.narrator import MatchNarrator

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

        self.df = deliveries_df.copy()

    # =====================================================
    # Generate Match Aura
    # =====================================================

    def generate(self):

        # -------------------------------------------------
        # Split Innings
        # -------------------------------------------------

        innings1 = self.df[
            self.df["innings"] == 1
        ].copy()

        innings2 = self.df[
            self.df["innings"] == 2
        ].copy()

        if innings1.empty or innings2.empty:

            raise ValueError(
                "Match must contain two innings."
            )

        # -------------------------------------------------
        # Team Names
        # -------------------------------------------------

        team1_name = innings1.iloc[0]["team"]
        team2_name = innings2.iloc[0]["team"]

        # -------------------------------------------------
        # Feature Extraction
        # -------------------------------------------------

        team1 = MatchFeatureExtractor(
            innings1
        ).extract_all_features()

        team2 = MatchFeatureExtractor(
            innings2
        ).extract_all_features()

        # -------------------------------------------------
# Phase Statistics
# -------------------------------------------------

                # -------------------------------------------------
        # Phase Statistics
        # -------------------------------------------------

        phase_stats = {

            "powerplay": {

                "team1": {
                    "runs": team1["powerplay_runs"],
                    "wickets": team1["powerplay_wickets"]
                },

                "team2": {
                    "runs": team2["powerplay_runs"],
                    "wickets": team2["powerplay_wickets"]
                }

            },

            "middle": {

                "team1": {
                    "runs": team1["middle_over_runs"],
                    "wickets": team1["middle_over_wickets"]
                },

                "team2": {
                    "runs": team2["middle_over_runs"],
                    "wickets": team2["middle_over_wickets"]
                }

            },

            "death": {

                "team1": {
                    "runs": team1["death_over_runs"],
                    "wickets": team1["death_over_wickets"]
                },

                "team2": {
                    "runs": team2["death_over_runs"],
                    "wickets": team2["death_over_wickets"]
                }

            }

        }

        # -------------------------------------------------
        # Timeline
        # -------------------------------------------------

        timeline = TimelineBuilder(
            self.df
        ).build()

        # -------------------------------------------------
        # Momentum
        # -------------------------------------------------

        momentum = MomentumEngine(
            timeline
        ).calculate()

        # -------------------------------------------------
        # Drama
        # -------------------------------------------------

        drama = DramaEngine(
            timeline
        ).calculate()

        # -------------------------------------------------
        # Events
        # -------------------------------------------------

        events = EventDetector(
            timeline
        ).detect()

        # -------------------------------------------------
        # Winner
        # -------------------------------------------------

        if team1["total_runs"] > team2["total_runs"]:

            winner = team1_name

        elif team2["total_runs"] > team1["total_runs"]:

            winner = team2_name

        else:

            winner = "Tie"

        # -------------------------------------------------
        # Match Details
        # -------------------------------------------------

        match_details = {

            "team1": team1_name,

            "team2": team2_name,

            "winner": winner,

            "venue": "Unknown"

        }

        # -------------------------------------------------
        # Battle Meter
        # -------------------------------------------------

        battle_meter = calculate_battle_meter(

            abs(

                team1["total_runs"]

                -

                team2["total_runs"]

            ),

            "runs"

        )

        # -------------------------------------------------
        # Hype Meter
        # -------------------------------------------------

        hype_meter = calculate_hype_meter(

            team1["boundaries"]

            +

            team2["boundaries"],

            team1["sixes"]

            +

            team2["sixes"]

        )

        # -------------------------------------------------
        # Aura Score
        # -------------------------------------------------

        aura_score = calculate_aura_score(

            battle_meter,

            hype_meter

        )

        # -------------------------------------------------
        # Personality
        # -------------------------------------------------

        personality = determine_personality(

            aura_score,

            battle_meter,

            hype_meter,

            momentum["momentum_swings"]

        )

        # -------------------------------------------------
        # Achievements
        # -------------------------------------------------

        achievements = generate_achievements(

            total_boundaries=

                team1["boundaries"]

                +

                team2["boundaries"],

            total_sixes=

                team1["sixes"]

                +

                team2["sixes"],

            win_margin=

                abs(

                    team1["total_runs"]

                    -

                    team2["total_runs"]

                ),

            margin_type="runs",

            plot_twist_count=

                momentum["momentum_swings"]

        )

        # -------------------------------------------------
        # Signature Moment
        # -------------------------------------------------

        signature = determine_signature_moment(

            momentum["phase_winners"]["powerplay"],

            momentum["phase_winners"]["middle"],

            momentum["phase_winners"]["death"],

            abs(

                team1["total_runs"]

                -

                team2["total_runs"]

            ),

            "runs",

            momentum["momentum_swings"]

        )

        # -------------------------------------------------
        # AI Narrator
        # -------------------------------------------------

        narrator = MatchNarrator(

            match_details,

            timeline,

            momentum,

            drama,

            events

        )

        # -------------------------------------------------
        # Return Match Aura
        # -------------------------------------------------

        return MatchAura(

            aura_score=aura_score,

            personality=personality,

            battle_meter=battle_meter,

            hype_meter=hype_meter,

            drama_score=drama["drama_score"],

            phase_stats=phase_stats,

            momentum_timeline={

                "timeline": timeline,

                "phase_winners": momentum["phase_winners"],

                "momentum_swings": momentum["momentum_swings"],

                "dominating_team": momentum["dominating_team"]

            },

            plot_twists=events,

            achievements=achievements,

            signature_moment=signature,

            ai_verdict=narrator.generate(),

            ending=f"{winner} won the match."

        )