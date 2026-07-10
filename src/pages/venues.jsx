import Navbar from "../components/navbar";
import "./Pages.css";

const venues = [

{
name:"Wankhede Stadium",
city:"Mumbai",
capacity:"33000",
pitch:"Batting Friendly"
},

{
name:"Chepauk Stadium",
city:"Chennai",
capacity:"50000",
pitch:"Spin Friendly"
},

{
name:"Eden Gardens",
city:"Kolkata",
capacity:"68000",
pitch:"Balanced"
},

{
name:"Narendra Modi Stadium",
city:"Ahmedabad",
capacity:"132000",
pitch:"Balanced"
}

];

function Venues(){

return(

<>

<Navbar/>

<div className="page-header">

<h1>🏟 IPL Venues</h1>

<p>Major IPL Stadiums</p>

</div>

<div className="venue-grid">

{venues.map((venue,index)=>(

<div className="venue-card" key={index}>

<h2>{venue.name}</h2>

<p>📍 {venue.city}</p>

<p>👥 Capacity : {venue.capacity}</p>

<p>🏏 {venue.pitch}</p>

</div>

))}

</div>

</>

)

}

export default Venues;
