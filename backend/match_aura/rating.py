"""
Match Rating
"""


class MatchRating:

    @staticmethod
    def calculate(aura):

        if aura >= 95:
            return 5

        if aura >= 85:
            return 4

        if aura >= 70:
            return 3

        if aura >= 50:
            return 2

        return 1