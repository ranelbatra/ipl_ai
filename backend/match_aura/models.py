"""
Pydantic model for Match Aura
"""

from pydantic import BaseModel


class MatchAura(BaseModel):

    aura_score: int

    personality: str

    battle_meter: int

    hype_meter: int

    drama_score: int

    momentum_timeline: dict

    plot_twists: list

    achievements: list

    signature_moment: str

    ai_verdict: str

    ending: str