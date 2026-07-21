import streamlit as st

from data.loader import (
    get_all_seasons,
    get_matches,
    get_match_details,
    get_match_deliveries
)

from match_aura.aura_engine import MatchAuraEngine
from match_aura.charts import MatchCharts
from match_aura.chapters import ChapterGenerator
from match_aura.rating import MatchRating


def match_aura():

    st.markdown(
        """
        <h1 style='
            color:#556B2F;
            font-size:60px;
            font-family:Montserrat;'>
        Match Aura
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ==========================================
    # SELECT SEASON
    # ==========================================

    seasons = get_all_seasons()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Season")

        season = st.selectbox(
            "Select Season",
            seasons,
            label_visibility="collapsed"
        )

    # ==========================================
    # SELECT MATCH
    # ==========================================

    matches_df = get_matches(season)

    with col2:

        st.subheader("Match")

        selected_match_name = st.selectbox(
            "Select Match",
            matches_df["display_name"],
            label_visibility="collapsed"
        )

    # ==========================================
    # GET MATCH ID
    # ==========================================

    selected_row = matches_df[
        matches_df["display_name"] == selected_match_name
    ].iloc[0]

    match_id = selected_row["match_id"]

    # ==========================================
    # LOAD MATCH
    # ==========================================

    match_details = get_match_details(match_id)

    if match_details is None:
        st.error("Match not found.")
        return

    deliveries = get_match_deliveries(match_id)

    if deliveries.empty:
        st.warning("No delivery data available for this match.")
        return

    # ==========================================
    # GENERATE MATCH AURA
    # ==========================================

    engine = MatchAuraEngine(deliveries)

    aura = engine.generate()

    timeline = aura.momentum_timeline

    chapters = ChapterGenerator(
    aura.plot_twists
).generate()

    rating = MatchRating.calculate(
    aura.aura_score
)

    team1_name = match_details["team1"]
    team2_name = match_details["team2"]

    signature_moment = (
        aura.signature_moment
        .replace("Team 1", team1_name)
        .replace("Team 2", team2_name)
    )

    timeline = aura.momentum_timeline
    phase = timeline["phase_winners"]
    chart = MatchCharts.momentum_chart(
    timeline["timeline"]
)

    powerplay = (
        phase["powerplay"]
        .replace("Team 1", team1_name)
        .replace("Team 2", team2_name)
    )

    middle = (
        phase["middle"]
        .replace("Team 1", team1_name)
        .replace("Team 2", team2_name)
    )

    death = (
        phase["death"]
        .replace("Team 1", team1_name)
        .replace("Team 2", team2_name)
    )

    dominating = (
        timeline["dominating_team"]
        .replace("Team 1", team1_name)
        .replace("Team 2", team2_name)
    )

    # ==========================================
    # MATCH DETAILS
    # ==========================================

    st.divider()

    st.subheader("🏏 Match")

    st.write(
        f"**{match_details['team1']} vs {match_details['team2']}**"
    )

    st.write(f"**Winner:** {match_details['winner']}")

    st.write(f"**Venue:** {match_details['venue']}")

    st.write(f"**Date:** {match_details['date']}")

    st.divider()

    # ==========================================
    # METRICS
    # ==========================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Aura Score",
            aura.aura_score
        )

    with c2:
        st.metric(
            "Battle Meter",
            aura.battle_meter
        )

    with c3:
        st.metric(
            "Hype Meter",
            aura.hype_meter
        )

    with c4:
        st.metric(
    "Drama Score",
    aura.drama_score
)
        
    st.divider()

    st.subheader("📈 Match Momentum")

    chart = MatchCharts.momentum_chart(
    timeline["timeline"]
)

    st.pyplot(chart)

    st.divider()

    # ==========================================
    # PERSONALITY
    # ==========================================

    st.subheader("🎭 Match Personality")

    st.success(aura.personality)

    st.divider()

    # ==========================================
    # MOMENTUM
    # ==========================================

    st.subheader("📈 Momentum Timeline")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("⚡ Powerplay", powerplay)

    with c2:
        st.metric("🏏 Middle Overs", middle)

    with c3:
        st.metric("💥 Death Overs", death)

    st.write("")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "🔄 Momentum Swings",
            timeline["momentum_swings"]
        )

    with c2:
        st.metric(
            "👑 Dominating Team",
            dominating
        )

    st.divider()

    # ==========================================
    # PLOT TWISTS
    # ==========================================

    st.subheader("🌪 Match Events")

    for event in aura.plot_twists:

        if event["severity"] == "High":

            st.error(
            f"🔥 {event['type']}\n\n{event['description']}"
        )

        elif event["severity"] == "Medium":

            st.warning(
            f"⚠ {event['type']}\n\n{event['description']}"
        )

        else:

            st.info(
            f"ℹ {event['type']}\n\n{event['description']}"
        )

    st.divider()

    st.subheader("🎬 Match Chapters")

    for chapter in chapters:

        st.markdown("---")

        st.markdown(
        f"### {chapter['title']}"
    )

        st.write(
        chapter["description"]
    )

    st.divider()

    # ==========================================
    # ACHIEVEMENTS
    # ==========================================

    st.subheader("🏅 Achievements")

    for achievement in aura.achievements:
        st.success(achievement)

    st.divider()

    # ==========================================
    # SIGNATURE MOMENT
    # ==========================================

    st.subheader("⭐ Signature Moment")

    st.info(signature_moment)

    st.divider()

    st.subheader("⭐ Match Rating")

    st.write("⭐" * rating)

    st.divider()

    # ==========================================
    # AI VERDICT
    # ==========================================

    st.subheader("🎙 Match Story")

    st.success(aura.ai_verdict)

    st.divider()

    # ==========================================
    # ENDING
    # ==========================================

    st.subheader("🏁 Ending")

    st.write(aura.ending)