from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

from .analytics import match_summary
from .momentum import detect_momentum
from .evidence import build_evidence
from .prompts import SYSTEM_PROMPT


# ----------------------------------------------------
# LOAD MODEL ONLY ONCE
# ----------------------------------------------------

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

print("Loading IPL Detective AI...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto"
)

print("AI Detective Ready!")


# ----------------------------------------------------
# Build Facts
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

Player of Match:
{match["player_of_match"]}

------------------------------------------------

PHASE SCORES

------------------------------------------------

Powerplay

{match["powerplay"]}

Middle Overs

{match["middle"]}

Death Overs

{match["death"]}

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
# Ask Qwen
# ----------------------------------------------------

def ask_qwen(case_file):

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

    prompt = tokenizer.apply_chat_template(

        messages,

        tokenize=False,

        add_generation_prompt=True

    )

    inputs = tokenizer(

        prompt,

        return_tensors="pt"

    ).to(model.device)

    outputs = model.generate(

        **inputs,

        max_new_tokens=700,

        temperature=0.35,

        top_p=0.90,

        do_sample=True,

        repetition_penalty=1.12

    )

    answer = tokenizer.decode(

        outputs[0][inputs.input_ids.shape[1]:],

        skip_special_tokens=True

    )

    return answer


# ----------------------------------------------------
# Main Function
# ----------------------------------------------------

def generate_report(match):

    case_file = build_case_file(match)

    report = ask_qwen(case_file)

    return {

        "summary": report,

        "case_file": case_file

    }


# ----------------------------------------------------
# Testing
# ----------------------------------------------------

if __name__ == "__main__":

    sample = {

        "match":"RCB vs PBKS",

        "venue":"M Chinnaswamy Stadium",

        "date":"18 April 2025",

        "winner":"Punjab Kings",

        "result":"Punjab Kings won by 6 wickets",

        "toss":"RCB elected to field",

        "player_of_match":"Shreyas Iyer",

        "powerplay":"RCB:42/1, PBKS:61/0",

        "middle":"RCB:71/5, PBKS:89/2",

        "death":"RCB:48/3, PBKS:54/1",

        "rrr":"8.75 rpo"

    }

    result = generate_report(sample)

    print(result["summary"])