import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

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
        "AI Detective"
    ],
    icons=[
        "house",
        "people",
        "person-badge",
        "trophy",
        "geo-alt",
        "bar-chart",
        "robot"
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

    st.markdown("""
    <style>

    .card {
        background: #E8F0E6;
        border-radius: 22px;
        padding: 30px;
        text-align: center;
        margin-top: 100px;
        width: 275px;
        box-shadow: 0 8px 25px rgba(0,0,0,.08);
        transition: all .3s ease;
        min-height: 220px;
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
            <div class="label">Man of the Match</div>
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

    left, right = st.columns([3, 2], gap="large")

    with left:

        col5, col6 = st.columns(2)

        with col5:
            st.markdown("""
            <div class="card" style="padding:10px;margin-top:10px;">
                <img src="https://documents.iplt20.com/ipl/IPLHeadshot2026/2.png"
                style="width:100%;">
                <div class="number">Virat Kohli</div>
            </div>
            """, unsafe_allow_html=True)

        with col6:
            st.markdown("""
            <div class="card" style="padding:10px;margin-top:10px;">
                <img src="https://documents.iplt20.com/playerheadshot/ipl/284/233.png"
                style="width:100%;">
                <div class="number">AB de Villiers</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")

        col10, col11 = st.columns(2)

        with col10:
            st.markdown("""
            <div class="card" style="padding:10px;margin-top:5px;">
                <img src="https://www.punjabkingsipl.in/static-assets/images/players/1201.png?v=6.68"
                style="width:100%;">
                <div class="number">Chris Gayle</div>
            </div>
            """, unsafe_allow_html=True)

        with col11:
            st.markdown("""
            <div class="card" style="padding:10px;margin-top:5px;">
                <img src="https://documents.iplt20.com/ipl/IPLHeadshot2026/57.png"
                style="width:100%;">
                <div class="number">MS Dhoni</div>
            </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div style="
            margin-top:255px;
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

elif selected == "Teams":

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

elif selected == "Players":

    st.markdown("""
    <style>

    .team-heading{
        font-size:42px;
        font-family:Georgia;
        font-weight:bold;
        color:#2F2F2F;
        margin-top:35px;
        margin-bottom:15px;
        border-left:6px solid #556B2F;
        padding-left:15px;
    }


    .scroll-container{
        display:flex;
        overflow-x:auto;
        gap:22px;
        padding:15px 5px 20px 5px;
    }


    .scroll-container::-webkit-scrollbar{
        height:10px;
    }


    .scroll-container::-webkit-scrollbar-thumb{
        background:#556B2F;
        border-radius:20px;
    }


    .player-card{

        min-width:260px;
        max-width:260px;

        background:#E8F0E6;

        border-radius:22px;

        padding:18px;

        text-align:center;

        box-shadow:0 8px 20px rgba(0,0,0,.08);

        transition:.3s;

    }


    .player-card:hover{

        transform:translateY(-8px);

        box-shadow:0 18px 35px rgba(0,0,0,.15);

    }


    .player-img{

        width:170px;
        height:170px;

        object-fit:contain;

        margin:auto;

        display:block;

    }


    .player-name{

        font-size:27px;

        font-weight:bold;

        font-family:Georgia;

        color:#222;

        margin-top:5px;

        margin-bottom:5px;

    }


    .player-info{

        font-size:17px;

        font-family:Montserrat;

        color:#555;

        line-height:1.6;

    }


    .badge{

        display:inline-block;

        background:#556B2F;

        color:white;

        padding:6px 14px;

        border-radius:20px;

        margin-top:10px;

        font-size:14px;

    }


    </style>
    """, unsafe_allow_html=True)


    st.markdown("""
    <h1 style="font-size:65px;font-family:Montserrat;">
    Man of the Match Winners
    </h1>
    """, unsafe_allow_html=True)


    players = [

        {
            "name":"Virat Kohli",
            "team":"RCB",
            "role":"Batter",
            "age":"37 Years",
            "image":"https://documents.iplt20.com/ipl/IPLHeadshot2026/2.png"
        },


        {
            "name":"KL Rahul",
            "team":"DC",
            "role":"Wicket Keeper Batter",
            "age":"34 Years",
            "image":"https://documents.iplt20.com/ipl/IPLHeadshot2026/1125.png"
        },


        {
            "name":"Ishan Kishan",
            "team":"SRH",
            "role":"Wicket Keeper Batter",
            "age":"28 Years",
            "image":"https://documents.iplt20.com/ipl/IPLHeadshot2026/164.png"
        },


        {
            "name":"Shardul Thakur",
            "team":"MI",
            "role":"All-Rounder",
            "age":"34 Years",
            "image":"https://documents.iplt20.com/ipl/IPLHeadshot2026/105.png"
        },


        {
            "name":"Nandre Burger",
            "team":"RR",
            "role":"Fast Bowler",
            "age":"31 Years",
            "image":"https://documents.iplt20.com/ipl/IPLHeadshot2026/1000.png"
        }

    ]


    html = """
    <div class="scroll-container">
    """

    for player in players:

        html += f"""
        <div class="player-card">

            <img class="player-img" src="{player['image']}">

            <div class="player-name">
                {player['name']}
            </div>

            <div class="player-info">
                {player['role']} <br>
                Age: {player['age']}
            </div>

            <div class="badge">
                🏏 {player['team']}
            </div>

        </div>
        """

    html += """
    </div>
    """

    st.components.v1.html(html, height=600, scrolling=True)


elif selected == "Matches":
    st.title("🏆 IPL Matches")

elif selected == "Venues":
    st.title("📍 IPL Venues")

elif selected == "Statistics":
    st.title("📊 IPL Statistics")

elif selected == "AI Detective":
    st.title("🕵 AI Detective")