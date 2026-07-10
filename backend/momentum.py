def calculate_momentum(analytics):

    powerplay = analytics["powerplay"]["phase_winner"]
    middle = analytics["middle_overs"]["phase_winner"]
    death = analytics["death_overs"]["phase_winner"]

    phase_winners = [
        powerplay,
        middle,
        death
    ]

    momentum = {}

    for winner in phase_winners:

        if winner == "Equal":
            continue

        momentum[winner] = momentum.get(winner, 0) + 1

    if len(momentum) == 0:
        overall = "Equal"

    else:
        overall = max(momentum, key=momentum.get)

    if powerplay == middle == death:
        summary = f"{overall} dominated every phase of the match."

    elif powerplay == middle and middle != death:
        summary = f"{overall} built momentum early and maintained control despite the late fightback."

    elif middle == death and powerplay != middle:
        summary = f"{overall} recovered after the powerplay and controlled the remainder of the match."

    elif powerplay == death and middle != powerplay:
        summary = f"{overall} started strongly, briefly lost momentum, and finished strongly."

    else:
        summary = "Momentum shifted between both teams throughout the match."

    return {

        "powerplay_winner": powerplay,

        "middle_overs_winner": middle,

        "death_overs_winner": death,

        "overall_momentum": overall,

        "momentum_summary": summary

    }


def decisive_phase(analytics):

    winners = {

        "Powerplay": analytics["powerplay"]["phase_winner"],

        "Middle Overs": analytics["middle_overs"]["phase_winner"],

        "Death Overs": analytics["death_overs"]["phase_winner"]

    }

    count = {}

    for phase, team in winners.items():

        if team == "Equal":
            continue

        count[team] = count.get(team, 0) + 1

    if not count:
        return "Not enough information"

    dominant_team = max(count, key=count.get)

    for phase, team in winners.items():

        if team == dominant_team:
            return phase

    return "Powerplay"


def match_pressure(analytics):

    pressure = {}

    for phase_name in [

        "powerplay",

        "middle_overs",

        "death_overs"

    ]:

        phase = analytics[phase_name]

        run_gap = phase["run_difference"]

        wicket_gap = phase["wicket_difference"]

        score = run_gap + (wicket_gap * 5)

        pressure[phase_name] = score

    highest = max(pressure, key=pressure.get)

    return {

        "pressure_scores": pressure,

        "highest_pressure_phase": highest

    }