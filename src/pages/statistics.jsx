import Navbar from "../components/navbar";
import "./Pages.css";

function Statistics(){

return(

<>

<Navbar/>

<div className="page-header">

<h1>📊 IPL Statistics</h1>

<p>Season Overview</p>

</div>

<div className="stats-grid">

<div className="stat-card">

<h3>Total Matches</h3>

<h1>1234</h1>

</div>

<div className="stat-card">

<h3>Total Players</h3>

<h1>321</h1>

</div>

<div className="stat-card">

<h3>Total Teams</h3>

<h1>19</h1>

</div>

<div className="stat-card">

<h3>Total Venues</h3>

<h1>62</h1>

</div>

</div>

<div className="progress-section">

<h2>Top Teams</h2>

<div className="progress-item">

<span>Mumbai Indians</span>

<div className="progress">

<div className="bar" style={{width:"90%"}}></div>

</div>

</div>

<div className="progress-item">

<span>Chennai Super Kings</span>

<div className="progress">

<div className="bar" style={{width:"88%"}}></div>

</div>

</div>

<div className="progress-item">

<span>Kolkata Knight Riders</span>

<div className="progress">

<div className="bar" style={{width:"72%"}}></div>

</div>

</div>

</div>

</>

)

}

export default Statistics;