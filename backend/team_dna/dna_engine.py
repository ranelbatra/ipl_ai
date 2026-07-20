from team_dna.feature_extractor import TeamDNAFeatureExtractor
from team_dna.personality import determine_personality
from team_dna.models import TeamDNA


class TeamDNAEngine:

    def __init__(self, team_name, player_stats):

        self.team = team_name
        self.player_stats = player_stats

    def generate(self):

        features = TeamDNAFeatureExtractor(
            self.player_stats
        ).extract_all_features()

        personality = determine_personality(features)

        return TeamDNA(

            team=self.team,

            batting_aggression=features["batting_aggression"],

            batting_consistency=features["batting_consistency"],

            bowling_strength=features["bowling_strength"],

            pace_attack=features["pace_attack"],

            spin_attack=features["spin_attack"],

            finishing=features["finishing"],

            fielding=features["fielding"],

            experience=features["experience"],

            personality=personality

        )