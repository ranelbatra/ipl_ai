import Navbar from "../components/Navbar";
import "./Pages.css";

const players = [

{
name:"Virat Kohli",
team:"RCB",
runs:8509,
role:"Batter"
},

{
name:"MS Dhoni",
team:"CSK",
runs:5439,
role:"Wicket Keeper"
},

{
name:"Rohit Sharma",
team:"MI",
runs:6928,
role:"Batter"
},

{
name:"Jasprit Bumrah",
team:"MI",
wickets:183,
role:"Bowler"
},

{
name:"Sunil Narine",
team:"KKR",
wickets:192,
role:"All Rounder"
},

{
name:"Ravindra Jadeja",
team:"CSK",
wickets:170,
runs:3100,
role:"All Rounder"
}

];

function Players(){

return(

<>

<Navbar/>

<div className="page-header">

<h1>👨‍💼 Players</h1>

<p>Top IPL performers.</p>

</div>

<div className="player-grid">

{players.map((player,index)=>(

<div className="player-card" key={index}>

<h2>{player.name}</h2>

<h3>{player.team}</h3>

<p><strong>Role</strong></p>

<p>{player.role}</p>

{player.runs &&
<p>🏏 Runs : {player.runs}</p>}

{player.wickets &&
<p>🎯 Wickets : {player.wickets}</p>}

</div>

))}

</div>

</>

)

}

export default Players;