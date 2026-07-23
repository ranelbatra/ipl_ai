"""
IPL Team Name Normalization
---------------------------
Handles old and new franchise names.
"""


TEAM_MAPPING = {

    "royal challengers bangalore":
        "Royal Challengers Bangalore",

    "royal challengers bengaluru":
        "Royal Challengers Bangalore",


    "delhi daredevils":
        "Delhi Capitals",

    "delhi capitals":
        "Delhi Capitals",


    "kings xi punjab":
        "Punjab Kings",

    "punjab kings":
        "Punjab Kings",


    "rising pune supergiant":
        "Rising Pune Supergiant",

    "rising pune supergiants":
        "Rising Pune Supergiant",


    "chennai super kings":
        "Chennai Super Kings",

    "mumbai indians":
        "Mumbai Indians",

    "kolkata knight riders":
        "Kolkata Knight Riders",

    "rajasthan royals":
        "Rajasthan Royals",

    "sunrisers hyderabad":
        "Sunrisers Hyderabad",

    "gujarat titans":
        "Gujarat Titans",

    "lucknow super giants":
        "Lucknow Super Giants"

}



def normalize_team(team):

    return TEAM_MAPPING.get(
        team.lower().strip(),
        team
    )