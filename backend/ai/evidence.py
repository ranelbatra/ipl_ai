from .analytics import (
    calculate_run_rates,
    calculate_phase_winners,
    dominance_score,
    collapse_index,
    pressure_index
)

from .momentum import detect_momentum


# ---------------------------------------------------
# Phase Evidence
# ---------------------------------------------------

def build_phase_evidence(match):

    phase_winners = calculate_phase_winners(match)

    evidence = []

    for phase, data in phase_winners.items():

        if data is None:
            continue

        if data["winner"] == "Tie":

            evidence.append(
                f"{phase} was evenly contested by both teams."
            )

        else:

            evidence.append(

                f"{data['winner']} dominated the {phase} by "

                f"{data['margin']} runs."

            )

    return evidence


# ---------------------------------------------------
# Run Rate Evidence
# ---------------------------------------------------

def build_run_rate_evidence(match):

    run_rates = calculate_run_rates(match)

    evidence = []

    for phase, teams in run_rates.items():

        if len(teams) != 2:
            continue

        team_names = list(teams.keys())

        t1 = team_names[0]
        t2 = team_names[1]

        rr1 = teams[t1]["run_rate"]
        rr2 = teams[t2]["run_rate"]

        if rr1 > rr2:

            evidence.append(

                f"{t1} maintained a better scoring rate "

                f"({rr1} rpo) than {t2} "

                f"({rr2} rpo) during the {phase}."

            )

        elif rr2 > rr1:

            evidence.append(

                f"{t2} maintained a better scoring rate "

                f"({rr2} rpo) than {t1} "

                f"({rr1} rpo) during the {phase}."

            )

    return evidence


# ---------------------------------------------------
# Collapse Evidence
# ---------------------------------------------------

def build_collapse_evidence(match):

    collapse = collapse_index(match)

    evidence = []

    for team, level in collapse.items():

        if level == "Severe":

            evidence.append(

                f"{team} suffered a severe batting collapse."

            )

        elif level == "High":

            evidence.append(

                f"{team} lost wickets at regular intervals."

            )

        elif level == "Medium":

            evidence.append(

                f"{team} struggled to build partnerships."

            )

    return evidence


# ---------------------------------------------------
# Pressure Evidence
# ---------------------------------------------------

def build_pressure_evidence(match):

    pressure = pressure_index(match)

    if pressure == "Extreme":

        return [

            "The chasing side faced extreme scoreboard pressure."

        ]

    if pressure == "High":

        return [

            "Required Run Rate kept increasing during the chase."

        ]

    if pressure == "Medium":

        return [

            "The chase remained competitive throughout."

        ]

    return [

        "The chase stayed under control."

    ]


# ---------------------------------------------------
# Momentum Evidence
# ---------------------------------------------------

def build_momentum_evidence(match):

    momentum = detect_momentum(match)

    return [

        f"The major turning point came during the "

        f"{momentum['prime_suspect']}.",

        momentum["reason"]

    ]


# ---------------------------------------------------
# Dominance Evidence
# ---------------------------------------------------

def build_dominance_evidence(match):

    dominance = dominance_score(match)

    evidence = []

    if len(dominance) == 0:

        return evidence

    winner = max(

        dominance,

        key=dominance.get

    )

    evidence.append(

        f"{winner} controlled "

        f"{dominance[winner]} "

        f"out of the three phases."

    )

    return evidence


# ---------------------------------------------------
# Master Function
# ---------------------------------------------------

def build_evidence(match):

    evidence = []

    evidence.extend(

        build_phase_evidence(match)

    )

    evidence.extend(

        build_run_rate_evidence(match)

    )

    evidence.extend(

        build_collapse_evidence(match)

    )

    evidence.extend(

        build_pressure_evidence(match)

    )

    evidence.extend(

        build_momentum_evidence(match)

    )

    evidence.extend(

        build_dominance_evidence(match)

    )

    # Remove duplicates

    final = []

    for item in evidence:

        if item not in final:

            final.append(item)

    return final


# ---------------------------------------------------
# Testing
# ---------------------------------------------------

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

    evidence = build_evidence(sample)

    for i, item in enumerate(evidence, 1):

        print(f"{i}. {item}")