from loader import IPLDataLoader
from analytics import CricketAnalytics


loader = IPLDataLoader(

    csv_path="IPL_matches.csv",

    excel_path="IPL_Data.xlsx"

)


analytics = CricketAnalytics(loader)


print(
analytics.compare_teams(
    "RCB",
    "Royal Challengers Bengaluru"
)
)