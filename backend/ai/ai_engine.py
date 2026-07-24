import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from match_aura.aura_engine import MatchAuraEngine
from .prompts import COMPARISON_PROMPT
from .prompts import SYSTEM_PROMPT
from .prompts import COACH_PROMPT


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

    deliveries = match["deliveries"]

    # ----------------------------------------
    # Ball-by-ball data
    # ----------------------------------------

    team1 = deliveries[deliveries["innings"] == 1].iloc[0]["team"]
    team2 = deliveries[deliveries["innings"] == 2].iloc[0]["team"]

    aura = MatchAuraEngine(deliveries).generate()

    phase = aura.phase_stats
    timeline = aura.momentum_timeline

    # ----------------------------------------
    # Build Case File
    # ----------------------------------------

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

================================================
PHASE STATISTICS
================================================

================================================
PHASE STATISTICS
================================================

POWERPLAY

{team1}

Runs:
{phase["powerplay"]["team1"]["runs"]}

Wickets:
{phase["powerplay"]["team1"]["wickets"]}


{team2}

Runs:
{phase["powerplay"]["team2"]["runs"]}

Wickets:
{phase["powerplay"]["team2"]["wickets"]}

------------------------------------------------

MIDDLE OVERS

{team1}

Runs:
{phase["middle"]["team1"]["runs"]}

Wickets:
{phase["middle"]["team1"]["wickets"]}


{team2}

Runs:
{phase["middle"]["team2"]["runs"]}

Wickets:
{phase["middle"]["team2"]["wickets"]}

------------------------------------------------

DEATH OVERS

{team1}

Runs:
{phase["death"]["team1"]["runs"]}

Wickets:
{phase["death"]["team1"]["wickets"]}


{team2}

Runs:
{phase["death"]["team2"]["runs"]}

Wickets:
{phase["death"]["team2"]["wickets"]}

================================================
MATCH AURA
================================================

Aura Score:
{aura.aura_score}

Battle Meter:
{aura.battle_meter}

Drama Score:
{aura.drama_score}

Personality:
{aura.personality}

Ending:
{aura.ending}

================================================
MOMENTUM
================================================

Momentum Swings:
{timeline["momentum_swings"]}

Dominating Team:
{timeline["dominating_team"]}

Phase Winners:

Powerplay:
{timeline["phase_winners"]["powerplay"]}

Middle Overs:
{timeline["phase_winners"]["middle"]}

Death Overs:
{timeline["phase_winners"]["death"]}

================================================
SIGNATURE MOMENT
================================================

{aura.signature_moment}

================================================
MATCH EVENTS
================================================
"""

    for event in aura.plot_twists:

        facts += f"""

Event:
{event["type"]}

Description:
{event["description"]}
"""

    facts += """

================================================
ACHIEVEMENTS
================================================
"""

    for achievement in aura.achievements:

        facts += f"\n• {achievement}"

    return facts


def ask_llm(system_prompt, user_prompt):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    completion = client.chat_completion(
        messages=messages,
        max_tokens=900,
        temperature=0.3,
        top_p=0.9
    )

    return completion.choices[0].message.content

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

def generate_match_coach(match):

    case_file = build_case_file(match)

    return ask_llm(
        COACH_PROMPT,
        case_file
    )

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



def generate_comparison_report(comparison):

    comparison_text = ""

    for item in comparison:

        comparison_text += f"""

--------------------------------

Name: {item.get("Player", item.get("Team"))}

Runs: {item.get("Runs")}

Balls: {item.get("Balls", "N/A")}

Fours: {item.get("Fours")}

Sixes: {item.get("Sixes")}

Strike Rate: {item.get("Strike Rate")}

Average: {item.get("Average", "N/A")}

Wins: {item.get("Wins", "N/A")}

Matches: {item.get("Matches", "N/A")}

Win Percentage: {item.get("Win %", "N/A")}

"""

    prompt = f"""
You are an elite IPL analyst.

Below are statistics of two cricket entities.
They may either be two teams or two players.

{comparison_text}

Write a professional comparison.

Format exactly like this:

## 🏆 Overall Winner

State who performed better overall.

## 📈 Strengths

Mention strengths of BOTH.

## ⚡ Aggression

Who attacks more?

## 🎯 Consistency

Who is more reliable?

## 🔥 Key Difference

Mention the biggest statistical difference.

## 💡 Final Verdict

Summarize in 3-4 sentences.
"""

    return ask_llm(
        SYSTEM_PROMPT,
        prompt
    )