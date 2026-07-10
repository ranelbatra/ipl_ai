from transformers import AutoTokenizer, AutoModelForCausalLM
from formatter import format_analytics
from prompts import SYSTEM_PROMPT
from analytics import analyze_match
from momentum import calculate_momentum, decisive_phase, match_pressure

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)


def generate_report(request):

    analytics = analyze_match(request)

    momentum = calculate_momentum(analytics)

    decisive = decisive_phase(analytics)

    pressure = match_pressure(analytics)

    formatted_analytics = format_analytics(analytics)

    match_information = f"""
================ MATCH DETAILS ================

Team 1: {request.team1}
Team 2: {request.team2}

Winner: {request.winner}

Venue: {request.venue}

Player of the Match: {request.playerOfMatch}

Result: {request.result}

Powerplay:
{request.powerplay}

Middle Overs:
{request.middleOvers}

Death Overs:
{request.deathOvers}

===============================================

{formatted_analytics}

===============================================

MOMENTUM ANALYSIS

{momentum}

===============================================

DECISIVE PHASE

{decisive}

===============================================

PRESSURE ANALYSIS

{pressure}

===============================================
"""

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },

        {
            "role": "user",
            "content": match_information
        }

    ]

    inputs = tokenizer.apply_chat_template(

        messages,

        tokenize=True,

        add_generation_prompt=True,

        return_dict=True,

        return_tensors="pt"

    )

    outputs = model.generate(

        **inputs,

        max_new_tokens=450,

        temperature=0.3,

        top_p=0.9,

        do_sample=True

    )

    report = tokenizer.decode(

        outputs[0][inputs["input_ids"].shape[-1]:],

        skip_special_tokens=True

    )

    return report