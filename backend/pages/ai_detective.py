import streamlit as st
import logging
import traceback
from data.loader import *
from ai.ai_engine import generate_report
logger = logging.getLogger(__name__)


def ai_detective():
    from data.loader import (
        get_all_seasons,
        get_matches,
        get_match_details
    )

    import time

    st.markdown("""
    <style>

    .title{

        font-size:42px;

        font-weight:800;

        color:#556B2F;

        text-align:center;

        margin-bottom:10px;

    }

    .subtitle{

        text-align:center;

        color:#777;

        margin-bottom:30px;

    }

    .summary-card{

        background:white;

        padding:25px;

        border-radius:18px;

        border:1px solid #E7E7E7;

        box-shadow:0px 3px 15px rgba(0,0,0,0.08);

    }

    .section-heading{

        font-size:28px;

        font-weight:bold;

        color:#556B2F;

        margin-top:20px;

        margin-bottom:15px;

    }

    .phase-card{

        background:white;

        padding:20px;

        border-radius:15px;

        border:1px solid #ECECEC;

        box-shadow:0px 3px 12px rgba(0,0,0,.05);

        height:220px;

    }

    .phase-title{

        font-size:22px;

        font-weight:bold;

        color:#556B2F;

    }

    .detective-card{

        background:white;

        padding:30px;

        border-radius:18px;

        border:1px solid #E5E5E5;

        box-shadow:0px 3px 15px rgba(0,0,0,.08);

    }

    .report{

        font-size:17px;

        line-height:1.8;

    }
                
    .label-name{
        font-size:26px;
        font-weight:bold;
        color:#222;
        font-family:Georgia;
        line-height:1.2;
        margin-bottom:12px;
    }
                
    .selector-title{

    font-size:26px;

    font-weight:bold;

    color:#222;

    font-family:Georgia;

    line-height:1.2;

    margin-bottom:12px;

}
                
    /* Selectbox container */
div[data-baseweb="select"] > div {

    background-color: #FCFAF2 !important;

    border: 2px solid #556B2F !important;

    border-radius: 12px !important;

    font-family: Georgia !important;

    font-size: 18px !important;

    color: #222 !important;

}

/* Selected value */
div[data-baseweb="select"] span {

    font-family: Georgia !important;

    font-size: 18px !important;

    color: #222 !important;

}

/* Dropdown arrow */
div[data-baseweb="select"] svg {

    color: #556B2F !important;

}
                
    ul[role="listbox"] {

    font-family: Georgia !important;

    font-size: 17px !important;

    background-color: #FCFAF2 !important;

}

ul[role="listbox"] li {

    color: #222 !important;

    padding: 10px !important;

}

ul[role="listbox"] li:hover {

    background-color: #E8F0E6 !important;

}

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="title"><h1 style="font-family:Montserrat;font-size:70px;">IPL AI Detective</h1></div>',
        unsafe_allow_html=True
    )

        # ==========================================================
    # LOAD MATCHS FROM CSV
    # ==========================================================

    seasons = get_all_seasons()

    left, right = st.columns(2)

    with left:

        st.markdown(
        """
        <div class="selector-title">
            Select IPL Season
        </div>
        """,
        unsafe_allow_html=True
    )

        season = st.selectbox(

        "",

        seasons,

        label_visibility="collapsed"

    )

    matches_df = get_matches(season)

    with right:

        st.markdown(
        """
        <div class="selector-title">
            Select Match
        </div>
        """,
        unsafe_allow_html=True
    )

        selected_match_name = st.selectbox(

        "",

        matches_df["display_name"],

        label_visibility="collapsed"

    )

# ----------------------------------------
# Get the selected row
# ----------------------------------------

    selected_row = matches_df[
    matches_df["display_name"] == selected_match_name
].iloc[0]

    match_id = selected_row["match_id"]

    selected_match = get_match_details(match_id)

    from data.loader import get_match_deliveries
    from match_aura.aura_engine import MatchAuraEngine

    deliveries = get_match_deliveries(match_id)
    selected_match["deliveries"] = deliveries

    engine = MatchAuraEngine(deliveries)
    aura = engine.generate()

    st.write("")

    st.markdown(
    '<div class="section-heading">📂 Match Dossier</div>',
    unsafe_allow_html=True
)

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
        "🏆 Winner",
        selected_match["winner"]
    )

    with c2:

        st.metric(
        "⭐ Player of Match",
        selected_match["player_of_match"]
    )

    with c3:

        st.metric(
        "🏟 Venue",
        selected_match["venue"]
    )

    with c4:

        st.metric(
        "📅 Date",
        str(selected_match["date"])
    )

    st.write("")

    c5, c6 = st.columns(2)

    with c5:

        st.info(
        f"""
**🪙 Toss**

{selected_match["toss"]}
"""
    )

    with c6:

        st.success(
        f"""
**🏏 Match**

{selected_match["match"]}
"""
    )

    st.write("")

    left, right = st.columns([3, 1])

    with left:

        st.success(
        f"""
### 🟢 CASE OPENED

**Match:** {selected_match["match"]}

**Winner:** {selected_match["winner"]}

**Investigation Status:** Ready
"""
    )

    with right:

        st.metric(
        "Evidence",
        "Pending",
        "📂"
    )

    st.markdown(
    '<div class="section-heading">🤖 AI Investigation</div>',
    unsafe_allow_html=True
)

    st.info(
    "The AI Detective will automatically analyze the selected match using the ball-by-ball dataset."
)

    solve = st.button(
    "🕵 Solve The Case",
    use_container_width=True,
    type="primary"
)

    if solve:

        progress = st.progress(0)
        status = st.empty()

        steps = [
        "🕵 Collecting match evidence...",
        "📊 Loading ball-by-ball data...",
        "🔥 Detecting momentum...",
        "📈 Computing match analytics...",
        "🧠 Building case file...",
        "🤖 Consulting AI Detective...",
        "⚖ Writing final verdict..."
    ]

        for i, step in enumerate(steps):
            status.info(step)
            progress.progress(int((i + 1) * 100 / len(steps)))
            time.sleep(0.15)

        progress.empty()
        status.success("✅ Investigation Complete!")

        deliveries = get_match_deliveries(match_id)

        if deliveries.empty:
            st.error("No ball-by-ball data found for this match.")
            st.stop()

    # Temporary values.
    # We'll replace these in the next step using Match Aura analytics.
        selected_match["powerplay"] = ""
        selected_match["middleOvers"] = ""
        selected_match["deathOvers"] = ""

        if not selected_match.get("result"):
            selected_match["result"] = (
            f"{selected_match['winner']} won the match"
        )

        try:

            with st.spinner("🧠 AI Detective is analyzing the match..."):

                ai_report = generate_report(selected_match)

            st.markdown(
            '<div class="section-heading">🕵 AI Detective Report</div>',
            unsafe_allow_html=True
        )

            st.markdown(
            f"""
<div class="detective-card">
    <div class="report">
        {ai_report.replace(chr(10), "<br>")}
    </div>
</div>
""",
            unsafe_allow_html=True,
        )

        except TimeoutError:

            st.error("⏳ The AI service took too long to respond. Please try again.")

            if st.button("🔄 Retry Investigation"):
                st.rerun()

        except ConnectionError:

            st.error("🔌 Unable to connect to the AI service.")

            if st.button("🔄 Retry Investigation"):
                st.rerun()

        except Exception as e:

            logger.exception("AI Detective failed")

            st.error("⚠ Unable to generate the detective report at the moment.")

            st.warning(
            """
AI Detective is temporarily unavailable.

You can still review the match dossier and statistics.
"""
        )

            if st.button("🔄 Retry Investigation"):
                st.rerun()