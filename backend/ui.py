import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from ai.ai_engine import generate_report
from pages.cricket_comparison import cricket_comparison
import traceback
from pages.players import show_players
from pages.matches import show_matches
from pages.teams import show_teams
from pages.venues import show_venues
from pages.statistics import show_statistics
from pages.ai_detective import ai_detective
from pages.match_aura import match_aura
from pages.dashboard import show_dashboard
from pages.ai_match_coach import ai_match_coach
from pages.ai_assistant import ai_assistant

st.set_page_config(layout="wide")

st.balloons()

st.markdown(
     """
<style>
.stApp{
background-color: #FCFAF2;
}
</style>
""", unsafe_allow_html=True
)

selected = option_menu(
    menu_title=None,
    options=[
        "Dashboard",
        "Teams",
        "Players",
        "Matches",
        "Venues",
        "Statistics",
        "AI Detective",
        "Match Aura",
        "AI Match Coach",
        "Cricket Comparison Studio",
        "AI Cricket Assistant"
    ],
    icons=[
        "house",
        "people",
        "person-badge",
        "trophy",
        "geo-alt",
        "bar-chart",
        "robot",
        "clipboard2-check"
    ],
    orientation="horizontal",

    styles={
        "container":{
            "padding":"5!important",
            "background-color":"#E8F0E6",
        },

        "icon":{
            "color":"#556B2F",
            "font-size":"20px",
        },

        "nav-link":{
            "font-size":"18px",
            "text-align":"center",
            "margin":"5px",
            "--hover-color":"#ede1cc",
            "color":"black",
            "font-family":"Georgia",
        },

        "nav-link-selected":{
            "background-color":"#DCE8D5",
            "color":"black",
        }
    }
)

if selected == "Dashboard":

    show_dashboard()

elif selected == "Teams":

    show_teams()

elif selected == "Players":

    show_players()

elif selected == "Matches":

    show_matches()

elif selected == "Venues":

    show_venues()
                
elif selected == "Statistics":

    show_statistics()

elif selected == "AI Detective":

    ai_detective()

elif selected == "Match Aura":

    match_aura()

elif selected == "AI Match Coach":

    ai_match_coach()

elif selected == "Cricket Comparison Studio":
    cricket_comparison()

elif selected == "AI Cricket Assistant":
    ai_assistant()