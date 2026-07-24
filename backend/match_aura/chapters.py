"""
Creates Netflix-style chapters for the match.
"""

from collections import defaultdict


class ChapterGenerator:

    def __init__(self, events):
        self.events = events

    def generate(self):

        grouped_events = defaultdict(list)

        # Group all events by type
        for event in self.events:
            grouped_events[event["type"]].append(event["description"])

        title_map = {

            "Explosive Overs": "💥 Powerplay Blitz",

            "Momentum Shift": "🔄 The Turning Point",

            "Wicket Cluster": "🎯 Wickets Tumble",

            "Comeback": "🔥 The Fightback",

            "Milestone": "🏆 Record Moment",

            "Boundary Spree": "🚀 Boundary Barrage",

            "Hat-trick": "🎩 Hat-trick Heroics",

            "Partnership": "🤝 Match-winning Partnership"

        }

        chapters = []

        for event_type, descriptions in grouped_events.items():

            title = title_map.get(event_type, event_type)

            description = ""

            for i, text in enumerate(descriptions, start=1):
                description += f"{i}. {text}\n\n"

            chapters.append({

                "title": title,

                "description": description.strip()

            })

        return chapters