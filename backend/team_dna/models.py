from pydantic import BaseModel


class TeamDNA(BaseModel):

    team: str

    batting_aggression: int

    batting_consistency: int

    bowling_strength: int

    pace_attack: int

    spin_attack: int

    finishing: int

    fielding: int

    experience: int

    personality: str