import streamlit as st

from data.loader import *


def show_statistics():
    import plotly.express as px
    import pandas as pd

    st.markdown("""
    <style>

    .stat-card{
        background:#E8F0E6;
        border-radius:22px;
        padding:20px;
        text-align:center;
        margin-top:20px;
        min-height:180px;
        box-shadow:0 8px 20px rgba(0,0,0,.08);
        transition:.3s;
    }

    .stat-card:hover{
        transform:translateY(-6px);
        box-shadow:0 18px 35px rgba(0,0,0,.15);
    }

    .stat-title{
        font-size:22px;
        font-weight:bold;
        color:#2F2F2F;
        font-family:Georgia;
    }

    .stat-number{
        font-size:45px;
        font-weight:bold;
        color:#556B2F;
        margin-top:12px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style="font-size:70px;font-family:Montserrat;">
    IPL Statistics
    </h1>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-title">Matches</div>
            <div class="stat-number">1095</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-title">Teams</div>
            <div class="stat-number">10</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-title">Venues</div>
            <div class="stat-number">35</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-title">Seasons</div>
            <div class="stat-number">18</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    season_df = pd.DataFrame({
        "Season": [
            "2008","2009","2010","2011","2012","2013",
            "2014","2015","2016","2017","2018","2019",
            "2020","2021","2022","2023","2024","2025"
        ],
        "Matches": [
            58,57,60,74,76,76,
            60,59,60,59,60,60,
            60,60,74,74,74,74
        ]
    })

    titles = pd.DataFrame({
        "Team": [
            "Mumbai Indians",
            "CSK",
            "KKR",
            "RCB",
            "SRH",
            "RR",
            "GT",
            "DC",
            "PBKS",
            "LSG"
        ],
        "Titles": [
            5,
            5,
            3,
            1,
            1,
            1,
            1,
            0,
            0,
            0
        ]
    })

    venues = pd.DataFrame({
        "Venue": [
            "Wankhede",
            "Chinnaswamy",
            "Eden Gardens",
            "Chepauk",
            "Arun Jaitley",
            "Hyderabad",
            "Jaipur",
            "Ahmedabad",
            "Lucknow",
            "Mullanpur"
        ],
        "Matches": [
            115,
            95,
            93,
            81,
            84,
            71,
            57,
            35,
            21,
            16
        ]
    })

    fig1 = px.bar(
        season_df,
        x="Season",
        y="Matches",
        color="Matches",
        title="Matches Played Per Season"
    )

    fig2 = px.bar(
        titles,
        x="Titles",
        y="Team",
        orientation="h",
        color="Titles",
        title="IPL Titles by Team"
    )

    fig3 = px.bar(
        venues,
        x="Venue",
        y="Matches",
        color="Matches",
        title="Matches Hosted by Venue"
    )

    fig4 = px.pie(
        titles,
        values="Titles",
        names="Team",
        title="Distribution of IPL Titles"
    )

    left, right = st.columns(2)

    with left:
        st.plotly_chart(fig1, use_container_width=True)

    with right:
        st.plotly_chart(fig2, use_container_width=True)

    left, right = st.columns(2)

    with left:
        st.plotly_chart(fig3, use_container_width=True)

    with right:
        st.plotly_chart(fig4, use_container_width=True)
