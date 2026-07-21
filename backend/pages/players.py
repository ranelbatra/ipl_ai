import streamlit as st

from data.loader import *


def show_players():

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