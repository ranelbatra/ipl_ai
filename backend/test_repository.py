from data.repository import *

print(get_all_teams()[:5])

print(get_all_venues()[:5])

print(get_matches_by_season(2024).head())

from data.loader import get_all_matches
