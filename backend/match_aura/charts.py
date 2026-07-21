"""
Charts for Match Aura
"""

import matplotlib.pyplot as plt


class MatchCharts:

    @staticmethod
    def momentum_chart(momentum_df):

        fig, ax = plt.subplots(figsize=(12,4))

        teams = momentum_df["team"].unique()

        for team in teams:

            team_df = momentum_df[
                momentum_df["team"] == team
            ]

            x = []

            for _, row in team_df.iterrows():

                x.append(
                    row["over"] +
                    (20 * (row["innings"] - 1))
                )

            ax.plot(
                x,
                team_df["momentum"],
                linewidth=3,
                marker="o",
                label=team
            )

        ax.set_title("Match Momentum")

        ax.set_xlabel("Overs")

        ax.set_ylabel("Momentum")

        ax.legend()

        ax.grid(True)

        return fig