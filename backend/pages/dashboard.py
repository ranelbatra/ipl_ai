import streamlit as st

from data.loader import *


def show_dashboard():
    st.markdown("""
    <style>

    .card{
    background:#E8F0E6;
    border-radius:22px;
    padding:18px;
    text-align:center;

    width:100%;
max-width:260px;
margin:15px auto 0 auto;   
    min-height:280px;     

    margin-top:15px;      

    box-shadow:0 8px 20px rgba(0,0,0,.08);
    transition:.3s;
}

    .card:hover{
        transform: translateY(-8px);
        box-shadow: 0 18px 35px rgba(0,0,0,.15);
    }

    .icon{
        font-size:50px;
        color:#6d667c;
        margin-bottom:15px;
    }

    .number{
        font-size:30px;
        font-weight:bold;
        color:#1f2937;
        font-family:'Montserrat';
    }

    .label{
        font-size:25px;
        color:#6b7280;
        font-family:'Montserrat';
    }

    </style>
    """, unsafe_allow_html=True)

    col7, col8 = st.columns([3, 1])

    with col7:
        st.markdown(
            """
            <h1 style="font-family:'Montserrat'; font-size:75px;">
            IPL Analytics Dashboard
            </h1>
            """,
            unsafe_allow_html=True
        )

    with col8:
        st.text_input("", placeholder="Search...")

    col1, col2, col3, col4 = st.columns(4, gap="small")

    with col1:
        st.markdown("""
        <div class="card">
            <div class="icon">🏏</div>
            <div class="number">1234</div>
            <div class="label">Matches</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="icon">👥</div>
            <div class="number">19</div>
            <div class="label">Teams</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="icon">🏆</div>
            <div class="number">321</div>
            <div class="label">Players</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <div class="icon">📍</div>
            <div class="number">62</div>
            <div class="label">Venues</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    left, right = st.columns([2.2,1.8], gap="small")

    with left:

        col5, col6 = st.columns(2)

        with col5:
            st.markdown("""
            <div class="card" style="padding:15px;">
                <img src="https://documents.iplt20.com/ipl/IPLHeadshot2026/2.png"
                style="
width:180px;
height:180px;
object-fit:contain;
display:block;
margin:auto;
">
                <div class="number">Virat Kohli</div>
            </div>
            """, unsafe_allow_html=True)

        with col6:
            st.markdown("""
            <div class="card" style="padding:15px;">
                <img src="https://documents.iplt20.com/playerheadshot/ipl/284/233.png"
                style="
width:180px;
height:180px;
object-fit:contain;
display:block;
margin:auto;
">
                <div class="number">AB de Villiers</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

        col10, col11 = st.columns(2)

        with col10:
            st.markdown("""
            <div class="card" style="padding:15px;">
                <img src="https://www.punjabkingsipl.in/static-assets/images/players/1201.png?v=6.68"
                style="
width:180px;
height:180px;
object-fit:contain;
display:block;
margin:auto;
">
                <div class="number">Chris Gayle</div>
            </div>
            """, unsafe_allow_html=True)

        with col11:
            st.markdown("""
            <div class="card" style="padding:15px;">
                <img src="https://documents.iplt20.com/ipl/IPLHeadshot2026/57.png"
                style="
width:180px;
height:180px;
object-fit:contain;
display:block;
margin:auto;
">
                <div class="number">MS Dhoni</div>
            </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div style="
            margin-top:205px;
            padding-left:25px;
            border-left:6px solid #556B2F;
        ">
            <div style="
                font-size:110px;
                font-weight:800;
                line-height:0.9;
                font-family:'Montserrat', sans-serif;
                color:#2F2F2F;
            ">
                Top<br>Players
            </div>
        </div>
        """, unsafe_allow_html=True)