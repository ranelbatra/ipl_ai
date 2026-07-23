"""
IPL Data Loader
---------------
Loads CSV + Excel datasets required by AI features.
"""

import pandas as pd


class IPLDataLoader:

    def __init__(
        self,
        csv_path,
        excel_path
    ):

        # Match metadata CSV
        self.matches_csv = pd.read_csv(
            csv_path
        )


        # Excel sheets

        self.matches = pd.read_excel(
            excel_path,
            sheet_name="Matches"
        )

        self.innings = pd.read_excel(
            excel_path,
            sheet_name="Innings"
        )

        self.deliveries = pd.read_excel(
            excel_path,
            sheet_name="Deliveries"
        )

        self.player_match_stats = pd.read_excel(
            excel_path,
            sheet_name="Player_Match_Stats"
        )

        self.player_career_stats = pd.read_excel(
            excel_path,
            sheet_name="Player_Career_Stats"
        )

        self.team_match_stats = pd.read_excel(
            excel_path,
            sheet_name="Team_Match_Stats"
        )

        self.team_dna = pd.read_excel(
            excel_path,
            sheet_name="Team_DNA"
        )

        self.match_aura = pd.read_excel(
            excel_path,
            sheet_name="Match_Aura"
        )