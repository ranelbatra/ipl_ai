import Navbar from "../components/Navbar";
import "./Pages.css";

const teams = [
  {
    name: "Mumbai Indians",
    captain: "Hardik Pandya",
    titles: 5,
    home: "Wankhede Stadium",
    color: "#004BA0"
  },
  {
    name: "Chennai Super Kings",
    captain: "MS Dhoni",
    titles: 5,
    home: "Chepauk Stadium",
    color: "#F9CD05"
  },
  {
    name: "Royal Challengers Bengaluru",
    captain: "Rajat Patidar",
    titles: 0,
    home: "M. Chinnaswamy Stadium",
    color: "#D71920"
  },
  {
    name: "Kolkata Knight Riders",
    captain: "Ajinkya Rahane",
    titles: 3,
    home: "Eden Gardens",
    color: "#3A225D"
  },
  {
    name: "Sunrisers Hyderabad",
    captain: "Pat Cummins",
    titles: 1,
    home: "Hyderabad",
    color: "#F26522"
  },
  {
    name: "Punjab Kings",
    captain: "Shreyas Iyer",
    titles: 0,
    home: "Mohali",
    color: "#D71920"
  }
];

function Teams() {
  return (
    <>
      <Navbar />

      <div className="page-header">
        <h1>🏏 IPL Teams</h1>
        <p>Explore every franchise.</p>
      </div>

      <div className="team-grid">

        {teams.map((team, index) => (

          <div
            key={index}
            className="team-card"
            style={{ borderTop: `8px solid ${team.color}` }}
          >

            <h2>{team.name}</h2>

            <p>
              <strong>Captain</strong><br />
              {team.captain}
            </p>

            <p>
              <strong>Titles</strong><br />
              🏆 {team.titles}
            </p>

            <p>
              <strong>Home Ground</strong><br />
              {team.home}
            </p>

          </div>

        ))}

      </div>
    </>
  );
}

export default Teams;