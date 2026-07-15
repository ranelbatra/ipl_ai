import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from ai.ai_engine import generate_report
import traceback

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
    <h1 style="font-size:65px;font-family:Montserrat;">
    IPL Players
    </h1>
    """, unsafe_allow_html=True)

    teams = {
        "Chennai Super Kings": [

        {
            "name": "Ruturaj Gaikwad",
            "role": "Captain",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/102.png"
        },

        {
            "name": "MS Dhoni",
            "role": "Wicket Keeper | Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/57.png"
        },

        {
            "name": "Sanju Samson",
            "role": "Wicket Keeper | Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/190.png"
        },

        {
            "name": "Sarfaraz Khan",
            "role": "Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/139.png"
        },

        {
            "name": "Ayush Mhatre",
            "role": "Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3497.png"
        },

        {
            "name": "Urvil Patel",
            "role": "Wicket Keeper | Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1486.png"
        },

        {
            "name": "Dewald Brevis",
            "role": "Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/797.png"
        },

        {
            "name": "Matthew Short",
            "role": "Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2032.png"
        },

        {
            "name": "Kartik Sharma",
            "role": "Wicket Keeper | Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4540.png"
        },

        {
            "name": "Shivam Dube",
            "role": "All-Rounder",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/211.png"
        },

        {
            "name": "Jamie Overton",
            "role": "All-Rounder",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1216.png"
        },

        {
            "name": "Ajay Mandal",
            "role": "All-Rounder",
            "image": "https://www.iplbetonline.in/wp-content/uploads/2023/04/1931.png"
        },

        {
            "name": "Anshul Kamboj",
            "role": "All-Rounder",
            "image": "https://static.toiimg.com/photo/120896469.cms"
        },

        {
            "name": "Prashant Veer",
            "role": "All-Rounder",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4541.png"
        },

        {
            "name": "Zakary Foulkes",
            "role": "All-Rounder",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3493.png"
        },

        {
            "name": "Aman Khan",
            "role": "All-Rounder",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/979.png"
        },

        {
            "name": "Matheesha Pathirana",
            "role": "Bowler",
            "image": "https://static.toiimg.com/photo/120896430.cms"
        },

        {
            "name": "Shreyas Gopal",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/970.png"
        },

        {
            "name": "Syed Khaleel Ahmed",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/8.png"
        },

        {
            "name": "Mukesh Choudhary",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4541.png"
        },

        {
            "name": "Anshul Kamboj",
            "role": "Bowler",
            "image": "https://static.toiimg.com/photo/120896469.cms"
        },

        {
            "name": " Nathan Ellis",
            "role": "Bowler",
            "image": "https://static.toiimg.com/photo/120896426.cms"
        },

        {
            "name": "Noor Ahmad",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/975.png"
        },

        {
            "name": "Ramakrishna Ghosh",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3559.png"
        },
        
        {
            "name": "Akeal Hosein",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/722.png"
        },

        {
            "name": "Rahul Chahar",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/171.png"
        },

        {
            "name": "Matt Henry",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/71.png"
        },
    ],

    "Delhi Capitals": [

        {
            "name": "Axar Patel",
            "role": "Captain",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/110.png"
        },

        {
            "name": "Prithvi Shaw",
            "role": "Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/51.png"
        },

        {
            "name": "Tristan Stubbs",
            "role": "Wicket Keeper | Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1017.png"
        },

        {
            "name": "Abhishek Porel",
            "role": "Wicket Keeper | Batter",
            "image": "https://static.toiimg.com/photo/120896578.cms"
        },

        {
            "name": "Harry Brook",
            "role": "Wicket Keeper | Batter",
            "image": "https://www.delhicapitals.in/static-assets/images/players/ipl/66374.png?v=2.58"
        },

        {
            "name": "Jake Fraser-McGurk",
            "role": "Wicket Keeper | Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2025/3115.png"
        },

        {
            "name": "Shai Hope",
            "role": "Wicket Keeper | Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2024/268.png"
        },

        {
            "name": "Sumit Kumar",
            "role": "All-Rounder",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2024/1535.png"
        },

        {
            "name": "Lalit Yadav",
            "role": "All-Rounder",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2024/538.png"
        },
        
        {
            "name": "Ashutosh Sharma",
            "role": "All-Rounder",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3109.png"
        },

        {
            "name": "Vipraj Nigam",
            "role": "All-Rounder",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3560.png"
        },
        
        {
            "name": "Auqib Nabi Dar",
            "role": "All-Rounder",
            "image": "https://www.delhicapitals.in/static-assets/images/players/ipl/70172.png?v=2.58"
        },

        {
            "name": "Madhav Tiwari",
            "role": "All-Rounder",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4542.png"
        },
        
        {
            "name": "Tripurana Vijay",
            "role": "All-Rounder",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3563.png"
        },

        {
            "name": "Kuldeep Yadav",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/14.png"
        },

        {
            "name": "Mukesh Kumar",
            "role": "Bowler",
            "image": "https://static.toiimg.com/photo/120896536.cms"
        },

        {
            "name": "Dushmantha Chameera",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/608.png"
        },

        {
            "name": "T Natarajan",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/224.png"
        },

        {
            "name": "Mitchell Starc",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/31.png"
        },

        {
            "name": "Lungi Ngidi",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/99.png"
        },

        {
            "name": "Kyle Jamieson",
            "role": "Bowler",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/382.png"
        },

        {
            "name": "Karun Nair",
            "role": "Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/131.png"
        },

        {
            "name": "Sameer Rizvi",
            "role": "Wicket Keeper | Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1229.png"
        },

        {
            "name": "Pathum Nissanka",
            "role": "Wicket Keeper | Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/618.png"
        },

        {
            "name": "Nitish Rana",
            "role": "Wicket Keeper | Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/148.png"
        },

        {
            "name": "David Miller",
            "role": "Wicket Keeper | Batter",
            "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/128.png"
        }

    ],
    
    "Gujarat Titans": [

    {
        "name": "Shubman Gill",
        "role": "Captain",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/62.png"
    },

    {
        "name": "Shahrukh Khan",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/590.png"
    },

    {
        "name": "Sai Sudharsan",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/976.png"
    },

    {
        "name": "Nishant Sindhu",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/791.png"
    },

    {
        "name": "Rashid Khan",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/218.png"
    },

    {
        "name": "Manav Suthar",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2443.png"
    },

    {
        "name": "Rahul Tewatia",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/120.png"
    },

    {
        "name": "Washington Sundar",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/20.png"
    },

    {
        "name": "Arshad Khan",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/988.png"
    },

    {
        "name": "R Sai Kishore",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/544.png"
    },

    {
        "name": "Jason Holder",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/263.png"
    },

    {
        "name": "Anuj Rawat",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/534.png"
    },

    {
        "name": "Jos Buttler",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/151.png"
    },

    {
        "name": "Kumar Kushagra",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3101.png"
    },

    {
        "name": "Glenn Phillips",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/635.png"
    },

    {
        "name": "Gurnoor Brar",
        "role": "Bowler",
        "image": "https://www.gujarattitansipl.com/static-assets/images/players/90572.png?v=6.76"
    },

    {
        "name": "Mohammed Siraj",
        "role": "Bowler",
        "image": "https://www.gujarattitansipl.com/static-assets/images/players/65799.png?v=6.76"
    },

    {
        "name": "Prasidh Krishna",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/150.png"
    },

    {
        "name": "Kagiso Rabada",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/116.png"
    },

    {
        "name": "Jayant Yadav",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/165.png"
    },

    {
        "name": "Ishant Sharma",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/50.png"
    },

    {
        "name": "Ashok Sharma",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/980.png"
    },

    {
        "name": "Luke Wood",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3116.png"
    },

    {
        "name": "Kulwant Khejroliya",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/204.png"
    }

],

    "Royal Challengers Bengaluru": [

    {
        "name": "Rajat Patidar",
        "role": "Captain",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/597.png"
    },

    {
        "name": "Virat Kohli",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2.png"
    },

    {
        "name": "Tim David",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/636.png"
    },

    {
        "name": "Devdutt Padikkal",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/200.png"
    },

    {
        "name": "Jacob Bethell",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/869.png"
    },

    {
        "name": "Krunal Pandya",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/17.png"
    },

    {
        "name": "Venkatesh Iyer",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/584.png"
    },

    {
        "name": "Vihaan Malhotra",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4012.png"
    },

    {
        "name": "Romario Shepherd",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/371.png"
    },

    {
        "name": "Mangesh Yadav",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4554.png"
    },

    {
        "name": "Kanishk Chouhan",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4016.png"
    },

    {
        "name": "Satvik Deswal",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4555.png"
    },

    {
        "name": "Philip Salt",
        "role": "Wicket Keeper | Batter",
        "image": "https://static.toiimg.com/photo/120897590.cms"
    },

    {
        "name": "Jitesh Sharma",
        "role": "Wicket Keeper | Batter",
        "image": "https://static.toiimg.com/photo/120897607.cms"
    },

    {
        "name": "Jordan Cox",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3372.png"
    },

    {
        "name": "Abhinandan Singh",
        "role": "Bowler",
        "image": "https://static.toiimg.com/photo/120897614.cms"
    },

    {
        "name": "Josh Hazlewood",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/36.png"
    },

    {
        "name": "Rasikh Salam Dar",
        "role": "Bowler",
        "image": "https://static.toiimg.com/photo/120897584.cms"
    },

    {
        "name": "Bhuvneshwar Kumar",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/15.png"
    },

    {
        "name": "Suyash Sharma",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1932.png"
    },

    {
        "name": "Swapnil Singh",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1483.png"
    },

    {
        "name": "Jacob Duffy",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1701.png"
    },

    {
        "name": "Vicky Ostwal",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/786.png"
    },

],

    "Punjab Kings": [

    {
        "name": "Shreyas Iyer",
        "role": "Captain",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/12.png"
    },

    {
        "name": "Priyansh Arya",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3571.png"
    },

    {
        "name": "Pyla Avinash",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3573.png"
    },

    {
        "name": "Nehal Wadhera",
        "role": "Batter",
        "image": "https://www.punjabkingsipl.in/static-assets/images/players/69657.png?v=6.68"
    },

    {
        "name": "Mitchell Owen",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3870.png"
    },

    {
        "name": "Musheer Khan",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2813.png"
    },

    {
        "name": "Shashank Singh",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/191.png"
    },

    {
        "name": "Marcus Stoinis",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/23.png"
    },

    {
        "name": "Suryansh Shedge",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2146.png"
    },

    {
        "name": "Cooper Connolly",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/848.png"
    },

    {
        "name": "Azmatullah Omarzai",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1354.png"
    },

    {
        "name": "Marco Jansen",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/586.png"
    },

    {
        "name": "Praveen Dubey",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/548.png?v=1.35"
    },

    {
        "name": "Prabhsimran Singh",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/137.png"
    },

    {
        "name": "Vishnu Vinod",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/581.png"
    },

    {
        "name": "Arshdeep Singh",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/125.png"
    },

    {
        "name": "Xavier Bartlett",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3572.png"
    },

    {
        "name": "Yuzvendra Chahal",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/10.png"
    },

    {
        "name": "Lockie Ferguson",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/69.png"
    },

    {
        "name": "Harpreet Brar",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/130.png"
    },

    {
        "name": "Vijaykumar Vyshak",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2034.png"
    },

    {
        "name": "Yash Thakur",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1550.png"
    },

    {
        "name": "Ben Dwarshuis",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/632.png"
    },

    {
        "name": "Vishal Nishad",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4547.png"
    }

],

    "Kolkata Knight Riders": [

    {
        "name": "Ajinkya Rahane",
        "role": "Captain",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/44.png"
    },

    {
        "name": "Manish Pandey",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/16.png"
    },

    {
        "name": "Rovman Powell",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/329.png"
    },

    {
        "name": "Angkrish Raghuvanshi",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/787.png"
    },

    {
        "name": "Rinku Singh",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/152.png"
    },

    {
        "name": "Finn Allen",
        "role": "Batter",
        "image": "https://www.kkr.in/static-assets/images/players/66046.png?v=112.13"
    },

    {
        "name": "Rahul Tripathi",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/188.png"
    },

    {
        "name": "Sarthak Ranjan",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4203.png"
    },

    {
        "name": "Ramandeep Singh",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/991.png"
    },

    {
        "name": "Anukul Roy",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/160.png"
    },

    {
        "name": "Cameron Green",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/550.png"
    },

    {
        "name": "Sunil Narine",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/156.png"
    },

    {
        "name": "Daksh Kamra",
        "role": "Bowling All-Rounder",
        "image": "https://www.kkr.in/static-assets/images/players/137799.png?v=112.13"
    },

    {
        "name": "Tim Seifert",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/82.png"
    },

    {
        "name": "Tejasvi Dahiya",
        "role": "Wicket Keeper | Batter",
        "image": "https://www.kkr.in/static-assets/images/players/126180.png?v=112.13"
    },

    {
        "name": "Luvnith Sisodia",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2025/1009.png"
    },

    {
        "name": "Vaibhav Arora",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/583.png"
    },

    {
        "name": "Umran Malik",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/637.png"
    },

    {
        "name": "Varun Chakaravarthy",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/140.png"
    },

    {
        "name": "Prashant Solanki",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/972.png"
    },

    {
        "name": "Kartik Tyagi",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/536.png"
    },

    {
        "name": "Matheesha Pathirana",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1014.png"
    },

    {
        "name": "Blessing Muzarabani",
        "role": "Bowler",
        "image": "https://www.kkr.in/static-assets/images/players/67784.png?v=112.13"
    },

    {
        "name": "Saurabh Dubey",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1010.png"
    },

    {
        "name": "Navdeep Saini",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/207.png"
    }

],

    "Sunrisers Hyderabad": [

    {
        "name": "Pat Cummins",
        "role": "Captain",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/33.png"
    },

    {
        "name": "Travis Head",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/37.png"
    },

    {
        "name": "Smaran Ravichandran",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3752.png"
    },

    {
        "name": "Aniket Verma",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3576.png"
    },

    {
        "name": "Abhishek Sharma",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/212.png"
    },

    {
        "name": "Kamindu Mendis",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/627.png"
    },

    {
        "name": "Nitish Kumar Reddy",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1944.png"
    },

    {
        "name": "Liam Livingstone",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/183.png"
    },

    {
        "name": "Harsh Dubey",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1494.png"
    },

    {
        "name": "Shivang Kumar",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4561.png"
    },

    {
        "name": "Ishan Kishan",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/164.png"
    },

    {
        "name": "Heinrich Klaasen",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/202.png"
    },

    {
        "name": "Salil Arora",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4556.png"
    },

    {
        "name": "Eshan Malinga",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3339.png"
    },

    {
        "name": "Jaydev Unadkat",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/180.png"
    },

    {
        "name": "Harshal Patel",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/114.png"
    },

    {
        "name": "Zeeshan Ansari",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3575.png"
    },

    {
        "name": "Sakib Hussain",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3104.png"
    },

    {
        "name": "Onkar Tarmale",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4560.png"
    },

    {
        "name": "Amit Kumar",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4559.png"
    },

    {
        "name": "Praful Hinge",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4558.png"
    },

    {
        "name": "Krains Fuletra",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3575.png"
    },

    {
        "name": "Dilshan Madushanka",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1018.png?v=1.35"
    },

    {
        "name": "Gerald Coetzee",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2535.png"
    }

],

    "Rajasthan Royals": [

    {
        "name": "Riyan Parag",
        "role": "Captain",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/189.png"
    },

    {
        "name": "Shubham Dubey",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3112.png"
    },

    {
        "name": "Shimron Hetmyer",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/210.png"
    },

    {
        "name": "Yashasvi Jaiswal",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/533.png"
    },

    {
        "name": "Vaibhav Sooryavanshi",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3498.png"
    },

    {
        "name": "Aman Rao Perala",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4552.png"
    },

    {
        "name": "Dasun Shanaka",
        "role": "Batting All-Rounder",
        "image": "https://www.rajasthanroyals.com/static-assets/images/players/59067.png?v=7.93"
    },

    {
        "name": "Ravindra Jadeja",
        "role": "Bowling All-Rounder",
        "image": "https://www.rajasthanroyals.com/static-assets/images/players/3850.png?v=7.93"
    },

    {
        "name": "Dhruv Jurel",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1004.png"
    },

    {
        "name": "Lhuan-dre Pretorius",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2827.png"
    },

    {
        "name": "Donovan Ferreira",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2033.png"
    },

    {
        "name": "Ravi Singh",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4550.png"
    },

    {
        "name": "Jofra Archer",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/181.png"
    },

    {
        "name": "Nandre Burger",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2806.png"
    },

    {
        "name": "Tushar Deshpande",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/539.png"
    },

    {
        "name": "Kwena Maphaka",
        "role": "Bowler",
        "image": "https://www.rajasthanroyals.com/static-assets/images/players/90908.png?v=7.93"
    },

    {
        "name": "Sandeep Sharma",
        "role": "Bowler",
        "image": "https://www.rajasthanroyals.com/static-assets/images/players/10116.png?v=7.93"
    },

    {
        "name": "Yudhvir Singh Charak",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/587.png"
    },

    {
        "name": "Vignesh Puthur",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3566.png"
    },

    {
        "name": "Yash Raj Punja",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4553.png"
    },

    {
        "name": "Sushant Mishra",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1016.png"
    },

    {
        "name": "Ravi Bishnoi",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/520.png"
    },

    {
        "name": "Brijesh Sharma",
        "role": "Bowler",
        "image": "https://www.rajasthanroyals.com/static-assets/images/players/133689.png?v=7.93"
    },

    {
        "name": "Adam Milne",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/157.png"
    },

    {
        "name": "Kuldeep Sen",
        "role": "Bowler",
        "image": "https://www.rajasthanroyals.com/static-assets/images/players/70402.png?v=7.93"
    }

],

    "Lucknow Super Giants": [

    {
        "name": "Rishabh Pant",
        "role": "Captain",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/18.png"
    },

    {
        "name": "Himmat Singh",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/203.png"
    },

    {
        "name": "Aiden Markram",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/287.png"
    },

    {
        "name": "Akshat Raghuwanshi",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1487.png"
    },

    {
        "name": "Abdul Samad",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/525.png"
    },

    {
        "name": "Ayush Badoni",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/985.png"
    },

    {
        "name": "Arshin Kulkarni",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2788.png"
    },

    {
        "name": "Mitchell Marsh",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/40.png"
    },

    {
        "name": "George Linde",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/340.png"
    },

    {
        "name": "Shahbaz Ahmed",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/523.png"
    },

    {
        "name": "Arjun Tendulkar",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/585.png"
    },

    {
        "name": "Matthew Breetzke",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2805.png"
    },

    {
        "name": "Nicholas Pooran",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/136.png"
    },

    {
        "name": "Mukul Choudhary",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4549.png"
    },

    {
        "name": "Josh Inglis",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/647.png"
    },

    {
        "name": "Avesh Khan",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/541.png"
    },

    {
        "name": "Mohammed Shami",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/47.png"
    },

    {
        "name": "Prince Yadav",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1225.png"
    },

    {
        "name": "Mohsin Khan",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/541.png"
    },

    {
        "name": "Digvesh Singh Rathi",
        "role": "Bowler",
        "image": "https://www.lucknowsupergiants.in/static-assets/images/players/100574.png?v=14.11"
    },

    {
        "name": "Manimaran Siddharth",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2801.png"
    },

    {
        "name": "Mayank Yadav",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/987.png"
    },

    {
        "name": "Anrich Nortje",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/142.png"
    },

    {
        "name": "Naman Tiwari",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2801.png"
    }

],

    "Mumbai Indians": [

    {
        "name": "Hardik Pandya",
        "role": "Captain",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/54.png"
    },

    {
        "name": "Naman Dhir",
        "role": "Batter",
        "image": "https://static.toiimg.com/photo/120897201.cms"
    },

    {
        "name": "Rohit Sharma",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/6.png"
    },

    {
        "name": "Suryakumar Yadav",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/174.png"
    },

    {
        "name": "Tilak Varma",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/993.png"
    },

    {
        "name": "Danish Malewar",
        "role": "Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4546.png"
    },

    {
        "name": "Sherfane Rutherford",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/122.png"
    },

    {
        "name": "Will Jacks",
        "role": "Batting All-Rounder",
        "image": "https://www.mumbaiindians.com/static-assets/images/players/large/action-shots/66927.png?v=7.64&w=400"
    },

    {
        "name": "Mayank Rawat",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1228.png"
    },

    {
        "name": "Krish Bhagat",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/5034.png"
    },

    {
        "name": "Raj Bawa",
        "role": "Batting All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/781.png"
    },

    {
        "name": "Mahipal Lomror",
        "role": "Batting All-Rounder",
        "image": "https://www.mumbaiindians.com/static-assets/images/players/large/action-shots/65432.png?v=7.64&w=400"
    },

    {
        "name": "Corbin Bosch",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/1041.png"
    },

    {
        "name": "Shardul Thakur",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/105.png"
    },

    {
        "name": "Atharva Ankolekar",
        "role": "Bowling All-Rounder",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/4544.png"
    },

    {
        "name": "Robin Minz",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3103.png"
    },

    {
        "name": "Ryan Rickelton",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/743.png"
    },

    {
        "name": "Quinton de Kock",
        "role": "Wicket Keeper | Batter",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/170.png"
    },

    {
        "name": "Ruchit Ahir",
        "role": "Wicket Keeper | Batter",
        "image": "https://www.mumbaiindians.com/static-assets/images/players/large/action-shots/94913.png?v=7.64&w=400"
    },

    {
        "name": "Trent Boult",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/66.png"
    },

    {
        "name": "Ashwani Kumar",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3569.png"
    },

    {
        "name": "Jasprit Bumrah",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/9.png"
    },

    {
        "name": "Deepak Chahar",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/91.png"
    },

    {
        "name": "Mayank Markande",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/87.png"
    },

    {
        "name": "AM Ghazanfar",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/2761.png"
    },

    {
        "name": "Raghu Sharma",
        "role": "Bowler",
        "image": "https://documents.iplt20.com/ipl/IPLHeadshot2026/3869.png"
    },

    {
        "name": "Keshav Maharaj",
        "role": "Bowler",
        "image": "https://www.mumbaiindians.com/static-assets/images/players/large/action-shots/48607.png?v=7.64&w=400"
    }

]
    }

    html = """
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
    flex-shrink:0;
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

</style>
"""

    for team, players in teams.items():

        html += f"""
        <div class="team-heading">
            {team}
        </div>

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
                    {player['role']}
                </div>

            </div>
            """

        html += """
        </div>
        """

    st.components.v1.html(
        html,
        height=2500,
        scrolling=True
    )


elif selected == "Matches":

    st.markdown("""
    <h1 style="font-size:65px;font-family:Montserrat;">
    IPL Matches
    </h1>
    """, unsafe_allow_html=True)

    teams = {

        "2007/08": [

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "18-04-2008",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Chennai Super Kings",
        "date": "19-04-2008",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Rajasthan Royals",
        "date": "19-04-2008",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "20-04-2008",
        "venue": "Wankhede Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Deccan Chargers",
        "date": "20-04-2008",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Kings XI Punjab",
        "date": "21-04-2008",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Deccan Chargers vs Delhi Daredevils",
        "date": "22-04-2008",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "23-04-2008",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Deccan Chargers vs Rajasthan Royals",
        "date": "24-04-2008",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "25-04-2008",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "26-04-2008",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "26-04-2008",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Deccan Chargers",
        "date": "27-04-2008",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Daredevils",
        "date": "27-04-2008",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "28-04-2008",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "29-04-2008",
        "venue": "Eden Gardens",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Royal Challengers Bangalore",
        "date": "30-04-2008",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Deccan Chargers vs Kings XI Punjab",
        "date": "01-05-2008",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "01-05-2008",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Daredevils",
        "date": "02-05-2008",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "03-05-2008",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Deccan Chargers",
        "date": "03-05-2008",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Mumbai Indians vs Delhi Daredevils",
        "date": "04-05-2008",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "04-05-2008",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "05-05-2008",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Deccan Chargers",
        "date": "06-05-2008",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "07-05-2008",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Chennai Super Kings",
        "date": "08-05-2008",
        "venue": "Feroz Shah Kotla",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "08-05-2008",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Deccan Chargers",
        "date": "09-05-2008",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "10-05-2008",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Deccan Chargers vs Kolkata Knight Riders",
        "date": "11-05-2008",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Daredevils",
        "date": "11-05-2008",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "12-05-2008",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Daredevils",
        "date": "13-05-2008",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "14-05-2008",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Deccan Chargers",
        "date": "15-05-2008",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "16-05-2008",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "17-05-2008",
        "venue": "Feroz Shah Kotla",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "17-05-2008",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Deccan Chargers vs Mumbai Indians",
        "date": "18-05-2008",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "18-05-2008",
        "venue": "Eden Gardens",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Daredevils",
        "date": "19-05-2008",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "20-05-2008",
        "venue": "Eden Gardens",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "21-05-2008",
        "venue": "Wankhede Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "21-05-2008",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kings XI Punjab vs Deccan Chargers",
        "date": "23-05-2008",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "24-05-2008",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "24-05-2008",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Deccan Chargers vs Royal Challengers Bangalore",
        "date": "25-05-2008",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "25-05-2008",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "26-05-2008",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Deccan Chargers vs Chennai Super Kings",
        "date": "27-05-2008",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "28-05-2008",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "28-05-2008",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Delhi Daredevils vs Rajasthan Royals",
        "date": "30-05-2008",
        "venue": "Wankhede Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "31-05-2008",
        "venue": "Wankhede Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "01-06-2008",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Rajasthan Royals"
    }

],

"2009": [

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "18-04-2009",
        "venue": "Newlands",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "18-04-2009",
        "venue": "Newlands",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "19-04-2009",
        "venue": "Newlands",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Deccan Chargers vs Kolkata Knight Riders",
        "date": "19-04-2009",
        "venue": "Newlands",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "20-04-2009",
        "venue": "St George's Park",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "21-04-2009",
        "venue": "Kingsmead",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Deccan Chargers",
        "date": "22-04-2009",
        "venue": "Newlands",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Daredevils",
        "date": "23-04-2009",
        "venue": "Kingsmead",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "23-04-2009",
        "venue": "Newlands",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "24-04-2009",
        "venue": "Kingsmead",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Deccan Chargers vs Mumbai Indians",
        "date": "25-04-2009",
        "venue": "Kingsmead",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Daredevils",
        "date": "26-04-2009",
        "venue": "St George's Park",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "26-04-2009",
        "venue": "Newlands",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Deccan Chargers",
        "date": "27-04-2009",
        "venue": "Kingsmead",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "27-04-2009",
        "venue": "St George's Park",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Rajasthan Royals",
        "date": "28-04-2009",
        "venue": "SuperSport Park",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "29-04-2009",
        "venue": "Kingsmead",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "29-04-2009",
        "venue": "Kingsmead",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Deccan Chargers vs Delhi Daredevils",
        "date": "30-04-2009",
        "venue": "SuperSport Park",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "30-04-2009",
        "venue": "SuperSport Park",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "01-05-2009",
        "venue": "Buffalo Park",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "01-05-2009",
        "venue": "Kingsmead",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Deccan Chargers vs Rajasthan Royals",
        "date": "02-05-2009",
        "venue": "St George's Park",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Daredevils",
        "date": "02-05-2009",
        "venue": "New Wanderers Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "03-05-2009",
        "venue": "St George's Park",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "03-05-2009",
        "venue": "New Wanderers Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Deccan Chargers",
        "date": "04-05-2009",
        "venue": "Buffalo Park",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "05-05-2009",
        "venue": "Kingsmead",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "05-05-2009",
        "venue": "Kingsmead",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Deccan Chargers vs Mumbai Indians",
        "date": "06-05-2009",
        "venue": "SuperSport Park",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "07-05-2009",
        "venue": "SuperSport Park",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "07-05-2009",
        "venue": "SuperSport Park",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "08-05-2009",
        "venue": "Buffalo Park",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Deccan Chargers vs Kings XI Punjab",
        "date": "09-05-2009",
        "venue": "De Beers Diamond Oval",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "09-05-2009",
        "venue": "De Beers Diamond Oval",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "10-05-2009",
        "venue": "St George's Park",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "10-05-2009",
        "venue": "New Wanderers Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Deccan Chargers vs Rajasthan Royals",
        "date": "11-05-2009",
        "venue": "De Beers Diamond Oval",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "12-05-2009",
        "venue": "SuperSport Park",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "12-05-2009",
        "venue": "SuperSport Park",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Deccan Chargers vs Delhi Daredevils",
        "date": "13-05-2009",
        "venue": "Kingsmead",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "14-05-2009",
        "venue": "Kingsmead",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "14-05-2009",
        "venue": "Kingsmead",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "15-05-2009",
        "venue": "OUTsurance Oval",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "16-05-2009",
        "venue": "St George's Park",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Deccan Chargers vs Kolkata Knight Riders",
        "date": "16-05-2009",
        "venue": "New Wanderers Stadium",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Deccan Chargers vs Kings XI Punjab",
        "date": "17-05-2009",
        "venue": "New Wanderers Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Delhi Daredevils vs Rajasthan Royals",
        "date": "17-05-2009",
        "venue": "OUTsurance Oval",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "18-05-2009",
        "venue": "SuperSport Park",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Daredevils",
        "date": "19-05-2009",
        "venue": "New Wanderers Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "20-05-2009",
        "venue": "Kingsmead",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "20-05-2009",
        "venue": "Kingsmead",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "21-05-2009",
        "venue": "SuperSport Park",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Royal Challengers Bangalore vs Deccan Chargers",
        "date": "21-05-2009",
        "venue": "SuperSport Park",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Deccan Chargers",
        "date": "22-05-2009",
        "venue": "SuperSport Park",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "23-05-2009",
        "venue": "New Wanderers Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Royal Challengers Bangalore vs Deccan Chargers",
        "date": "24-05-2009",
        "venue": "New Wanderers Stadium",
        "winner": "Deccan Chargers"
    }

],

"2009/10": [

    {
        "teams": "Deccan Chargers vs Kolkata Knight Riders",
        "date": "12-03-2010",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "13-03-2010",
        "venue": "Brabourne Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Daredevils",
        "date": "13-03-2010",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "14-03-2010",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Deccan Chargers",
        "date": "14-03-2010",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Daredevils",
        "date": "15-03-2010",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "16-03-2010",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "16-03-2010",
        "venue": "Eden Gardens",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "17-03-2010",
        "venue": "Feroz Shah Kotla",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "18-03-2010",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Chennai Super Kings",
        "date": "19-03-2010",
        "venue": "Feroz Shah Kotla",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Deccan Chargers vs Kings XI Punjab",
        "date": "19-03-2010",
        "venue": "Barabati Stadium",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "20-03-2010",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "20-03-2010",
        "venue": "Brabourne Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Deccan Chargers vs Delhi Daredevils",
        "date": "21-03-2010",
        "venue": "Barabati Stadium",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "21-03-2010",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "22-03-2010",
        "venue": "Brabourne Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "23-03-2010",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "24-03-2010",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "25-03-2010",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Daredevils",
        "date": "25-03-2010",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Rajasthan Royals vs Deccan Chargers",
        "date": "26-03-2010",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "27-03-2010",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "28-03-2010",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Deccan Chargers vs Mumbai Indians",
        "date": "28-03-2010",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "29-03-2010",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "30-03-2010",
        "venue": "Brabourne Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "31-03-2010",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Rajasthan Royals",
        "date": "31-03-2010",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kolkata Knight Riders vs Deccan Chargers",
        "date": "01-04-2010",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "02-04-2010",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "03-04-2010",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Deccan Chargers",
        "date": "03-04-2010",
        "venue": "Brabourne Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "04-04-2010",
        "venue": "Eden Gardens",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Delhi Daredevils vs Royal Challengers Bangalore",
        "date": "04-04-2010",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Deccan Chargers vs Rajasthan Royals",
        "date": "05-04-2010",
        "venue": "Vidarbha Cricket Association Stadium, Jamtha",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "06-04-2010",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Kings XI Punjab",
        "date": "07-04-2010",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Daredevils",
        "date": "07-04-2010",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Deccan Chargers",
        "date": "08-04-2010",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "09-04-2010",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Deccan Chargers vs Chennai Super Kings",
        "date": "10-04-2010",
        "venue": "Vidarbha Cricket Association Stadium, Jamtha",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "10-04-2010",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "11-04-2010",
        "venue": "Feroz Shah Kotla",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "11-04-2010",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Deccan Chargers vs Royal Challengers Bangalore",
        "date": "12-04-2010",
        "venue": "Vidarbha Cricket Association Stadium, Jamtha",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Mumbai Indians vs Delhi Daredevils",
        "date": "13-04-2010",
        "venue": "Brabourne Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "13-04-2010",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "14-04-2010",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Daredevils",
        "date": "15-04-2010",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kings XI Punjab vs Deccan Chargers",
        "date": "16-04-2010",
        "venue": "Himachal Pradesh Cricket Association Stadium",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "17-04-2010",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "17-04-2010",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Chennai Super Kings",
        "date": "18-04-2010",
        "venue": "Himachal Pradesh Cricket Association Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Deccan Chargers",
        "date": "18-04-2010",
        "venue": "Feroz Shah Kotla",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "19-04-2010",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "21-04-2010",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Deccan Chargers",
        "date": "22-04-2010",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Deccan Chargers",
        "date": "24-04-2010",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "25-04-2010",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Chennai Super Kings"
    }

],

"2011": [

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "08-04-2011",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Deccan Chargers vs Rajasthan Royals",
        "date": "09-04-2011",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kochi Tuskers Kerala vs Royal Challengers Bangalore",
        "date": "09-04-2011",
        "venue": "Nehru Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "10-04-2011",
        "venue": "Feroz Shah Kotla",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Pune Warriors vs Kings XI Punjab",
        "date": "10-04-2011",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Kolkata Knight Riders vs Deccan Chargers",
        "date": "11-04-2011",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Daredevils",
        "date": "12-04-2011",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "12-04-2011",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Chennai Super Kings",
        "date": "13-04-2011",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Pune Warriors vs Kochi Tuskers Kerala",
        "date": "13-04-2011",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Deccan Chargers vs Royal Challengers Bangalore",
        "date": "14-04-2011",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "15-04-2011",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Kochi Tuskers Kerala",
        "date": "15-04-2011",
        "venue": "Wankhede Stadium",
        "winner": "Kochi Tuskers Kerala"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "16-04-2011",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Deccan Chargers vs Kings XI Punjab",
        "date": "16-04-2011",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Pune Warriors vs Delhi Daredevils",
        "date": "17-04-2011",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "17-04-2011",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kochi Tuskers Kerala vs Chennai Super Kings",
        "date": "18-04-2011",
        "venue": "Nehru Stadium",
        "winner": "Kochi Tuskers Kerala"
    },

    {
        "teams": "Delhi Daredevils vs Deccan Chargers",
        "date": "19-04-2011",
        "venue": "Feroz Shah Kotla",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Mumbai Indians vs Pune Warriors",
        "date": "20-04-2011",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Kochi Tuskers Kerala",
        "date": "20-04-2011",
        "venue": "Eden Gardens",
        "winner": "Kochi Tuskers Kerala"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "21-04-2011",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "22-04-2011",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "22-04-2011",
        "venue": "Eden Gardens",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "23-04-2011",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Deccan Chargers vs Mumbai Indians",
        "date": "24-04-2011",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rajasthan Royals vs Kochi Tuskers Kerala",
        "date": "24-04-2011",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Pune Warriors",
        "date": "25-04-2011",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Royal Challengers Bangalore",
        "date": "26-04-2011",
        "venue": "Feroz Shah Kotla",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Pune Warriors vs Chennai Super Kings",
        "date": "27-04-2011",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kochi Tuskers Kerala vs Deccan Chargers",
        "date": "27-04-2011",
        "venue": "Nehru Stadium",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "28-04-2011",
        "venue": "Feroz Shah Kotla",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "29-04-2011",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Pune Warriors",
        "date": "29-04-2011",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kochi Tuskers Kerala vs Delhi Daredevils",
        "date": "30-04-2011",
        "venue": "Nehru Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "30-04-2011",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Pune Warriors",
        "date": "01-05-2011",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Deccan Chargers",
        "date": "01-05-2011",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "02-05-2011",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Kochi Tuskers Kerala",
        "date": "02-05-2011",
        "venue": "Feroz Shah Kotla",
        "winner": "Kochi Tuskers Kerala"
    },

    {
        "teams": "Deccan Chargers vs Kolkata Knight Riders",
        "date": "03-05-2011",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "04-05-2011",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Pune Warriors vs Mumbai Indians",
        "date": "04-05-2011",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kochi Tuskers Kerala vs Kolkata Knight Riders",
        "date": "05-05-2011",
        "venue": "Nehru Stadium",
        "winner": "Kochi Tuskers Kerala"
    },

    {
        "teams": "Deccan Chargers vs Delhi Daredevils",
        "date": "05-05-2011",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "06-05-2011",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "07-05-2011",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Delhi Daredevils",
        "date": "07-05-2011",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kochi Tuskers Kerala",
        "date": "08-05-2011",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kings XI Punjab vs Pune Warriors",
        "date": "08-05-2011",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "09-05-2011",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Deccan Chargers vs Pune Warriors",
        "date": "10-05-2011",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "10-05-2011",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "11-05-2011",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Daredevils",
        "date": "12-05-2011",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kochi Tuskers Kerala vs Kings XI Punjab",
        "date": "13-05-2011",
        "venue": "Holkar Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "14-05-2011",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Mumbai Indians vs Deccan Chargers",
        "date": "14-05-2011",
        "venue": "Wankhede Stadium",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Daredevils",
        "date": "15-05-2011",
        "venue": "Himachal Pradesh Cricket Association Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kochi Tuskers Kerala vs Rajasthan Royals",
        "date": "15-05-2011",
        "venue": "Holkar Cricket Stadium",
        "winner": "Kochi Tuskers Kerala"
    },

    {
        "teams": "Pune Warriors vs Deccan Chargers",
        "date": "16-05-2011",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "17-05-2011",
        "venue": "Himachal Pradesh Cricket Association Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Kochi Tuskers Kerala",
        "date": "18-05-2011",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Pune Warriors vs Kolkata Knight Riders",
        "date": "19-05-2011",
        "venue": "Dr DY Patil Sports Academy",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "20-05-2011",
        "venue": "Wankhede Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Deccan Chargers",
        "date": "21-05-2011",
        "venue": "Himachal Pradesh Cricket Association Stadium",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Delhi Daredevils vs Pune Warriors",
        "date": "21-05-2011",
        "venue": "Feroz Shah Kotla",
        "winner": "Draw"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "22-05-2011",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "22-05-2011",
        "venue": "Eden Gardens",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "24-05-2011",
        "venue": "Wankhede Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "25-05-2011",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "27-05-2011",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "28-05-2011",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    }

],

"2012": [

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "04-04-2012",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Daredevils",
        "date": "05-04-2012",
        "venue": "Eden Gardens",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Pune Warriors",
        "date": "06-04-2012",
        "venue": "Wankhede Stadium",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Rajasthan Royals vs Kings XI Punjab",
        "date": "06-04-2012",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Daredevils",
        "date": "07-04-2012",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Deccan Chargers vs Chennai Super Kings",
        "date": "07-04-2012",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "08-04-2012",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Pune Warriors vs Kings XI Punjab",
        "date": "08-04-2012",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Deccan Chargers vs Mumbai Indians",
        "date": "09-04-2012",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "10-04-2012",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Chennai Super Kings",
        "date": "10-04-2012",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "11-04-2012",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "12-04-2012",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Pune Warriors",
        "date": "12-04-2012",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "13-04-2012",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Pune Warriors vs Chennai Super Kings",
        "date": "14-04-2012",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "15-04-2012",
        "venue": "Eden Gardens",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "15-04-2012",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Delhi Daredevils",
        "date": "16-04-2012",
        "venue": "Wankhede Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Rajasthan Royals vs Deccan Chargers",
        "date": "17-04-2012",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Pune Warriors",
        "date": "17-04-2012",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "18-04-2012",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Deccan Chargers",
        "date": "19-04-2012",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Chennai Super Kings vs Pune Warriors",
        "date": "19-04-2012",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "20-04-2012",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "21-04-2012",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Pune Warriors",
        "date": "21-04-2012",
        "venue": "Feroz Shah Kotla",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "22-04-2012",
        "venue": "Wankhede Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Deccan Chargers vs Kolkata Knight Riders",
        "date": "22-04-2012",
        "venue": "Barabati Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "23-04-2012",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Pune Warriors vs Delhi Daredevils",
        "date": "24-04-2012",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "25-04-2012",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Pune Warriors vs Deccan Chargers",
        "date": "26-04-2012",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "27-04-2012",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "28-04-2012",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "28-04-2012",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Rajasthan Royals",
        "date": "29-04-2012",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Deccan Chargers",
        "date": "29-04-2012",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "30-04-2012",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Deccan Chargers vs Pune Warriors",
        "date": "01-05-2012",
        "venue": "Barabati Stadium",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Daredevils",
        "date": "01-05-2012",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "02-05-2012",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Pune Warriors vs Mumbai Indians",
        "date": "03-05-2012",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Deccan Chargers",
        "date": "04-05-2012",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Pune Warriors",
        "date": "05-05-2012",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "05-05-2012",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "06-05-2012",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Deccan Chargers",
        "date": "06-05-2012",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "07-05-2012",
        "venue": "Feroz Shah Kotla",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Pune Warriors vs Rajasthan Royals",
        "date": "08-05-2012",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Deccan Chargers vs Kings XI Punjab",
        "date": "08-05-2012",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "09-05-2012",
        "venue": "Wankhede Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Deccan Chargers vs Delhi Daredevils",
        "date": "10-05-2012",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "10-05-2012",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Pune Warriors vs Royal Challengers Bangalore",
        "date": "11-05-2012",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "12-05-2012",
        "venue": "Eden Gardens",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Daredevils",
        "date": "12-05-2012",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Pune Warriors",
        "date": "13-05-2012",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Deccan Chargers",
        "date": "13-05-2012",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "14-05-2012",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "14-05-2012",
        "venue": "Eden Gardens",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "15-05-2012",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "16-05-2012",
        "venue": "Wankhede Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Chennai Super Kings",
        "date": "17-05-2012",
        "venue": "Himachal Pradesh Cricket Association Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Delhi Daredevils vs Royal Challengers Bangalore",
        "date": "17-05-2012",
        "venue": "Feroz Shah Kotla",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Deccan Chargers vs Rajasthan Royals",
        "date": "18-05-2012",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Daredevils",
        "date": "19-05-2012",
        "venue": "Himachal Pradesh Cricket Association Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Pune Warriors vs Kolkata Knight Riders",
        "date": "19-05-2012",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Deccan Chargers vs Royal Challengers Bangalore",
        "date": "20-05-2012",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Deccan Chargers"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "20-05-2012",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "22-05-2012",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "23-05-2012",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Chennai Super Kings",
        "date": "25-05-2012",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "27-05-2012",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Kolkata Knight Riders"
    }

],

"2013": [

    {
        "teams": "Kolkata Knight Riders vs Delhi Daredevils",
        "date": "03-04-2013",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "04-04-2013",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Pune Warriors",
        "date": "05-04-2013",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Delhi Daredevils vs Rajasthan Royals",
        "date": "06-04-2013",
        "venue": "Feroz Shah Kotla",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "06-04-2013",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Pune Warriors vs Kings XI Punjab",
        "date": "07-04-2013",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bangalore",
        "date": "07-04-2013",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "08-04-2013",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Delhi Daredevils",
        "date": "09-04-2013",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "09-04-2013",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kings XI Punjab vs Chennai Super Kings",
        "date": "10-04-2013",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "11-04-2013",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Pune Warriors vs Rajasthan Royals",
        "date": "11-04-2013",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Delhi Daredevils vs Sunrisers Hyderabad",
        "date": "12-04-2013",
        "venue": "Feroz Shah Kotla",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Pune Warriors",
        "date": "13-04-2013",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "13-04-2013",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "14-04-2013",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Kings XI Punjab",
        "date": "14-04-2013",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Pune Warriors",
        "date": "15-04-2013",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "16-04-2013",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Daredevils",
        "date": "16-04-2013",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Pune Warriors vs Sunrisers Hyderabad",
        "date": "17-04-2013",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "17-04-2013",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Delhi Daredevils vs Chennai Super Kings",
        "date": "18-04-2013",
        "venue": "Feroz Shah Kotla",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kings XI Punjab",
        "date": "19-04-2013",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "20-04-2013",
        "venue": "Eden Gardens",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "20-04-2013",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "21-04-2013",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kings XI Punjab vs Pune Warriors",
        "date": "21-04-2013",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "22-04-2013",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Pune Warriors",
        "date": "23-04-2013",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "23-04-2013",
        "venue": "Feroz Shah Kotla",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "24-04-2013",
        "venue": "Eden Gardens",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "25-04-2013",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "26-04-2013",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "27-04-2013",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "27-04-2013",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "28-04-2013",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Pune Warriors",
        "date": "28-04-2013",
        "venue": "Shaheed Veer Narayan Singh International Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "29-04-2013",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "29-04-2013",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Pune Warriors vs Chennai Super Kings",
        "date": "30-04-2013",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "01-05-2013",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "01-05-2013",
        "venue": "Shaheed Veer Narayan Singh International Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "02-05-2013",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Pune Warriors vs Royal Challengers Bangalore",
        "date": "02-05-2013",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "03-05-2013",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Daredevils",
        "date": "04-05-2013",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "05-05-2013",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rajasthan Royals vs Pune Warriors",
        "date": "05-05-2013",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "06-05-2013",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Daredevils",
        "date": "07-05-2013",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "07-05-2013",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "08-05-2013",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "09-05-2013",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Pune Warriors vs Kolkata Knight Riders",
        "date": "09-05-2013",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Royal Challengers Bangalore",
        "date": "10-05-2013",
        "venue": "Feroz Shah Kotla",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Pune Warriors vs Mumbai Indians",
        "date": "11-05-2013",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Sunrisers Hyderabad",
        "date": "11-05-2013",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "12-05-2013",
        "venue": "JSCA International Stadium Complex",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "12-05-2013",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "13-05-2013",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "14-05-2013",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Daredevils",
        "date": "14-05-2013",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Pune Warriors",
        "date": "15-05-2013",
        "venue": "JSCA International Stadium Complex",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "15-05-2013",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Daredevils",
        "date": "16-05-2013",
        "venue": "Himachal Pradesh Cricket Association Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rajasthan Royals",
        "date": "17-05-2013",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "18-05-2013",
        "venue": "Himachal Pradesh Cricket Association Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "18-05-2013",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Pune Warriors vs Delhi Daredevils",
        "date": "19-05-2013",
        "venue": "Subrata Roy Sahara Stadium",
        "winner": "Pune Warriors"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "19-05-2013",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "21-05-2013",
        "venue": "Feroz Shah Kotla",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "22-05-2013",
        "venue": "Feroz Shah Kotla",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "24-05-2013",
        "venue": "Eden Gardens",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "26-05-2013",
        "venue": "Eden Gardens",
        "winner": "Mumbai Indians"
    }

],

"2014": [

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "16-04-2014",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Royal Challengers Bangalore",
        "date": "17-04-2014",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "18-04-2014",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rajasthan Royals",
        "date": "18-04-2014",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "19-04-2014",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Daredevils",
        "date": "19-04-2014",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Rajasthan Royals vs Kings XI Punjab",
        "date": "20-04-2014",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Daredevils",
        "date": "21-04-2014",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Sunrisers Hyderabad",
        "date": "22-04-2014",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "23-04-2014",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "24-04-2014",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Daredevils",
        "date": "25-04-2014",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "25-04-2014",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "26-04-2014",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "26-04-2014",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "27-04-2014",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "27-04-2014",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "28-04-2014",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "29-04-2014",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "30-04-2014",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "02-05-2014",
        "venue": "JSCA International Stadium Complex",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "03-05-2014",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Rajasthan Royals",
        "date": "03-05-2014",
        "venue": "Feroz Shah Kotla",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "04-05-2014",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "05-05-2014",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Delhi Daredevils vs Chennai Super Kings",
        "date": "05-05-2014",
        "venue": "Feroz Shah Kotla",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "06-05-2014",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "07-05-2014",
        "venue": "Feroz Shah Kotla",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Chennai Super Kings",
        "date": "07-05-2014",
        "venue": "Barabati Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "08-05-2014",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "09-05-2014",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Delhi Daredevils vs Sunrisers Hyderabad",
        "date": "10-05-2014",
        "venue": "Feroz Shah Kotla",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "10-05-2014",
        "venue": "Wankhede Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "11-05-2014",
        "venue": "Barabati Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "11-05-2014",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "12-05-2014",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "13-05-2014",
        "venue": "JSCA International Stadium Complex",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Daredevils",
        "date": "13-05-2014",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kings XI Punjab",
        "date": "14-05-2014",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "14-05-2014",
        "venue": "Barabati Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Daredevils",
        "date": "15-05-2014",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "18-05-2014",
        "venue": "JSCA International Stadium Complex",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "18-05-2014",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "19-05-2014",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "19-05-2014",
        "venue": "Feroz Shah Kotla",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bangalore",
        "date": "20-05-2014",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "20-05-2014",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "21-05-2014",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "22-05-2014",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "22-05-2014",
        "venue": "JSCA International Stadium Complex",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Delhi Daredevils",
        "date": "23-05-2014",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "23-05-2014",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "24-05-2014",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "24-05-2014",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Daredevils",
        "date": "25-05-2014",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "25-05-2014",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "27-05-2014",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "28-05-2014",
        "venue": "Brabourne Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "30-05-2014",
        "venue": "Wankhede Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "01-06-2014",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Kolkata Knight Riders"
    }

],

"2015": [

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "08-04-2015",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Daredevils",
        "date": "09-04-2015",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "10-04-2015",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "11-04-2015",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "11-04-2015",
        "venue": "Eden Gardens",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Rajasthan Royals",
        "date": "12-04-2015",
        "venue": "Feroz Shah Kotla",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "12-04-2015",
        "venue": "Wankhede Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "13-04-2015",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "14-04-2015",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Daredevils",
        "date": "15-04-2015",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rajasthan Royals",
        "date": "16-04-2015",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "17-04-2015",
        "venue": "Wankhede Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Daredevils",
        "date": "18-04-2015",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "18-04-2015",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "19-04-2015",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "19-04-2015",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "20-04-2015",
        "venue": "Feroz Shah Kotla",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Kings XI Punjab",
        "date": "21-04-2015",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "22-04-2015",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "22-04-2015",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "23-04-2015",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "24-04-2015",
        "venue": "Sardar Patel Stadium, Motera",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "25-04-2015",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "25-04-2015",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Royal Challengers Bangalore",
        "date": "26-04-2015",
        "venue": "Feroz Shah Kotla",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kings XI Punjab vs Sunrisers Hyderabad",
        "date": "27-04-2015",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "28-04-2015",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "29-04-2015",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Draw"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "30-04-2015",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "01-05-2015",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "01-05-2015",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "02-05-2015",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "02-05-2015",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "03-05-2015",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Daredevils",
        "date": "03-05-2015",
        "venue": "Brabourne Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "04-05-2015",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "04-05-2015",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Delhi Daredevils",
        "date": "05-05-2015",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "06-05-2015",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Daredevils",
        "date": "07-05-2015",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "07-05-2015",
        "venue": "Brabourne Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "08-05-2015",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "09-05-2015",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Sunrisers Hyderabad",
        "date": "09-05-2015",
        "venue": "Shaheed Veer Narayan Singh International Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "10-05-2015",
        "venue": "Wankhede Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "10-05-2015",
        "venue": "MA Chidambaram Stadium, Chepauk",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kings XI Punjab",
        "date": "11-05-2015",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Delhi Daredevils vs Chennai Super Kings",
        "date": "12-05-2015",
        "venue": "Shaheed Veer Narayan Singh International Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "13-05-2015",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "14-05-2015",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bangalore",
        "date": "15-05-2015",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kings XI Punjab vs Chennai Super Kings",
        "date": "16-05-2015",
        "venue": "Punjab Cricket Association Stadium, Mohali",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "16-05-2015",
        "venue": "Brabourne Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Daredevils",
        "date": "17-05-2015",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Draw"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "17-05-2015",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "19-05-2015",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "20-05-2015",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "22-05-2015",
        "venue": "JSCA International Stadium Complex",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "24-05-2015",
        "venue": "Eden Gardens",
        "winner": "Mumbai Indians"
    }

],

"2016": [

    {
        "teams": "Mumbai Indians vs Rising Pune Supergiants",
        "date": "09-04-2016",
        "venue": "Wankhede Stadium",
        "winner": "Rising Pune Supergiants"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Daredevils",
        "date": "10-04-2016",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Gujarat Lions",
        "date": "11-04-2016",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "12-04-2016",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "13-04-2016",
        "venue": "Eden Gardens",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Gujarat Lions vs Rising Pune Supergiants",
        "date": "14-04-2016",
        "venue": "Saurashtra Cricket Association Stadium",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "15-04-2016",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "16-04-2016",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Gujarat Lions",
        "date": "16-04-2016",
        "venue": "Wankhede Stadium",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Kings XI Punjab vs Rising Pune Supergiants",
        "date": "17-04-2016",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Daredevils",
        "date": "17-04-2016",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "18-04-2016",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "19-04-2016",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "20-04-2016",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Gujarat Lions vs Sunrisers Hyderabad",
        "date": "21-04-2016",
        "venue": "Saurashtra Cricket Association Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rising Pune Supergiants vs Royal Challengers Bangalore",
        "date": "22-04-2016",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "23-04-2016",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kings XI Punjab",
        "date": "23-04-2016",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Gujarat Lions vs Royal Challengers Bangalore",
        "date": "24-04-2016",
        "venue": "Saurashtra Cricket Association Stadium",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Rising Pune Supergiants vs Kolkata Knight Riders",
        "date": "24-04-2016",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "25-04-2016",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rising Pune Supergiants",
        "date": "26-04-2016",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Rising Pune Supergiants"
    },

    {
        "teams": "Delhi Daredevils vs Gujarat Lions",
        "date": "27-04-2016",
        "venue": "Feroz Shah Kotla",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "28-04-2016",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rising Pune Supergiants vs Gujarat Lions",
        "date": "29-04-2016",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "30-04-2016",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bangalore",
        "date": "30-04-2016",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Gujarat Lions vs Kings XI Punjab",
        "date": "01-05-2016",
        "venue": "Saurashtra Cricket Association Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Rising Pune Supergiants vs Mumbai Indians",
        "date": "01-05-2016",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "02-05-2016",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Gujarat Lions vs Delhi Daredevils",
        "date": "03-05-2016",
        "venue": "Saurashtra Cricket Association Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "04-05-2016",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Rising Pune Supergiants",
        "date": "05-05-2016",
        "venue": "Feroz Shah Kotla",
        "winner": "Rising Pune Supergiants"
    },

    {
        "teams": "Sunrisers Hyderabad vs Gujarat Lions",
        "date": "06-05-2016",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rising Pune Supergiants",
        "date": "07-05-2016",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Daredevils",
        "date": "07-05-2016",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "08-05-2016",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kolkata Knight Riders vs Gujarat Lions",
        "date": "08-05-2016",
        "venue": "Eden Gardens",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "09-05-2016",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Rising Pune Supergiants vs Sunrisers Hyderabad",
        "date": "10-05-2016",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "11-05-2016",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Daredevils",
        "date": "12-05-2016",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "13-05-2016",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Gujarat Lions",
        "date": "14-05-2016",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Rising Pune Supergiants",
        "date": "14-05-2016",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Sunrisers Hyderabad",
        "date": "15-05-2016",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Delhi Daredevils",
        "date": "15-05-2016",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "16-05-2016",
        "venue": "Eden Gardens",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Rising Pune Supergiants vs Delhi Daredevils",
        "date": "17-05-2016",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Rising Pune Supergiants"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "18-05-2016",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Gujarat Lions vs Kolkata Knight Riders",
        "date": "19-05-2016",
        "venue": "Green Park",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Delhi Daredevils vs Sunrisers Hyderabad",
        "date": "20-05-2016",
        "venue": "Shaheed Veer Narayan Singh International Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Rising Pune Supergiants vs Kings XI Punjab",
        "date": "21-05-2016",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Rising Pune Supergiants"
    },

    {
        "teams": "Gujarat Lions vs Mumbai Indians",
        "date": "21-05-2016",
        "venue": "Green Park",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "22-05-2016",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Royal Challengers Bangalore",
        "date": "22-05-2016",
        "venue": "Shaheed Veer Narayan Singh International Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Gujarat Lions vs Royal Challengers Bangalore",
        "date": "24-05-2016",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "25-05-2016",
        "venue": "Feroz Shah Kotla",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Gujarat Lions vs Sunrisers Hyderabad",
        "date": "27-05-2016",
        "venue": "Feroz Shah Kotla",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "29-05-2016",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Sunrisers Hyderabad"
    }

],

"2017": [

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bangalore",
        "date": "05-04-2017",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rising Pune Supergiant vs Mumbai Indians",
        "date": "06-04-2017",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Rising Pune Supergiant"
    },

    {
        "teams": "Gujarat Lions vs Kolkata Knight Riders",
        "date": "07-04-2017",
        "venue": "Saurashtra Cricket Association Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Rising Pune Supergiant",
        "date": "08-04-2017",
        "venue": "Holkar Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Daredevils",
        "date": "08-04-2017",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Gujarat Lions",
        "date": "09-04-2017",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "09-04-2017",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "10-04-2017",
        "venue": "Holkar Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Rising Pune Supergiant vs Delhi Daredevils",
        "date": "11-04-2017",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "12-04-2017",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "13-04-2017",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "14-04-2017",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Gujarat Lions vs Rising Pune Supergiant",
        "date": "14-04-2017",
        "venue": "Saurashtra Cricket Association Stadium",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "15-04-2017",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "15-04-2017",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Gujarat Lions",
        "date": "16-04-2017",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rising Pune Supergiant",
        "date": "16-04-2017",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Rising Pune Supergiant"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "17-04-2017",
        "venue": "Feroz Shah Kotla",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kings XI Punjab",
        "date": "17-04-2017",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Gujarat Lions vs Royal Challengers Bangalore",
        "date": "18-04-2017",
        "venue": "Saurashtra Cricket Association Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Daredevils",
        "date": "19-04-2017",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "20-04-2017",
        "venue": "Holkar Cricket Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Gujarat Lions",
        "date": "21-04-2017",
        "venue": "Eden Gardens",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Mumbai Indians vs Delhi Daredevils",
        "date": "22-04-2017",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rising Pune Supergiant vs Sunrisers Hyderabad",
        "date": "22-04-2017",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Rising Pune Supergiant"
    },

    {
        "teams": "Gujarat Lions vs Kings XI Punjab",
        "date": "23-04-2017",
        "venue": "Saurashtra Cricket Association Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "23-04-2017",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Rising Pune Supergiant",
        "date": "24-04-2017",
        "venue": "Wankhede Stadium",
        "winner": "Rising Pune Supergiant"
    },

    {
        "teams": "Rising Pune Supergiant vs Kolkata Knight Riders",
        "date": "26-04-2017",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Gujarat Lions",
        "date": "27-04-2017",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Daredevils",
        "date": "28-04-2017",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Sunrisers Hyderabad",
        "date": "28-04-2017",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rising Pune Supergiant vs Royal Challengers Bangalore",
        "date": "29-04-2017",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Rising Pune Supergiant"
    },

    {
        "teams": "Gujarat Lions vs Mumbai Indians",
        "date": "29-04-2017",
        "venue": "Saurashtra Cricket Association Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Daredevils",
        "date": "30-04-2017",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "30-04-2017",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "01-05-2017",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rising Pune Supergiant vs Gujarat Lions",
        "date": "01-05-2017",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Rising Pune Supergiant"
    },

    {
        "teams": "Delhi Daredevils vs Sunrisers Hyderabad",
        "date": "02-05-2017",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kolkata Knight Riders vs Rising Pune Supergiant",
        "date": "03-05-2017",
        "venue": "Eden Gardens",
        "winner": "Rising Pune Supergiant"
    },

    {
        "teams": "Delhi Daredevils vs Gujarat Lions",
        "date": "04-05-2017",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "05-05-2017",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rising Pune Supergiant",
        "date": "06-05-2017",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Rising Pune Supergiant"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "06-05-2017",
        "venue": "Feroz Shah Kotla",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "07-05-2017",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Gujarat Lions",
        "date": "07-05-2017",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali",
        "winner": "Gujarat Lions"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "08-05-2017",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "09-05-2017",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Gujarat Lions vs Delhi Daredevils",
        "date": "10-05-2017",
        "venue": "Green Park",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "11-05-2017",
        "venue": "Wankhede Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Delhi Daredevils vs Rising Pune Supergiant",
        "date": "12-05-2017",
        "venue": "Feroz Shah Kotla",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Gujarat Lions vs Sunrisers Hyderabad",
        "date": "13-05-2017",
        "venue": "Green Park",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "13-05-2017",
        "venue": "Eden Gardens",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rising Pune Supergiant vs Kings XI Punjab",
        "date": "14-05-2017",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Rising Pune Supergiant"
    },

    {
        "teams": "Delhi Daredevils vs Royal Challengers Bangalore",
        "date": "14-05-2017",
        "venue": "Feroz Shah Kotla",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Mumbai Indians vs Rising Pune Supergiant",
        "date": "16-05-2017",
        "venue": "Wankhede Stadium",
        "winner": "Rising Pune Supergiant"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "17-05-2017",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "19-05-2017",
        "venue": "M Chinnaswamy Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Mumbai Indians vs Rising Pune Supergiant",
        "date": "21-05-2017",
        "venue": "Rajiv Gandhi International Stadium, Uppal",
        "winner": "Mumbai Indians"
    }

],

"2018": [

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "07-04-2018",
        "venue": "Wankhede Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Kings XI Punjab",
        "date": "08-04-2018",
        "venue": "Punjab Cricket Association IS Bindra Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "08-04-2018",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "09-04-2018",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "10-04-2018",
        "venue": "MA Chidambaram Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Daredevils",
        "date": "11-04-2018",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "12-04-2018",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "13-04-2018",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Mumbai Indians vs Delhi Daredevils",
        "date": "14-04-2018",
        "venue": "Wankhede Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "14-04-2018",
        "venue": "Eden Gardens",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "15-04-2018",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Chennai Super Kings",
        "date": "15-04-2018",
        "venue": "Punjab Cricket Association IS Bindra Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Daredevils",
        "date": "16-04-2018",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "17-04-2018",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "18-04-2018",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Sunrisers Hyderabad",
        "date": "19-04-2018",
        "venue": "Punjab Cricket Association IS Bindra Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "20-04-2018",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "21-04-2018",
        "venue": "Eden Gardens",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Delhi Daredevils vs Royal Challengers Bangalore",
        "date": "21-04-2018",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "22-04-2018",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "22-04-2018",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Daredevils",
        "date": "23-04-2018",
        "venue": "Arun Jaitley Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "24-04-2018",
        "venue": "Wankhede Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "25-04-2018",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kings XI Punjab",
        "date": "26-04-2018",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Delhi Daredevils vs Kolkata Knight Riders",
        "date": "27-04-2018",
        "venue": "Arun Jaitley Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "28-04-2018",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rajasthan Royals",
        "date": "29-04-2018",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "29-04-2018",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Daredevils",
        "date": "30-04-2018",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "01-05-2018",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Rajasthan Royals",
        "date": "02-05-2018",
        "venue": "Arun Jaitley Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "03-05-2018",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "04-05-2018",
        "venue": "Holkar Cricket Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "05-05-2018",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Daredevils vs Sunrisers Hyderabad",
        "date": "05-05-2018",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "06-05-2018",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rajasthan Royals vs Kings XI Punjab",
        "date": "06-05-2018",
        "venue": "Holkar Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bangalore",
        "date": "07-05-2018",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rajasthan Royals vs Kings XI Punjab",
        "date": "08-05-2018",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "09-05-2018",
        "venue": "Eden Gardens",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Daredevils vs Sunrisers Hyderabad",
        "date": "10-05-2018",
        "venue": "Arun Jaitley Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "11-05-2018",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "12-05-2018",
        "venue": "Holkar Cricket Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Royal Challengers Bangalore",
        "date": "12-05-2018",
        "venue": "Arun Jaitley Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "13-05-2018",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "13-05-2018",
        "venue": "Wankhede Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "14-05-2018",
        "venue": "Holkar Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "15-05-2018",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "16-05-2018",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "17-05-2018",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Daredevils vs Chennai Super Kings",
        "date": "18-05-2018",
        "venue": "Arun Jaitley Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "19-05-2018",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "19-05-2018",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Daredevils vs Mumbai Indians",
        "date": "20-05-2018",
        "venue": "Arun Jaitley Stadium",
        "winner": "Delhi Daredevils"
    },

    {
        "teams": "Kings XI Punjab vs Chennai Super Kings",
        "date": "20-05-2018",
        "venue": "Maharashtra Cricket Association Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "22-05-2018",
        "venue": "Wankhede Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "23-05-2018",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "25-05-2018",
        "venue": "Eden Gardens",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "27-05-2018",
        "venue": "Wankhede Stadium",
        "winner": "Chennai Super Kings"
    }

],

"2019": [

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "23-03-2019",
        "venue": "MA Chidambaram Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "24-03-2019",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Capitals vs Mumbai Indians",
        "date": "24-03-2019",
        "venue": "Wankhede Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "25-03-2019",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Delhi Capitals vs Chennai Super Kings",
        "date": "26-03-2019",
        "venue": "Arun Jaitley Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "27-03-2019",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "28-03-2019",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "29-03-2019",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "30-03-2019",
        "venue": "Punjab Cricket Association IS Bindra Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Capitals",
        "date": "30-03-2019",
        "venue": "Arun Jaitley Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bangalore",
        "date": "31-03-2019",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "31-03-2019",
        "venue": "MA Chidambaram Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Capitals",
        "date": "01-04-2019",
        "venue": "Punjab Cricket Association IS Bindra Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "02-04-2019",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "03-04-2019",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Capitals vs Sunrisers Hyderabad",
        "date": "04-04-2019",
        "venue": "Arun Jaitley Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "05-04-2019",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "06-04-2019",
        "venue": "MA Chidambaram Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "06-04-2019",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Capitals",
        "date": "07-04-2019",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "07-04-2019",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kings XI Punjab",
        "date": "08-04-2019",
        "venue": "Punjab Cricket Association IS Bindra Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "09-04-2019",
        "venue": "MA Chidambaram Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Mumbai Indians",
        "date": "10-04-2019",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "11-04-2019",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Capitals",
        "date": "12-04-2019",
        "venue": "Eden Gardens",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "13-04-2019",
        "venue": "Wankhede Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "13-04-2019",
        "venue": "Punjab Cricket Association IS Bindra Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "14-04-2019",
        "venue": "Eden Gardens",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Capitals vs Sunrisers Hyderabad",
        "date": "14-04-2019",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "15-04-2019",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "16-04-2019",
        "venue": "Punjab Cricket Association IS Bindra Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "17-04-2019",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Delhi Capitals",
        "date": "18-04-2019",
        "venue": "Arun Jaitley Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "19-04-2019",
        "venue": "Eden Gardens",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "20-04-2019",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kings XI Punjab vs Delhi Capitals",
        "date": "20-04-2019",
        "venue": "Arun Jaitley Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "21-04-2019",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "21-04-2019",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Capitals",
        "date": "22-04-2019",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "23-04-2019",
        "venue": "MA Chidambaram Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "24-04-2019",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "25-04-2019",
        "venue": "Eden Gardens",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "26-04-2019",
        "venue": "MA Chidambaram Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rajasthan Royals",
        "date": "27-04-2019",
        "venue": "Sawai Mansingh Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Delhi Capitals vs Royal Challengers Bangalore",
        "date": "28-04-2019",
        "venue": "Arun Jaitley Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "28-04-2019",
        "venue": "Eden Gardens",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kings XI Punjab",
        "date": "29-04-2019",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "30-04-2019",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Draw"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Capitals",
        "date": "01-05-2019",
        "venue": "MA Chidambaram Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "02-05-2019",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Kolkata Knight Riders",
        "date": "03-05-2019",
        "venue": "Punjab Cricket Association IS Bindra Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Capitals",
        "date": "04-05-2019",
        "venue": "Arun Jaitley Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bangalore",
        "date": "04-05-2019",
        "venue": "M.Chinnaswamy Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Kings XI Punjab",
        "date": "05-05-2019",
        "venue": "Punjab Cricket Association IS Bindra Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "05-05-2019",
        "venue": "Wankhede Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "07-05-2019",
        "venue": "MA Chidambaram Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Capitals",
        "date": "08-05-2019",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Delhi Capitals vs Chennai Super Kings",
        "date": "10-05-2019",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "12-05-2019",
        "venue": "Rajiv Gandhi International Stadium",
        "winner": "Mumbai Indians"
    }

],

"2020/21": [

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "19-09-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Capitals vs Kings XI Punjab",
        "date": "20-09-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "21-09-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "22-09-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "23-09-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Royal Challengers Bangalore",
        "date": "24-09-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Delhi Capitals vs Chennai Super Kings",
        "date": "25-09-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "26-09-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "27-09-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "28-09-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Capitals",
        "date": "29-09-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "30-09-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "01-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "02-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "03-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Capitals vs Kolkata Knight Riders",
        "date": "03-10-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Kings XI Punjab vs Chennai Super Kings",
        "date": "04-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "04-10-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Capitals vs Royal Challengers Bangalore",
        "date": "05-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "06-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "07-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kings XI Punjab",
        "date": "08-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Delhi Capitals vs Rajasthan Royals",
        "date": "09-10-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "10-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "10-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rajasthan Royals",
        "date": "11-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Delhi Capitals vs Mumbai Indians",
        "date": "11-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "12-10-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "13-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Capitals vs Rajasthan Royals",
        "date": "14-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kings XI Punjab",
        "date": "15-10-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "16-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Capitals",
        "date": "17-10-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "17-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "18-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Kings XI Punjab",
        "date": "18-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "19-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Delhi Capitals vs Kings XI Punjab",
        "date": "20-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "21-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "22-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "23-10-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Capitals",
        "date": "24-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Kings XI Punjab vs Sunrisers Hyderabad",
        "date": "24-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "25-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "25-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Kings XI Punjab",
        "date": "26-10-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Kings XI Punjab"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Capitals",
        "date": "27-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "28-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "29-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kings XI Punjab vs Rajasthan Royals",
        "date": "30-10-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "31-10-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Delhi Capitals vs Mumbai Indians",
        "date": "31-10-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kings XI Punjab vs Chennai Super Kings",
        "date": "01-11-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "01-11-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Capitals",
        "date": "02-11-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "03-11-2020",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Delhi Capitals",
        "date": "05-11-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "06-11-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Delhi Capitals vs Sunrisers Hyderabad",
        "date": "08-11-2020",
        "venue": "Sheikh Zayed Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Delhi Capitals vs Mumbai Indians",
        "date": "10-11-2020",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Mumbai Indians"
    }

],

"2021": [

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "09-04-2021",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Capitals",
        "date": "10-04-2021",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "11-04-2021",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Punjab Kings vs Rajasthan Royals",
        "date": "12-04-2021",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "13-04-2021",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "14-04-2021",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Capitals vs Rajasthan Royals",
        "date": "15-04-2021",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Punjab Kings vs Chennai Super Kings",
        "date": "16-04-2021",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "17-04-2021",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "18-04-2021",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Punjab Kings vs Delhi Capitals",
        "date": "18-04-2021",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "19-04-2021",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Delhi Capitals",
        "date": "20-04-2021",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Punjab Kings vs Sunrisers Hyderabad",
        "date": "21-04-2021",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "21-04-2021",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "22-04-2021",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Mumbai Indians vs Punjab Kings",
        "date": "23-04-2021",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "24-04-2021",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "25-04-2021",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Capitals vs Sunrisers Hyderabad",
        "date": "25-04-2021",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Punjab Kings vs Kolkata Knight Riders",
        "date": "26-04-2021",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Capitals",
        "date": "27-04-2021",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "28-04-2021",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "29-04-2021",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Capitals",
        "date": "29-04-2021",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Punjab Kings vs Royal Challengers Bangalore",
        "date": "30-04-2021",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "01-05-2021",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "02-05-2021",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Punjab Kings vs Delhi Capitals",
        "date": "02-05-2021",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "19-09-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "20-09-2021",
        "venue": "Zayed Cricket Stadium, Abu Dhabi",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Punjab Kings",
        "date": "21-09-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Capitals",
        "date": "22-09-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "23-09-2021",
        "venue": "Zayed Cricket Stadium, Abu Dhabi",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "24-09-2021",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Capitals vs Rajasthan Royals",
        "date": "25-09-2021",
        "venue": "Zayed Cricket Stadium, Abu Dhabi",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Punjab Kings vs Sunrisers Hyderabad",
        "date": "25-09-2021",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "26-09-2021",
        "venue": "Zayed Cricket Stadium, Abu Dhabi",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "26-09-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "27-09-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Delhi Capitals vs Kolkata Knight Riders",
        "date": "28-09-2021",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Punjab Kings vs Mumbai Indians",
        "date": "28-09-2021",
        "venue": "Zayed Cricket Stadium, Abu Dhabi",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "29-09-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "30-09-2021",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Punjab Kings",
        "date": "01-10-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "02-10-2021",
        "venue": "Zayed Cricket Stadium, Abu Dhabi",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Delhi Capitals",
        "date": "02-10-2021",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Punjab Kings",
        "date": "03-10-2021",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "03-10-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Capitals",
        "date": "04-10-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "05-10-2021",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bangalore",
        "date": "06-10-2021",
        "venue": "Zayed Cricket Stadium, Abu Dhabi",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Punjab Kings",
        "date": "07-10-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "07-10-2021",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "08-10-2021",
        "venue": "Zayed Cricket Stadium, Abu Dhabi",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Capitals vs Royal Challengers Bangalore",
        "date": "08-10-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Capitals vs Chennai Super Kings",
        "date": "10-10-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Kolkata Knight Riders",
        "date": "11-10-2021",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Capitals vs Kolkata Knight Riders",
        "date": "13-10-2021",
        "venue": "Sharjah Cricket Stadium",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "15-10-2021",
        "venue": "Dubai International Cricket Stadium",
        "winner": "Chennai Super Kings"
    }

],

"2022": [

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "26-03-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Delhi Capitals",
        "date": "27-03-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Punjab Kings",
        "date": "27-03-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Lucknow Super Giants vs Gujarat Titans",
        "date": "28-03-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "29-03-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "30-03-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Lucknow Super Giants",
        "date": "31-03-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Punjab Kings vs Kolkata Knight Riders",
        "date": "01-04-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "02-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Gujarat Titans vs Delhi Capitals",
        "date": "02-04-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Punjab Kings vs Chennai Super Kings",
        "date": "03-04-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Lucknow Super Giants vs Sunrisers Hyderabad",
        "date": "04-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "05-04-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "06-04-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Capitals vs Lucknow Super Giants",
        "date": "07-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Punjab Kings vs Gujarat Titans",
        "date": "08-04-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "09-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "09-04-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Capitals vs Kolkata Knight Riders",
        "date": "10-04-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Rajasthan Royals vs Lucknow Super Giants",
        "date": "10-04-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Gujarat Titans vs Sunrisers Hyderabad",
        "date": "11-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "12-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Punjab Kings vs Mumbai Indians",
        "date": "13-04-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Gujarat Titans vs Rajasthan Royals",
        "date": "14-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "15-04-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Lucknow Super Giants vs Mumbai Indians",
        "date": "16-04-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Capitals",
        "date": "16-04-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Punjab Kings vs Sunrisers Hyderabad",
        "date": "17-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Gujarat Titans",
        "date": "17-04-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "18-04-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bangalore vs Lucknow Super Giants",
        "date": "19-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Punjab Kings vs Delhi Capitals",
        "date": "20-04-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "21-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Capitals",
        "date": "22-04-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Gujarat Titans vs Kolkata Knight Riders",
        "date": "23-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "23-04-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Lucknow Super Giants vs Mumbai Indians",
        "date": "24-04-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Punjab Kings vs Chennai Super Kings",
        "date": "25-04-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bangalore",
        "date": "26-04-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Gujarat Titans",
        "date": "27-04-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Capitals",
        "date": "28-04-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Lucknow Super Giants vs Punjab Kings",
        "date": "29-04-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Royal Challengers Bangalore vs Gujarat Titans",
        "date": "30-04-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "30-04-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Lucknow Super Giants vs Delhi Capitals",
        "date": "01-05-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "01-05-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "02-05-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Gujarat Titans vs Punjab Kings",
        "date": "03-05-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Chennai Super Kings",
        "date": "04-05-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Capitals vs Sunrisers Hyderabad",
        "date": "05-05-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Mumbai Indians vs Gujarat Titans",
        "date": "06-05-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Punjab Kings vs Rajasthan Royals",
        "date": "07-05-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Lucknow Super Giants vs Kolkata Knight Riders",
        "date": "07-05-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Royal Challengers Bangalore vs Sunrisers Hyderabad",
        "date": "08-05-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Capitals",
        "date": "08-05-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "09-05-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Gujarat Titans vs Lucknow Super Giants",
        "date": "10-05-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Capitals",
        "date": "11-05-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "12-05-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Punjab Kings vs Royal Challengers Bangalore",
        "date": "13-05-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "14-05-2022",
        "venue": "Maharashtra Cricket Association Stadium, Pune",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Gujarat Titans",
        "date": "15-05-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Rajasthan Royals vs Lucknow Super Giants",
        "date": "15-05-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Delhi Capitals vs Punjab Kings",
        "date": "16-05-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "17-05-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Lucknow Super Giants vs Kolkata Knight Riders",
        "date": "18-05-2022",
        "venue": "Dr DY Patil Sports Academy, Mumbai",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Gujarat Titans vs Royal Challengers Bangalore",
        "date": "19-05-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "20-05-2022",
        "venue": "Brabourne Stadium, Mumbai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Delhi Capitals vs Mumbai Indians",
        "date": "21-05-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Punjab Kings",
        "date": "22-05-2022",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Rajasthan Royals vs Gujarat Titans",
        "date": "24-05-2022",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Royal Challengers Bangalore vs Lucknow Super Giants",
        "date": "25-05-2022",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "27-05-2022",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Rajasthan Royals vs Gujarat Titans",
        "date": "29-05-2022",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    }

],

"2023": [

    {
        "teams": "Chennai Super Kings vs Gujarat Titans",
        "date": "31-03-2023",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Punjab Kings vs Kolkata Knight Riders",
        "date": "01-04-2023",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Lucknow Super Giants vs Delhi Capitals",
        "date": "01-04-2023",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "02-04-2023",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bangalore",
        "date": "02-04-2023",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Lucknow Super Giants",
        "date": "03-04-2023",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Capitals vs Gujarat Titans",
        "date": "04-04-2023",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Punjab Kings vs Rajasthan Royals",
        "date": "05-04-2023",
        "venue": "Barsapara Cricket Stadium, Guwahati",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "06-04-2023",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Sunrisers Hyderabad vs Lucknow Super Giants",
        "date": "07-04-2023",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Capitals",
        "date": "08-04-2023",
        "venue": "Barsapara Cricket Stadium, Guwahati",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "08-04-2023",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Gujarat Titans vs Kolkata Knight Riders",
        "date": "09-04-2023",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Punjab Kings vs Sunrisers Hyderabad",
        "date": "09-04-2023",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Lucknow Super Giants",
        "date": "10-04-2023",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Delhi Capitals vs Mumbai Indians",
        "date": "11-04-2023",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "12-04-2023",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Punjab Kings vs Gujarat Titans",
        "date": "13-04-2023",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "14-04-2023",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Capitals",
        "date": "15-04-2023",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Lucknow Super Giants vs Punjab Kings",
        "date": "15-04-2023",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "16-04-2023",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Gujarat Titans vs Rajasthan Royals",
        "date": "16-04-2023",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Royal Challengers Bangalore",
        "date": "17-04-2023",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "18-04-2023",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Lucknow Super Giants vs Rajasthan Royals",
        "date": "19-04-2023",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Royal Challengers Bangalore vs Punjab Kings",
        "date": "20-04-2023",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Capitals",
        "date": "20-04-2023",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "21-04-2023",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Gujarat Titans vs Lucknow Super Giants",
        "date": "22-04-2023",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Punjab Kings vs Mumbai Indians",
        "date": "22-04-2023",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "23-04-2023",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "23-04-2023",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Capitals vs Sunrisers Hyderabad",
        "date": "24-04-2023",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Gujarat Titans vs Mumbai Indians",
        "date": "25-04-2023",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bangalore",
        "date": "26-04-2023",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "27-04-2023",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Lucknow Super Giants vs Punjab Kings",
        "date": "28-04-2023",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Kolkata Knight Riders vs Gujarat Titans",
        "date": "29-04-2023",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Capitals",
        "date": "29-04-2023",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Punjab Kings",
        "date": "30-04-2023",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "30-04-2023",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Lucknow Super Giants",
        "date": "01-05-2023",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Delhi Capitals vs Gujarat Titans",
        "date": "02-05-2023",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Lucknow Super Giants vs Chennai Super Kings",
        "date": "03-05-2023",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Draw"
    },

    {
        "teams": "Punjab Kings vs Mumbai Indians",
        "date": "03-05-2023",
        "venue": "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "04-05-2023",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Gujarat Titans",
        "date": "05-05-2023",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "06-05-2023",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Delhi Capitals",
        "date": "06-05-2023",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Gujarat Titans vs Lucknow Super Giants",
        "date": "07-05-2023",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "07-05-2023",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Punjab Kings vs Kolkata Knight Riders",
        "date": "08-05-2023",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bangalore vs Mumbai Indians",
        "date": "09-05-2023",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Capitals",
        "date": "10-05-2023",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "11-05-2023",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Gujarat Titans",
        "date": "12-05-2023",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Lucknow Super Giants",
        "date": "13-05-2023",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Punjab Kings vs Delhi Capitals",
        "date": "13-05-2023",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Royal Challengers Bangalore vs Rajasthan Royals",
        "date": "14-05-2023",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "14-05-2023",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Gujarat Titans vs Sunrisers Hyderabad",
        "date": "15-05-2023",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Lucknow Super Giants vs Mumbai Indians",
        "date": "16-05-2023",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Delhi Capitals vs Punjab Kings",
        "date": "17-05-2023",
        "venue": "Himachal Pradesh Cricket Association Stadium, Dharamsala",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bangalore",
        "date": "18-05-2023",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Royal Challengers Bangalore"
    },

    {
        "teams": "Punjab Kings vs Rajasthan Royals",
        "date": "19-05-2023",
        "venue": "Himachal Pradesh Cricket Association Stadium, Dharamsala",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Capitals",
        "date": "20-05-2023",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Lucknow Super Giants vs Kolkata Knight Riders",
        "date": "20-05-2023",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "21-05-2023",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bangalore vs Gujarat Titans",
        "date": "21-05-2023",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Chennai Super Kings vs Gujarat Titans",
        "date": "23-05-2023",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Lucknow Super Giants",
        "date": "24-05-2023",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Gujarat Titans vs Mumbai Indians",
        "date": "26-05-2023",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Gujarat Titans vs Chennai Super Kings",
        "date": "29-05-2023",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Chennai Super Kings"
    }

],

"2024": [

    {
        "teams": "Royal Challengers Bengaluru vs Chennai Super Kings",
        "date": "22-03-2024",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Capitals vs Punjab Kings",
        "date": "23-03-2024",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "23-03-2024",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Lucknow Super Giants",
        "date": "24-03-2024",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Gujarat Titans vs Mumbai Indians",
        "date": "24-03-2024",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Punjab Kings vs Royal Challengers Bengaluru",
        "date": "25-03-2024",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Chennai Super Kings vs Gujarat Titans",
        "date": "26-03-2024",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "27-03-2024",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Capitals",
        "date": "28-03-2024",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Kolkata Knight Riders",
        "date": "29-03-2024",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Lucknow Super Giants vs Punjab Kings",
        "date": "30-03-2024",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Sunrisers Hyderabad vs Gujarat Titans",
        "date": "31-03-2024",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Delhi Capitals vs Chennai Super Kings",
        "date": "31-03-2024",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "01-04-2024",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Lucknow Super Giants vs Royal Challengers Bengaluru",
        "date": "02-04-2024",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Capitals",
        "date": "03-04-2024",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Gujarat Titans vs Punjab Kings",
        "date": "04-04-2024",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "05-04-2024",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Rajasthan Royals",
        "date": "06-04-2024",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Delhi Capitals",
        "date": "07-04-2024",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Lucknow Super Giants vs Gujarat Titans",
        "date": "07-04-2024",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "08-04-2024",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Punjab Kings",
        "date": "09-04-2024",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rajasthan Royals vs Gujarat Titans",
        "date": "10-04-2024",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Mumbai Indians",
        "date": "11-04-2024",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Lucknow Super Giants vs Delhi Capitals",
        "date": "12-04-2024",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Punjab Kings vs Rajasthan Royals",
        "date": "13-04-2024",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Lucknow Super Giants vs Kolkata Knight Riders",
        "date": "14-04-2024",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "14-04-2024",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bengaluru",
        "date": "15-04-2024",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "16-04-2024",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Gujarat Titans vs Delhi Capitals",
        "date": "17-04-2024",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Mumbai Indians vs Punjab Kings",
        "date": "18-04-2024",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Lucknow Super Giants",
        "date": "19-04-2024",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Capitals",
        "date": "20-04-2024",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bengaluru",
        "date": "21-04-2024",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Punjab Kings vs Gujarat Titans",
        "date": "21-04-2024",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "22-04-2024",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Lucknow Super Giants",
        "date": "23-04-2024",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Delhi Capitals vs Gujarat Titans",
        "date": "24-04-2024",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Sunrisers Hyderabad",
        "date": "25-04-2024",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Kolkata Knight Riders vs Punjab Kings",
        "date": "26-04-2024",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Delhi Capitals vs Mumbai Indians",
        "date": "27-04-2024",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Lucknow Super Giants vs Rajasthan Royals",
        "date": "27-04-2024",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Gujarat Titans vs Royal Challengers Bengaluru",
        "date": "28-04-2024",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "28-04-2024",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Delhi Capitals vs Kolkata Knight Riders",
        "date": "29-04-2024",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Mumbai Indians vs Lucknow Super Giants",
        "date": "30-04-2024",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Chennai Super Kings vs Punjab Kings",
        "date": "01-05-2024",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rajasthan Royals",
        "date": "02-05-2024",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "03-05-2024",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Gujarat Titans vs Royal Challengers Bengaluru",
        "date": "04-05-2024",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Chennai Super Kings vs Punjab Kings",
        "date": "05-05-2024",
        "venue": "Himachal Pradesh Cricket Association Stadium, Dharamsala",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Lucknow Super Giants",
        "date": "05-05-2024",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "06-05-2024",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Capitals vs Rajasthan Royals",
        "date": "07-05-2024",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Lucknow Super Giants vs Sunrisers Hyderabad",
        "date": "08-05-2024",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Punjab Kings",
        "date": "09-05-2024",
        "venue": "Himachal Pradesh Cricket Association Stadium, Dharamsala",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Gujarat Titans vs Chennai Super Kings",
        "date": "10-05-2024",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "11-05-2024",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "12-05-2024",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Delhi Capitals",
        "date": "12-05-2024",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Delhi Capitals vs Lucknow Super Giants",
        "date": "14-05-2024",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Rajasthan Royals vs Punjab Kings",
        "date": "15-05-2024",
        "venue": "Barsapara Cricket Stadium, Guwahati",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Lucknow Super Giants vs Mumbai Indians",
        "date": "17-05-2024",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Chennai Super Kings",
        "date": "18-05-2024",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Punjab Kings vs Sunrisers Hyderabad",
        "date": "19-05-2024",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "21-05-2024",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Rajasthan Royals",
        "date": "22-05-2024",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rajasthan Royals",
        "date": "24-05-2024",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "26-05-2024",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Kolkata Knight Riders"
    }

],

"2025": [

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bengaluru",
        "date": "22-03-2025",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rajasthan Royals",
        "date": "23-03-2025",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "23-03-2025",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Lucknow Super Giants vs Delhi Capitals",
        "date": "24-03-2025",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Punjab Kings vs Gujarat Titans",
        "date": "25-03-2025",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "26-03-2025",
        "venue": "Barsapara Cricket Stadium, Guwahati",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Sunrisers Hyderabad vs Lucknow Super Giants",
        "date": "27-03-2025",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Chennai Super Kings",
        "date": "28-03-2025",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Gujarat Titans vs Mumbai Indians",
        "date": "29-03-2025",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Capitals",
        "date": "30-03-2025",
        "venue": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Rajasthan Royals vs Chennai Super Kings",
        "date": "30-03-2025",
        "venue": "Barsapara Cricket Stadium, Guwahati",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "31-03-2025",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Lucknow Super Giants vs Punjab Kings",
        "date": "01-04-2025",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Gujarat Titans",
        "date": "02-04-2025",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Kolkata Knight Riders vs Sunrisers Hyderabad",
        "date": "03-04-2025",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Lucknow Super Giants vs Mumbai Indians",
        "date": "04-04-2025",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Delhi Capitals vs Chennai Super Kings",
        "date": "05-04-2025",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Rajasthan Royals vs Punjab Kings",
        "date": "05-04-2025",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Gujarat Titans",
        "date": "06-04-2025",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Mumbai Indians",
        "date": "07-04-2025",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Lucknow Super Giants vs Kolkata Knight Riders",
        "date": "08-04-2025",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Punjab Kings vs Chennai Super Kings",
        "date": "08-04-2025",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Gujarat Titans vs Rajasthan Royals",
        "date": "09-04-2025",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Delhi Capitals",
        "date": "10-04-2025",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "11-04-2025",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Gujarat Titans vs Lucknow Super Giants",
        "date": "12-04-2025",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Punjab Kings vs Sunrisers Hyderabad",
        "date": "12-04-2025",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rajasthan Royals vs Royal Challengers Bengaluru",
        "date": "13-04-2025",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Mumbai Indians vs Delhi Capitals",
        "date": "13-04-2025",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Lucknow Super Giants vs Chennai Super Kings",
        "date": "14-04-2025",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Punjab Kings vs Kolkata Knight Riders",
        "date": "15-04-2025",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Delhi Capitals vs Rajasthan Royals",
        "date": "16-04-2025",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "17-04-2025",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Punjab Kings",
        "date": "18-04-2025",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Delhi Capitals vs Gujarat Titans",
        "date": "19-04-2025",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Lucknow Super Giants vs Rajasthan Royals",
        "date": "19-04-2025",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Punjab Kings vs Royal Challengers Bengaluru",
        "date": "20-04-2025",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "20-04-2025",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Gujarat Titans vs Kolkata Knight Riders",
        "date": "21-04-2025",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Lucknow Super Giants vs Delhi Capitals",
        "date": "22-04-2025",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Mumbai Indians",
        "date": "23-04-2025",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Rajasthan Royals",
        "date": "24-04-2025",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "25-04-2025",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Punjab Kings vs Kolkata Knight Riders",
        "date": "26-04-2025",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Draw"
    },

    {
        "teams": "Mumbai Indians vs Lucknow Super Giants",
        "date": "27-04-2025",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Capitals vs Royal Challengers Bengaluru",
        "date": "27-04-2025",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Gujarat Titans vs Rajasthan Royals",
        "date": "28-04-2025",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Kolkata Knight Riders vs Delhi Capitals",
        "date": "29-04-2025",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Chennai Super Kings vs Punjab Kings",
        "date": "30-04-2025",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Mumbai Indians vs Rajasthan Royals",
        "date": "01-05-2025",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Gujarat Titans vs Sunrisers Hyderabad",
        "date": "02-05-2025",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Chennai Super Kings",
        "date": "03-05-2025",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Kolkata Knight Riders vs Rajasthan Royals",
        "date": "04-05-2025",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Punjab Kings vs Lucknow Super Giants",
        "date": "04-05-2025",
        "venue": "Himachal Pradesh Cricket Association Stadium, Dharamsala",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Delhi Capitals vs Sunrisers Hyderabad",
        "date": "05-05-2025",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Draw"
    },

    {
        "teams": "Mumbai Indians vs Gujarat Titans",
        "date": "06-05-2025",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Kolkata Knight Riders vs Chennai Super Kings",
        "date": "07-05-2025",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Punjab Kings vs Delhi Capitals",
        "date": "08-05-2025",
        "venue": "Himachal Pradesh Cricket Association Stadium, Dharamsala",
        "winner": "Draw"
    },

    {
        "teams": "Punjab Kings vs Rajasthan Royals",
        "date": "18-05-2025",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Delhi Capitals vs Gujarat Titans",
        "date": "18-05-2025",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Lucknow Super Giants vs Sunrisers Hyderabad",
        "date": "19-05-2025",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "20-05-2025",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Delhi Capitals",
        "date": "21-05-2025",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Lucknow Super Giants vs Gujarat Titans",
        "date": "22-05-2025",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bengaluru",
        "date": "23-05-2025",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Punjab Kings vs Delhi Capitals",
        "date": "24-05-2025",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Chennai Super Kings vs Gujarat Titans",
        "date": "25-05-2025",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "25-05-2025",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Mumbai Indians vs Punjab Kings",
        "date": "26-05-2025",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Lucknow Super Giants vs Royal Challengers Bengaluru",
        "date": "27-05-2025",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Punjab Kings vs Royal Challengers Bengaluru",
        "date": "29-05-2025",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Mumbai Indians vs Gujarat Titans",
        "date": "30-05-2025",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Mumbai Indians vs Punjab Kings",
        "date": "01-06-2025",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Punjab Kings",
        "date": "03-06-2025",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Royal Challengers Bengaluru"
    }

],

"2026": [

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bengaluru",
        "date": "28-03-2026",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Kolkata Knight Riders vs Mumbai Indians",
        "date": "29-03-2026",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Rajasthan Royals",
        "date": "30-03-2026",
        "venue": "Barsapara Cricket Stadium, Guwahati",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Gujarat Titans vs Punjab Kings",
        "date": "31-03-2026",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Lucknow Super Giants vs Delhi Capitals",
        "date": "01-04-2026",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "02-04-2026",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Punjab Kings",
        "date": "03-04-2026",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Mumbai Indians vs Delhi Capitals",
        "date": "04-04-2026",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Rajasthan Royals vs Gujarat Titans",
        "date": "04-04-2026",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Lucknow Super Giants",
        "date": "05-04-2026",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Chennai Super Kings",
        "date": "05-04-2026",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Kolkata Knight Riders vs Punjab Kings",
        "date": "06-04-2026",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Draw"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "07-04-2026",
        "venue": "Barsapara Cricket Stadium, Guwahati",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Gujarat Titans vs Delhi Capitals",
        "date": "08-04-2026",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Kolkata Knight Riders vs Lucknow Super Giants",
        "date": "09-04-2026",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Rajasthan Royals",
        "date": "10-04-2026",
        "venue": "Barsapara Cricket Stadium, Guwahati",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Punjab Kings",
        "date": "11-04-2026",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Chennai Super Kings vs Delhi Capitals",
        "date": "11-04-2026",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Lucknow Super Giants vs Gujarat Titans",
        "date": "12-04-2026",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Mumbai Indians",
        "date": "12-04-2026",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Sunrisers Hyderabad vs Rajasthan Royals",
        "date": "13-04-2026",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Kolkata Knight Riders",
        "date": "14-04-2026",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Lucknow Super Giants vs Royal Challengers Bengaluru",
        "date": "15-04-2026",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Mumbai Indians vs Punjab Kings",
        "date": "16-04-2026",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Kolkata Knight Riders vs Gujarat Titans",
        "date": "17-04-2026",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Delhi Capitals",
        "date": "18-04-2026",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Sunrisers Hyderabad vs Chennai Super Kings",
        "date": "18-04-2026",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rajasthan Royals vs Kolkata Knight Riders",
        "date": "19-04-2026",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Punjab Kings vs Lucknow Super Giants",
        "date": "19-04-2026",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Mumbai Indians vs Gujarat Titans",
        "date": "20-04-2026",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Sunrisers Hyderabad vs Delhi Capitals",
        "date": "21-04-2026",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Rajasthan Royals vs Lucknow Super Giants",
        "date": "22-04-2026",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Chennai Super Kings vs Mumbai Indians",
        "date": "23-04-2026",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Gujarat Titans vs Royal Challengers Bengaluru",
        "date": "24-04-2026",
        "venue": "M Chinnaswamy Stadium, Bengaluru",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Delhi Capitals vs Punjab Kings",
        "date": "25-04-2026",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "25-04-2026",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Chennai Super Kings vs Gujarat Titans",
        "date": "26-04-2026",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Kolkata Knight Riders vs Lucknow Super Giants",
        "date": "26-04-2026",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Delhi Capitals vs Royal Challengers Bengaluru",
        "date": "27-04-2026",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Punjab Kings vs Rajasthan Royals",
        "date": "28-04-2026",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Sunrisers Hyderabad",
        "date": "29-04-2026",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Gujarat Titans",
        "date": "30-04-2026",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Capitals",
        "date": "01-05-2026",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Mumbai Indians vs Chennai Super Kings",
        "date": "02-05-2026",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Kolkata Knight Riders",
        "date": "03-05-2026",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Punjab Kings vs Gujarat Titans",
        "date": "03-05-2026",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Lucknow Super Giants vs Mumbai Indians",
        "date": "04-05-2026",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Delhi Capitals vs Chennai Super Kings",
        "date": "05-05-2026",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Sunrisers Hyderabad vs Punjab Kings",
        "date": "06-05-2026",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Lucknow Super Giants vs Royal Challengers Bengaluru",
        "date": "07-05-2026",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Delhi Capitals vs Kolkata Knight Riders",
        "date": "08-05-2026",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Gujarat Titans vs Rajasthan Royals",
        "date": "09-05-2026",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Lucknow Super Giants vs Chennai Super Kings",
        "date": "10-05-2026",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Chennai Super Kings"
    },

    {
        "teams": "Mumbai Indians vs Royal Challengers Bengaluru",
        "date": "10-05-2026",
        "venue": "Shaheed Veer Narayan Singh International Stadium, Raipur",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Punjab Kings vs Delhi Capitals",
        "date": "11-05-2026",
        "venue": "Himachal Pradesh Cricket Association Stadium, Dharamsala",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Gujarat Titans vs Sunrisers Hyderabad",
        "date": "12-05-2026",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Kolkata Knight Riders vs Royal Challengers Bengaluru",
        "date": "13-05-2026",
        "venue": "Shaheed Veer Narayan Singh International Stadium, Raipur",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Punjab Kings vs Mumbai Indians",
        "date": "14-05-2026",
        "venue": "Himachal Pradesh Cricket Association Stadium, Dharamsala",
        "winner": "Mumbai Indians"
    },

    {
        "teams": "Chennai Super Kings vs Lucknow Super Giants",
        "date": "15-05-2026",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Lucknow Super Giants"
    },

    {
        "teams": "Kolkata Knight Riders vs Gujarat Titans",
        "date": "16-05-2026",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Punjab Kings",
        "date": "17-05-2026",
        "venue": "Himachal Pradesh Cricket Association Stadium, Dharamsala",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Rajasthan Royals vs Delhi Capitals",
        "date": "17-05-2026",
        "venue": "Arun Jaitley Stadium, Delhi",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Chennai Super Kings vs Sunrisers Hyderabad",
        "date": "18-05-2026",
        "venue": "MA Chidambaram Stadium, Chepauk, Chennai",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Lucknow Super Giants vs Rajasthan Royals",
        "date": "19-05-2026",
        "venue": "Sawai Mansingh Stadium, Jaipur",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Mumbai Indians vs Kolkata Knight Riders",
        "date": "20-05-2026",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Kolkata Knight Riders"
    },

    {
        "teams": "Gujarat Titans vs Chennai Super Kings",
        "date": "21-05-2026",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Sunrisers Hyderabad vs Royal Challengers Bengaluru",
        "date": "22-05-2026",
        "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "winner": "Sunrisers Hyderabad"
    },

    {
        "teams": "Lucknow Super Giants vs Punjab Kings",
        "date": "23-05-2026",
        "venue": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
        "winner": "Punjab Kings"
    },

    {
        "teams": "Rajasthan Royals vs Mumbai Indians",
        "date": "24-05-2026",
        "venue": "Wankhede Stadium, Mumbai",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Delhi Capitals vs Kolkata Knight Riders",
        "date": "24-05-2026",
        "venue": "Eden Gardens, Kolkata",
        "winner": "Delhi Capitals"
    },

    {
        "teams": "Royal Challengers Bengaluru vs Gujarat Titans",
        "date": "26-05-2026",
        "venue": "Himachal Pradesh Cricket Association Stadium, Dharamsala",
        "winner": "Royal Challengers Bengaluru"
    },

    {
        "teams": "Rajasthan Royals vs Sunrisers Hyderabad",
        "date": "27-05-2026",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh",
        "winner": "Rajasthan Royals"
    },

    {
        "teams": "Rajasthan Royals vs Gujarat Titans",
        "date": "29-05-2026",
        "venue": "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh",
        "winner": "Gujarat Titans"
    },

    {
        "teams": "Gujarat Titans vs Royal Challengers Bengaluru",
        "date": "31-05-2026",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "winner": "Royal Challengers Bengaluru"
    }

]

    }

    html = """
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

.match-card{
    min-width:280px;
    max-width:280px;
    background:#E8F0E6;
    border-radius:22px;
    padding:22px;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
    transition:.3s;
    flex-shrink:0;
}

.match-card:hover{
    transform:translateY(-8px);
    box-shadow:0 18px 35px rgba(0,0,0,.15);
}

.match-title{
    font-size:28px;
    font-weight:bold;
    font-family:Georgia;
    color:#222;
    margin-bottom:15px;
}

.match-info{
    font-size:17px;
    font-family:Montserrat;
    color:#555;
    line-height:1.8;
}

</style>
"""

    for year, season_matches in teams.items():

        html += f"""
<div class="team-heading">
    IPL {year}
</div>

<div class="scroll-container">
"""

        for match in season_matches:

            html += f"""
<div class="match-card">

    <div class="match-title">
        {match['teams']}
    </div>

    <div class="match-info">
        <b>Date: </b> {match['date']}<br>
        <b>Venue: </b> {match['venue']}<br>
        <b>Winner: </b> {match['winner']}
    </div>

</div>
"""

        html += """
</div>
"""

    st.components.v1.html(
        html,
        height=2500,
        scrolling=True
    )

elif selected == "Venues":

    st.markdown("""
    <style>

    .venue-card{
        background:#E8F0E6;
        border-radius:22px;
        padding:20px;
        text-align:center;
        margin-top:30px;
        box-shadow:0 8px 25px rgba(0,0,0,.08);
        transition:all .3s ease;
        min-height:360px;
    }

    .venue-card:hover{
        transform:translateY(-8px);
        box-shadow:0 18px 35px rgba(0,0,0,.15);
    }

    .venue-img{
        width:180px;
        height:180px;
        object-fit:cover;
        border-radius:16px;
        margin:auto;
        display:block;
        margin-bottom:12px;
    }

    .venue-name{
        font-size:26px;
        font-weight:bold;
        color:#222;
        font-family:Georgia;
        line-height:1.2;
        margin-bottom:12px;
    }

    .venue-details{
        font-size:17px;
        color:#555;
        font-family:Montserrat;
        line-height:1.9;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style="font-family:Montserrat;font-size:70px;">
    IPL Venues
    </h1>
    """, unsafe_allow_html=True)

    venues = [

        {
    "name": "M. Chinnaswamy Stadium",
    "city": "Bengaluru",
    "matches": "95+",
    "capacity": "40,000",
    "image": "https://static.vecteezy.com/system/resources/previews/075/244/946/non_2x/royal-challengers-bengaluru-logo-rcb-logo-icon-on-transparent-background-free-png.png"
},

{
    "name": "Wankhede Stadium",
    "city": "Mumbai",
    "matches": "115+",
    "capacity": "33,000",
    "image": "https://static.vecteezy.com/system/resources/previews/075/244/951/non_2x/mumbai-indians-logo-mi-logo-icon-on-transparent-background-free-png.png"
},

{
    "name": "Eden Gardens",
    "city": "Kolkata",
    "matches": "93+",
    "capacity": "68,000",
    "image": "https://static.vecteezy.com/system/resources/previews/075/244/950/non_2x/kolkata-knight-riders-logo-kkr-logo-icon-on-transparent-background-free-png.png"
},

{
    "name": "M. A. Chidambaram Stadium",
    "city": "Chennai",
    "matches": "81+",
    "capacity": "50,000",
    "image": "https://static.vecteezy.com/system/resources/previews/075/244/942/non_2x/chennai-super-kings-logo-csk-logo-icon-on-transparent-background-free-png.png"
},

{
    "name": "Arun Jaitley Stadium",
    "city": "New Delhi",
    "matches": "84+",
    "capacity": "55,000",
    "image": "https://static.vecteezy.com/system/resources/previews/075/252/975/non_2x/delhi-capitals-logo-dc-logo-icon-on-transparent-background-free-png.png"
},

{
    "name": "Rajiv Gandhi International Stadium",
    "city": "Hyderabad",
    "matches": "71+",
    "capacity": "55,000",
    "image": "https://static.vecteezy.com/system/resources/previews/075/244/941/non_2x/sunrisers-hyderabad-logo-srh-logo-icon-on-transparent-background-free-png.png"
},

{
    "name": "Sawai Mansingh Stadium",
    "city": "Jaipur",
    "matches": "57+",
    "capacity": "30,000",
    "image": "https://static.vecteezy.com/system/resources/previews/075/244/952/non_2x/rajasthan-royals-logo-rr-logo-icon-on-transparent-background-free-png.png"
},

{
    "name": "Narendra Modi Stadium",
    "city": "Ahmedabad",
    "matches": "35+",
    "capacity": "132,000",
    "image": "https://static.vecteezy.com/system/resources/previews/075/244/947/non_2x/gujarat-titans-logo-gt-logo-icon-on-transparent-background-free-png.png"
},

{
    "name": "BRSABV Ekana Cricket Stadium",
    "city": "Lucknow",
    "matches": "21+",
    "capacity": "50,000",
    "image": "https://static.vecteezy.com/system/resources/previews/075/244/945/non_2x/lucknow-super-giants-logo-lsg-logo-icon-on-transparent-background-free-png.png"
},

{
    "name": "Maharaja Yadavindra Singh Stadium",
    "city": "Mullanpur",
    "matches": "16+",
    "capacity": "38,000",
    "image": "https://static.vecteezy.com/system/resources/previews/075/244/949/non_2x/punjab-kings-logo-pbks-logo-icon-on-transparent-background-free-png.png"
},

    ]

    for i in range(0, len(venues), 4):

        cols = st.columns(4)

        for col, venue in zip(cols, venues[i:i+4]):

            with col:

                st.markdown(f"""
<div class="venue-card">
<img class="venue-img" src="{venue['image']}" />
<div class="venue-name">
{venue['name']}
</div>

<div class="venue-details">

<b>City:</b> {venue['city']}<br>
<b>Matches:</b> {venue['matches']}<br>
<b>Capacity:</b> {venue['capacity']}

</div>

</div>
""", unsafe_allow_html=True)
                
elif selected == "Statistics":

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

elif selected == "AI Detective":

    from backend.data.loader import (
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

    matches = get_matches(season)

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

    matches,

    label_visibility="collapsed"

)

        selected_match = get_match_details(

    season,

    selected_match_name

)

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
        '<div class="section-heading">📊 Match Phase Details</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Enter the phase-wise scores in Runs/Wickets format (Example: 61/1)"
    )

    powerplay = st.text_area(

    "⚡ Powerplay",

    placeholder=f"{selected_match['team1']}:61/1,{selected_match['team2']}:42/2",

    height=80

)

    middle = st.text_area(

    "🔥 Middle Overs",

    placeholder=f"{selected_match['team1']}:101/3,{selected_match['team2']}:71/5",

    height=80

)

    death = st.text_area(

    "💥 Death Overs",

    placeholder=f"{selected_match['team1']}:48/2,{selected_match['team2']}:54/1",

    height=80

)

    st.write("")

    solve = st.button(

        "🕵 Solve The Case",

        use_container_width=True,

        type="primary"

    )

    if solve:

                # ==========================================================
        # INVESTIGATION LOADING
        # ==========================================================

        progress = st.progress(0)

        status = st.empty()

        steps = [

            "🕵 Collecting match evidence...",

            "📊 Calculating run rates...",

            "🔥 Detecting momentum...",

            "🧠 Building case file...",

            "🤖 Consulting AI Detective...",

            "⚖ Writing final verdict..."

        ]

        for i, step in enumerate(steps):

            status.info(step)

            progress.progress(int((i + 1) * 100 / len(steps)))

            time.sleep(0.5)

        progress.empty()

        status.success("✅ Investigation Complete!")

        st.write("")

        selected_match["powerplay"] = powerplay

        selected_match["middle"] = middle

        selected_match["death"] = death

        selected_match["result"] = f"{selected_match['winner']} won the match"

        # ==========================================================
        # AI REPORT
        # ==========================================================

        try:

            ai_report = generate_report(selected_match)

            st.markdown(
                '<div class="section-heading">🕵 AI Detective Report</div>',
                unsafe_allow_html=True
            )

            st.markdown(f"""

            <div class="detective-card">

            <div class="report">

            {ai_report.replace(chr(10), "<br>")}

            </div>

            </div>

            """, unsafe_allow_html=True)

        except Exception:
            st.exception(Exception(traceback.format_exc()))