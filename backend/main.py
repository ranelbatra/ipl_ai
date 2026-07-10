from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai_engine import generate_report

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
