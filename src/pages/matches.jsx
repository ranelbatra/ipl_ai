import Navbar from "../components/navbar";
import "./Pages.css";

const matches = [
  {
    id: 1,
    teams: "MI vs CSK",
    winner: "Mumbai Indians",
    venue: "Wankhede",
    season: "2025",
    result: "Won by 18 Runs"
  },
  {
    id: 2,
    teams: "RCB vs KKR",
    winner: "RCB",
    venue: "Chinnaswamy",
    season: "2025",
    result: "Won by 7 Wickets"
  },
  {
    id: 3,
    teams: "GT vs RR",
    winner: "GT",
    venue: "Ahmedabad",
    season: "2025",
    result: "Won by 5 Wickets"
  },
  {
    id: 4,
    teams: "PBKS vs DC",
    winner: "PBKS",
    venue: "Mohali",
    season: "2025",
    result: "Won by 20 Runs"
  }
];

function Matches() {
  return (
    <>
      <Navbar />

      <div className="page-header">
        <h1>🏏 Matches</h1>
        <p>IPL Match Summary</p>
      </div>

      <div className="table-card">

        <table>

          <thead>

            <tr>
              <th>ID</th>
              <th>Match</th>
              <th>Winner</th>
              <th>Venue</th>
              <th>Season</th>
              <th>Result</th>
            </tr>

          </thead>

          <tbody>

            {matches.map((match) => (

              <tr key={match.id}>

                <td>{match.id}</td>
                <td>{match.teams}</td>
                <td>{match.winner}</td>
                <td>{match.venue}</td>
                <td>{match.season}</td>
                <td>{match.result}</td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </>
  );
}

export default Matches;