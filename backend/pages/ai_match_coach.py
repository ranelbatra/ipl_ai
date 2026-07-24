import streamlit as st
from data.loader import (
    get_all_seasons,
    get_matches,
    get_match_details,
    get_match_deliveries
)

from ai.ai_engine import generate_match_coach


def ai_match_coach():

    st.markdown(
        """
        <h1 style="
            color:#556B2F;
            font-size:60px;
            font-family:Montserrat;
        ">
            AI Match Coach
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # -----------------------------------------
    # Season
    # -----------------------------------------

    seasons = get_all_seasons()

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("Season")

        season = st.selectbox(
            "Season",
            seasons,
            label_visibility="collapsed"
        )

    # -----------------------------------------
    # Match
    # -----------------------------------------

    matches = get_matches(season)

    with c2:

        st.subheader("Match")

        selected_match_name = st.selectbox(
            "Match",
            matches["display_name"],
            label_visibility="collapsed"
        )

    selected_row = matches[
        matches["display_name"] == selected_match_name
    ].iloc[0]

    match = get_match_details(
        selected_row["match_id"]
    )

    st.divider()

    st.subheader("🏏 Match Information")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Winner",
        match["winner"]
    )

    col2.metric(
        "Venue",
        match["venue"]
    )

    col3.metric(
        "Player of Match",
        match["player_of_match"]
    )

    

    if st.button(
    "🏏 Generate Coaching Report",
    use_container_width=True,
    type="primary"
):

        match_id = selected_row["match_id"]

    # -----------------------------------------
    # Load ball-by-ball data
    # -----------------------------------------

        deliveries = get_match_deliveries(match_id)

        if deliveries.empty:

            st.error(
            "No ball-by-ball data found for this match."
        )

            st.stop()

    # Attach deliveries for Match Aura Engine

        match["deliveries"] = deliveries

        if "result" not in match:
            match["result"] = f"{match['winner']} won the match"

    # -----------------------------------------
    # Generate Report
    # -----------------------------------------

        with st.spinner(
        "🏏 AI Coach is analyzing the match..."
    ):

            report = generate_match_coach(match)

        st.divider()

        st.subheader(
        "🧠 AI Match Coach"
    )

        st.markdown(
        f"""
<div style="
background:white;
padding:30px;
border-radius:15px;
border:1px solid #E5E5E5;
box-shadow:0px 2px 10px rgba(0,0,0,.08);
font-size:18px;
line-height:1.8;
">

{report.replace(chr(10), "<br>")}

</div>
""",
        unsafe_allow_html=True
    )

        st.download_button(
        "📄 Download Coaching Report",
        report,
        file_name="match_coach_report.md",
        mime="text/markdown"
    )