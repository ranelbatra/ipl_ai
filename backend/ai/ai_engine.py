import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from .analytics import match_summary
from .momentum import detect_momentum
from .evidence import build_evidence
from .prompts import SYSTEM_PROMPT

# ----------------------------------------------------
# Load Environment Variables
# ----------------------------------------------------

load_dotenv()

MODEL_NAME = os.environ.get("HF_MODEL", "Qwen/Qwen2.5-7B-Instruct")

HF_TOKEN = (
    os.environ.get("HF_TOKEN")
    or os.environ.get("HUGGINGFACEHUB_API_TOKEN")
)

if not HF_TOKEN:
    raise RuntimeError(
        "HF_TOKEN is not set. Export your Hugging Face token before starting the server."
    )

client = InferenceClient(
    model=MODEL_NAME,
    token=HF_TOKEN
)

# ----------------------------------------------------
# Build Case File
# ----------------------------------------------------

def build_case_file(match):

    analytics = match_summary(match)
    momentum = detect_momentum(match)
    evidence = build_evidence(match)

    facts = f"""
================================================
MATCH DETAILS
================================================

Match:
{match["match"]}

Venue:
{match["venue"]}

Date:
{match["date"]}

Winner:
{match["winner"]}

Result:
{match["result"]}

Toss:
{match["toss"]}

Player of the Match:
{match["player_of_match"]}

------------------------------------------------
PHASE SCORES
------------------------------------------------

Powerplay
{match["powerplay"]}

Middle Overs
{match["middleOvers"]}

Death Overs
{match["deathOvers"]}

------------------------------------------------
ANALYTICS
------------------------------------------------

{analytics}

------------------------------------------------
MOMENTUM
------------------------------------------------

Prime Suspect:
{momentum["prime_suspect"]}

Turning Point:
{momentum["turning_point"]}

Momentum Team:
{momentum["momentum_team"]}

Confidence:
{momentum["confidence"]}

Reason:
{momentum["reason"]}

------------------------------------------------
EVIDENCE
------------------------------------------------
"""

    for item in evidence:
        facts += f"\n• {item}"

    return facts


# ----------------------------------------------------
# Generate AI Detective Report
# ----------------------------------------------------

def generate_report(match):

    case_file = build_case_file(match)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": case_file
        }
    ]

    completion = client.chat_completion(
        messages=messages,
        max_tokens=900,
        temperature=0.3,
        top_p=0.9
    )

    report = completion.choices[0].message.content

    return report


# ----------------------------------------------------
# Testing
# ----------------------------------------------------

if __name__ == "__main__":

    sample = {
        "match": "RCB vs PBKS",
        "venue": "M Chinnaswamy Stadium",
        "date": "18 April 2025",
        "winner": "Punjab Kings",
        "result": "Punjab Kings won by 6 wickets",
        "toss": "RCB elected to field",
        "player_of_match": "Shreyas Iyer",
        "powerplay": "RCB:42/1, PBKS:61/0",
        "middle": "RCB:71/5, PBKS:89/2",
        "death": "RCB:48/3, PBKS:54/1",
        "rrr": "8.75 rpo"
    }

    report = generate_report(sample)

    print(report)