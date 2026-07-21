import streamlit as st

from data.loader import *


def show_venues():
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