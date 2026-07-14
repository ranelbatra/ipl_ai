from .analytics import (
    calculate_phase_winners,
    calculate_run_rates,
    dominance_score,
    collapse_index,
    pressure_index
)


# -------------------------------------------------------
# Determine Momentum Winner
# -------------------------------------------------------

def detect_momentum(match):

    phase_winners = calculate_phase_winners(match)

    dominance = dominance_score(match)

    collapse = collapse_index(match)

    pressure = pressure_index(match)

    report = {

        "prime_suspect": None,

        "turning_point": None,

        "confidence": 0,

        "reason": "",

        "momentum_team": None

    }

    # --------------------------------------------
    # Count phase wins
    # --------------------------------------------

    if len(dominance) == 0:

        report["prime_suspect"] = "Unknown"

        report["turning_point"] = "Unknown"

        report["confidence"] = 50

        report["reason"] = "Insufficient match data."

        return report

    momentum_team = max(

        dominance,

        key=dominance.get

    )

    report["momentum_team"] = momentum_team

    # --------------------------------------------
    # Find strongest phase
    # --------------------------------------------

    biggest_margin = -1

    suspect = None

    for phase_name, data in phase_winners.items():

        if data is None:

            continue

        if data["winner"] != momentum_team:

            continue

        if data["margin"] > biggest_margin:

            biggest_margin = data["margin"]

            suspect = phase_name

    report["prime_suspect"] = suspect

    report["turning_point"] = suspect

    # --------------------------------------------
    # Confidence Score
    # --------------------------------------------

    confidence = 60

    confidence += dominance[momentum_team] * 10

    if collapse.get(momentum_team) == "Low":

        confidence += 10

    if pressure == "High":

        confidence += 5

    if pressure == "Extreme":

        confidence += 10

    confidence = min(confidence, 99)

    report["confidence"] = confidence

    # --------------------------------------------
    # Reason Builder
    # --------------------------------------------

    reasons = []

    reasons.append(

        f"{momentum_team} controlled {dominance[momentum_team]} out of 3 phases."

    )

    if suspect:

        reasons.append(

            f"The biggest momentum swing occurred during the {suspect}."

        )

    if collapse.get(momentum_team) == "Low":

        reasons.append(

            f"{momentum_team} avoided losing wickets at crucial moments."

        )

    if pressure == "Extreme":

        reasons.append(

            "The chasing side faced extreme scoreboard pressure."

        )

    elif pressure == "High":

        reasons.append(

            "Required run rate kept increasing during the chase."

        )

    report["reason"] = " ".join(reasons)

    return report


# -------------------------------------------------------
# Human Friendly Momentum Text
# -------------------------------------------------------

def momentum_summary(match):

    momentum = detect_momentum(match)

    text = f"""

Prime Suspect:
{momentum['prime_suspect']}

Turning Point:
{momentum['turning_point']}

Momentum Team:
{momentum['momentum_team']}

Confidence:
{momentum['confidence']}%

Reason:
{momentum['reason']}

"""

    return text


# -------------------------------------------------------
# Match Rating
# -------------------------------------------------------

def match_rating(match):

    dominance = dominance_score(match)

    collapse = collapse_index(match)

    total = sum(

        dominance.values()

    )

    stars = 3

    if total == 3:

        stars = 5

    elif total == 2:

        stars = 4

    if "Severe" in collapse.values():

        stars -= 1

    stars = max(stars, 1)

    return "★" * stars + "☆" * (5 - stars)


# -------------------------------------------------------
# Testing
# -------------------------------------------------------

if __name__ == "__main__":

    sample = {

        "powerplay":

            "KKR:61/1,RCB:26/4",

        "middle":

            "KKR:101/1,RCB:41/5",

        "death":

            "KKR:60/1,RCB:28/1",

        "rrr":

            "10.75 rpo"

    }

    print(

        detect_momentum(sample)

    )

    print(

        momentum_summary(sample)

    )

    print(

        match_rating(sample)

    )