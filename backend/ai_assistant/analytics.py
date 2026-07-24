"""
Cricket Analytics Engine
------------------------

Central analytics layer for:

- AI Cricket Assistant
- Cricket Comparison Studio
- Match Aura Analysis
- Team DNA Comparison

"""

from ai_assistant.team_mapping import normalize_team

class CricketAnalytics:


    def __init__(self, loader):

        self.matches = loader.matches

        self.innings = loader.innings

        self.deliveries = loader.deliveries

        self.player_match = (
            loader.player_match_stats
        )

        self.player_career = (
            loader.player_career_stats
        )

        self.team_stats = (
            loader.team_match_stats
        )

        self.team_dna = (
            loader.team_dna
        )

        self.match_aura = (
            loader.match_aura
        )



    # ======================================================
    # TEAM ANALYTICS
    # ======================================================


    def team_profile(self, team):

        """
        Returns complete team analysis
        """

        data = self.team_dna[
            self.team_dna["team"]
            .str.lower()
            ==
            normalize_team(team)
        ]


        if data.empty:
            return {
                "error":
                "Team not found"
            }


        return data.iloc[0].to_dict()



    def team_match_stats(self, team):

        """
        Overall team performance
        """

        data = self.team_stats[
            self.team_stats["team"]
            .str.lower()
            ==
            normalize_team(team)
        ]


        if data.empty:

            return {
                "error":
                "No team stats found"
            }


        return {

            "average_runs":
                data["total_runs"]
                .mean(),


            "average_run_rate":
                data["run_rate"]
                .mean(),


            "average_wickets":
                data["total_wickets"]
                .mean()
        }



    # ======================================================
    # TEAM COMPARISON
    # ======================================================


    def compare_teams(
        self,
        team1,
        team2
):

        team1 = normalize_team(team1)
        team2 = normalize_team(team2)


        return {

        team1:
        self.team_profile(team1),

        team2:
        self.team_profile(team2)

    }



    # ======================================================
    # MATCH AURA
    # ======================================================


    def match_aura_analysis(
        self,
        match_id
    ):

        data = self.match_aura[
            self.match_aura["match_id"]
            ==
            match_id
        ]


        if data.empty:

            return {
                "error":
                "Aura data unavailable"
            }


        return data.iloc[0].to_dict()



    # ======================================================
    # PLAYER ANALYTICS
    # ======================================================


    def player_profile(
        self,
        player
    ):


        data = self.player_career[
            self.player_career["player"]
            .str.lower()
            ==
            player.lower()
        ]


        if data.empty:

            return {
                "error":
                "Player not found"
            }


        return data.iloc[0].to_dict()



    def compare_players(
        self,
        player1,
        player2
    ):


        return {

            player1:
            self.player_profile(player1),


            player2:
            self.player_profile(player2)

        }



    # ======================================================
    # MATCH HISTORY
    # ======================================================


    def head_to_head(
        self,
        team1,
        team2
    ):


        matches = self.matches[

            (

            (
            self.matches["team_1"]
            .str.lower()
            ==
            team1.lower()
            )

            |

            (
            self.matches["team_2"]
            .str.lower()
            ==
            team1.lower()
            )

            )

            &

            (

            (
            self.matches["team_1"]
            .str.lower()
            ==
            team2.lower()
            )

            |

            (
            self.matches["team_2"]
            .str.lower()
            ==
            team2.lower()
            )

            )

        ]


        return {

            "matches_played":
            len(matches),


            team1+"_wins":
            len(
                matches[
                    matches["winner"]
                    .str.lower()
                    ==
                    team1.lower()
                ]
            ),


            team2+"_wins":
            len(
                matches[
                    matches["winner"]
                    .str.lower()
                    ==
                    team2.lower()
                ]
            )

        }

