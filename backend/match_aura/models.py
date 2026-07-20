from pydantic import BaseModel
from typing import Dict, Any, List


class MatchAura(BaseModel):
    # Overall score (0-100)
    aura_score: int

    # Match identity
    personality: str

    # Core meters
    battle_meter: int
    hype_meter: int

    # Momentum by phase
    momentum_timeline: Dict[str, Any]

    # Interesting events
    plot_twists: List[str]

    # Gamification
    achievements: List[str]

    # Highlight
    signature_moment: str

    # AI summary (placeholder for Sprint 2)
    ai_verdict: str

    # Final feeling of the match
    ending: str