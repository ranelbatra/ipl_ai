from pydantic import BaseModel
from typing import List


class DetectiveResponse(BaseModel):
    case_summary: str
    primary_suspect: str
    evidence: List[str]
    turning_point: str
    alternative_strategy: str
    prevention_plan: str
    final_verdict: str