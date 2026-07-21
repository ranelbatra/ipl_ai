import streamlit as st

from data.loader import *


def show_matches():
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