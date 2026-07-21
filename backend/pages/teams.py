import streamlit as st

from data.loader import *


def show_teams():
    st.markdown("""
    <style>

    .team-card{
        background:#E8F0E6;
        border-radius:22px;
        padding:20px;
        text-align:center;
        margin-top:30px;
        box-shadow:0 8px 25px rgba(0,0,0,.08);
        transition:all .3s ease;
        min-height:360px;
    }

    .team-card:hover{
        transform:translateY(-8px);
        box-shadow:0 18px 35px rgba(0,0,0,.15);
    }

    .team-img{
        width:180px;
        height:180px;
        object-fit:contain;
        margin:auto;
        display:block;
        margin-bottom:8px;
    }

    .team-name{
        font-size:28px;
        font-weight:bold;
        color:#222;
        font-family:Georgia;
        margin-bottom:10px;
        line-height:1.2;
    }

    .team-details{
        font-size:17px;
        color:#555;
        font-family:Montserrat;
        line-height:1.8;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style="font-family:Montserrat;font-size:70px;">
    IPL Teams
    </h1>
    """, unsafe_allow_html=True)

    teams = [

        {
            "name":"Mumbai Indians",
            "captain":"Hardik Pandya",
            "titles":"5",
            "home":"Wankhede Stadium, Mumbai",
            "image":"https://static.vecteezy.com/system/resources/previews/075/244/951/non_2x/mumbai-indians-logo-mi-logo-icon-on-transparent-background-free-png.png"
        },

        {
            "name":"Chennai Super Kings",
            "captain":"Ruturaj Gaikwad",
            "titles":"5",
            "home":"M. A. Chidambaram Stadium, Chennai",
            "image":"https://static.vecteezy.com/system/resources/previews/075/244/942/non_2x/chennai-super-kings-logo-csk-logo-icon-on-transparent-background-free-png.png"
        },

        {
            "name":"Lucknow Super Giants",
            "captain":"Rishabh Pant",
            "titles":"0",
            "home":"BRSABV Ekana Cricket Stadium, Lucknow",
            "image":"https://static.vecteezy.com/system/resources/previews/075/244/945/non_2x/lucknow-super-giants-logo-lsg-logo-icon-on-transparent-background-free-png.png"
        },

        {
            "name":"Gujrat Titans",
            "captain":"Shubman Gill",
            "titles":"1",
            "home":"Narendra Modi Stadium, Ahmedabad",
            "image":"https://static.vecteezy.com/system/resources/previews/075/244/947/non_2x/gujarat-titans-logo-gt-logo-icon-on-transparent-background-free-png.png"
        },

        {
            "name":"Royal Challengers Bengaluru",
            "captain":"Rajat Patidar",
            "titles":"2",
            "home":"M. Chinnaswamy Stadium, Bengaluru",
            "image":"https://static.vecteezy.com/system/resources/previews/075/244/946/non_2x/royal-challengers-bengaluru-logo-rcb-logo-icon-on-transparent-background-free-png.png"
        },

        {
            "name":"Kolkata Knight Riders",
            "captain":"Ajinkya Rahane",
            "titles":"3",
            "home":"Eden Gardens, Kolkata",
            "image":"https://static.vecteezy.com/system/resources/previews/075/244/950/non_2x/kolkata-knight-riders-logo-kkr-logo-icon-on-transparent-background-free-png.png"
        },

        {
            "name":"Sunrisers Hyderabad",
            "captain":"Pat Cummins",
            "titles":"1",
            "home":"Rajiv Gandhi International Stadium, Hyderabad",
            "image":"https://static.vecteezy.com/system/resources/previews/075/244/941/non_2x/sunrisers-hyderabad-logo-srh-logo-icon-on-transparent-background-free-png.png"
        },

        {
            "name":"Rajasthan Royals",
            "captain":"Riyan Parag",
            "titles":"1",
            "home":"Sawai Mansingh Stadium, Jaipur",
            "image":"https://static.vecteezy.com/system/resources/previews/075/244/952/non_2x/rajasthan-royals-logo-rr-logo-icon-on-transparent-background-free-png.png"
        },

        {
            "name":"Delhi Capitals",
            "captain":"Axar Patel",
            "titles":"0",
            "home":"Arun Jaitley Stadium, New Delhi",
            "image":"https://static.vecteezy.com/system/resources/previews/075/252/975/non_2x/delhi-capitals-logo-dc-logo-icon-on-transparent-background-free-png.png"
        },

        {
            "name":"Punjab Kings",
            "captain":"Shreyas Iyer",
            "titles":"0",
            "home":"Maharaja Yadavindra Singh Stadium, Mullanpur",
            "image":"https://static.vecteezy.com/system/resources/previews/075/244/949/non_2x/punjab-kings-logo-pbks-logo-icon-on-transparent-background-free-png.png"
        }

    ]

    for i in range(0, len(teams), 4):

        cols = st.columns(4)

        for col, team in zip(cols, teams[i:i+4]):

            with col:

                st.markdown(f"""
<div class="team-card">

<img class="team-img" src="{team['image']}" />

<div class="team-name">
{team['name']}
</div>

<div class="team-details">

<b>Captain:</b> {team['captain']}<br>
<b>Titles:</b> {team['titles']}<br>
<b>Home:</b> {team['home']}

</div>

</div>
""", unsafe_allow_html=True)