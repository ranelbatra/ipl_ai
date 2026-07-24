import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from ai.prompts import (
    MATCH_COMPARISON_PROMPT,
    TEAM_COMPARISON_PROMPT,
    PLAYER_COMPARISON_PROMPT
)

load_dotenv()

MODEL_NAME = os.environ.get(
    "HF_MODEL",
    "Qwen/Qwen2.5-7B-Instruct"
)

HF_TOKEN = (
    os.environ.get("HF_TOKEN")
    or os.environ.get("HUGGINGFACEHUB_API_TOKEN")
)

client = InferenceClient(
    model=MODEL_NAME,
    token=HF_TOKEN
)


# =====================================================
# Generic LLM Helper
# =====================================================

def ask_llm(system_prompt, user_prompt):

    completion = client.chat_completion(

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],

        max_tokens=900,

        temperature=0.3,

        top_p=0.9
    )

    return completion.choices[0].message.content


# =====================================================
# Match Comparison
# =====================================================

def generate_match_comparison(comparison):

    prompt = "Compare these two IPL matches.\n\n"

    for match in comparison:

        prompt += f"""
Match:
{match["Match"]}

Winner:
{match["Winner"]}

Venue:
{match["Venue"]}

Runs:
{match["Runs"]}

Wickets:
{match["Wickets"]}

Fours:
{match["Fours"]}

Sixes:
{match["Sixes"]}

------------------------------------
"""

    return ask_llm(
        MATCH_COMPARISON_PROMPT,
        prompt
    )


# =====================================================
# Team Comparison
# =====================================================

def generate_team_comparison(comparison):

    prompt = "Compare these IPL teams.\n\n"

    for team in comparison:

        prompt += f"""
Team:
{team["Team"]}

Runs:
{team["Runs"]}

Wickets:
{team["Wickets"]}

Run Rate:
{team["Run Rate"]}

Boundaries:
{team["Boundaries"]}

Sixes:
{team["Sixes"]}

Dot Balls:
{team["Dot Balls"]}

------------------------------------
"""

    return ask_llm(
        TEAM_COMPARISON_PROMPT,
        prompt
    )


# =====================================================
# Player Comparison
# =====================================================

def generate_player_comparison(comparison):

    prompt = "Compare these IPL players.\n\n"

    for player in comparison:

        prompt += f"""
Player:
{player["Player"]}

Runs:
{player["Runs"]}

Balls:
{player["Balls"]}

Strike Rate:
{player["Strike Rate"]}

Average:
{player["Average"]}

Fours:
{player["Fours"]}

Sixes:
{player["Sixes"]}

------------------------------------
"""

    return ask_llm(
        PLAYER_COMPARISON_PROMPT,
        prompt
    )