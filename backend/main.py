from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.ai.ai_engine import generate_report
from backend.loader import get_match_deliveries
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

@app.post("/investigate")
def investigate_match(request: MatchRequest):
    try:
        report = generate_report(request)

        return {
            "detective_report": report
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/match-aura/{match_id}")
def get_match_aura(match_id: int):

    try:

        deliveries = get_match_deliveries(match_id)

        if deliveries.empty:

            return {
                "error": "Match not found."
            }

        engine = MatchAuraEngine(deliveries)

        aura = engine.generate()

        return aura.model_dump()

    except Exception as e:

        return {
            "error": str(e)
        }