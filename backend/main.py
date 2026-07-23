from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.ai.ai_engine import generate_report
from backend.data.loader import get_match_deliveries
from backend.match_aura.aura_engine import MatchAuraEngine

app = FastAPI()

class MatchRequest(BaseModel):
    team1: str
    team2: str
    winner: str
    powerplay: str

    middleOvers: str
    deathOvers: str
    playerOfMatch: str
    venue: str
    result: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/overview")
def overview():
    return {
        "matches": 1234,
        "players": 321,
        "teams": 19,
        "venues": 62
    }

from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

@app.post("/investigate")
def investigate(request: MatchRequest):
    try:
        report = generate_report(request.model_dump())

        if not report:
            raise HTTPException(
                status_code=404,
                detail="Unable to generate match report."
            )

        return {"report": report}

    except HTTPException:
        raise

    except FileNotFoundError:
        logger.exception("Dataset not found")
        raise HTTPException(
            status_code=500,
            detail="Required dataset is missing."
        )

    except ValueError as e:
        logger.exception(e)
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception:
        logger.exception("Unexpected error while generating report")
        raise HTTPException(
            status_code=500,
            detail="Unexpected server error. Please try again."
        )

@app.get("/match-aura/{match_id}")
def get_match_aura(match_id: int):

    try:

        deliveries = get_match_deliveries(match_id)

        if deliveries.empty:
            raise HTTPException(
                status_code=404,
                detail="Match not found."
            )

        engine = MatchAuraEngine(deliveries)

        aura = engine.generate()

        return aura.model_dump()

    except HTTPException:
        raise

    except Exception:
        logger.exception("Error generating Match Aura")

        raise HTTPException(
            status_code=500,
            detail="Unable to generate Match Aura."
        )