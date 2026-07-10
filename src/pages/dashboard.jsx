import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function Dashboard() {

  const [overview, setOverview] = useState({

    matches: 0,
    players: 0,
    teams: 0,
    venues: 0

  });

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/overview")
      .then((res) => setOverview(res.data))
      .catch((err) => console.log(err));

  }, []);

  return (

    <>

      <Navbar />

      <div className="hero">

        <h1>IPL Analytics Dashboard</h1>

        <p>

          AI Powered Cricket Analytics & Match Investigation

        </p>

      </div>

      <div className="cards">

        <div className="card">

          <h3>Total Matches</h3>

          <h1>{overview.matches}</h1>

        </div>

        <div className="card">

          <h3>Total Players</h3>

          <h1>{overview.players}</h1>

        </div>

        <div className="card">

          <h3>Total Teams</h3>

          <h1>{overview.teams}</h1>

        </div>

        <div className="card">

          <h3>Total Venues</h3>

          <h1>{overview.venues}</h1>

        </div>

      </div>

      <div className="bottom">

        <div className="panel">

          <h2>Recent Matches</h2>

          <ul>

            <li>🏏 MI defeated CSK by 18 Runs</li>

            <li>🏏 RCB defeated KKR by 7 Wickets</li>

            <li>🏏 GT defeated RR by 5 Wickets</li>

            <li>🏏 PBKS defeated DC by 20 Runs</li>

          </ul>

        </div>

        <div className="panel">

          <h2>Top Teams</h2>

          <ul>

            <li>🏆 Mumbai Indians</li>

            <li>🏆 Chennai Super Kings</li>

            <li>🏆 Kolkata Knight Riders</li>

            <li>🏆 Royal Challengers Bengaluru</li>

          </ul>

        </div>

      </div>

    </>

  );

}

export default Dashboard;