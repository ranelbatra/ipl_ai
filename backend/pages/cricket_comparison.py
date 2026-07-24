# cricket_comparison.py
import streamlit as st
import pandas as pd


from data.loader import (
    get_all_seasons,
    get_matches,
    get_match_details,
    get_match_deliveries,
    load_deliveries,
)

from ai.comparison_engine import (
    compare_matches,
    compare_teams,
    compare_players,
)

from ai.comparison_ai import (
    generate_match_comparison,
    generate_team_comparison,
    generate_player_comparison,
)





def cricket_comparison():

    st.markdown("""
    <h1 style="color:#556B2F;font-size:60px;font-family:Montserrat;">
    Cricket Comparison Studio
    </h1>
    """, unsafe_allow_html=True)

    st.subheader("⚔ Match Comparison")

    seasons = get_all_seasons()

    c1, c2 = st.columns(2)

    with c1:
        season1 = st.selectbox("Season 1", seasons)
        matches1 = get_matches(season1)
        match1 = st.selectbox("Match 1", matches1["display_name"])

    with c2:
        season2 = st.selectbox("Season 2", seasons)
        matches2 = get_matches(season2)
        match2 = st.selectbox("Match 2", matches2["display_name"])

    if st.button("⚔ Compare Matches", use_container_width=True, type="primary"):

        row1 = matches1[matches1["display_name"] == match1].iloc[0]
        row2 = matches2[matches2["display_name"] == match2].iloc[0]

        d1 = get_match_details(row1["match_id"])
        d2 = get_match_details(row2["match_id"])

        d1["deliveries"] = get_match_deliveries(row1["match_id"])
        d2["deliveries"] = get_match_deliveries(row2["match_id"])

        comparison = compare_matches(d1, d2)

        df = pd.DataFrame.from_records(comparison)

        st.dataframe(df, use_container_width=True)

        with st.spinner("🤖 Comparing matches..."):
            report = generate_match_comparison(comparison)

        st.markdown(report)

    st.divider()

    deliveries = load_deliveries()

    mode = st.radio(
        "Choose Comparison",
        ["🏏 Team Comparison", "👤 Player Comparison"],
        horizontal=True,
    )

    if mode == "🏏 Team Comparison":

        teams = sorted(deliveries["team"].dropna().unique())

        a, b = st.columns(2)

        with a:
            team1 = st.selectbox("Team 1", teams)

        with b:
            team2 = st.selectbox("Team 2", teams, index=1 if len(teams) > 1 else 0)

        if st.button("Compare Teams", use_container_width=True):

            comparison = compare_teams(deliveries, team1, team2)

            df = pd.DataFrame(comparison).T
            df.index.name = "Team"
            df.reset_index(inplace=True)

            st.dataframe(df, use_container_width=True)

            with st.spinner("🤖 Comparing teams..."):
                report = generate_team_comparison(comparison)

            st.markdown(report)

    else:

        players = sorted(deliveries["batter"].dropna().unique())

        a, b = st.columns(2)

        with a:
            player1 = st.selectbox("Player 1", players)

        with b:
            player2 = st.selectbox("Player 2", players, index=1 if len(players) > 1 else 0)

        if st.button("Compare Players", use_container_width=True):

            comparison = compare_players(deliveries, player1, player2)

            df = pd.DataFrame(comparison)

            st.dataframe(df, use_container_width=True)

            with st.spinner("🤖 Comparing players..."):
                report = generate_player_comparison(comparison)

            st.markdown(report)