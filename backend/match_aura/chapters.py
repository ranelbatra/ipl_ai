"""
Creates Netflix-style chapters for the match.
"""


class ChapterGenerator:

    def __init__(self, events):

        self.events = events

    def generate(self):

        chapters = []

        for event in self.events:

            chapters.append({

                "title": event["type"],

                "description": event["description"]

            })

        return chapters