import { useState } from "react";
import axios from "axios";

function AIDetective() {

    const [matchData, setMatchData] = useState({
        team1: "",
        team2: "",
        winner: "",
        powerplay: "",
        middleOvers: "",
        deathOvers: "",
        playerOfMatch: "",
        venue: "",
        result: ""
    });

    const [report, setReport] = useState("");
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {
        setMatchData({
            ...matchData,
            [e.target.name]: e.target.value
        });
    };

    const investigateMatch = async () => {
        try {
            setLoading(true);

            const response = await axios.post(
                "http://127.0.0.1:8000/investigate",
                matchData
            );

            setReport(response.data.detective_report);

        } catch (error) {
            console.log(error);
            setReport("❌ Failed to generate detective report.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="detective-page">

            <h1>🕵️ IPL Match Detective</h1>

            <p>
                Enter the match details below and let AI investigate what happened.
            </p>

            <div className="detective-form">

                <input
                    type="text"
                    name="team1"
                    placeholder="Team 1"
                    value={matchData.team1}
                    onChange={handleChange}
                />

                <input
                    type="text"
                    name="team2"
                    placeholder="Team 2"
                    value={matchData.team2}
                    onChange={handleChange}
                />

                <input
                    type="text"
                    name="winner"
                    placeholder="Winner"
                    value={matchData.winner}
                    onChange={handleChange}
                />

                <input
                    type="text"
                    name="playerOfMatch"
                    placeholder="Player of the Match"
                    value={matchData.playerOfMatch}
                    onChange={handleChange}
                />

                <input
                    type="text"
                    name="venue"
                    placeholder="Venue"
                    value={matchData.venue}
                    onChange={handleChange}
                />

                <textarea
                    name="powerplay"
                    placeholder="Powerplay Analysis"
                    rows="3"
                    value={matchData.powerplay}
                    onChange={handleChange}
                />

                <textarea
                    name="middleOvers"
                    placeholder="Middle Overs Analysis"
                    rows="3"
                    value={matchData.middleOvers}
                    onChange={handleChange}
                />

                <textarea
                    name="deathOvers"
                    placeholder="Death Overs Analysis"
                    rows="3"
                    value={matchData.deathOvers}
                    onChange={handleChange}
                />

                <textarea
                    name="result"
                    placeholder="Match Result"
                    rows="2"
                    value={matchData.result}
                    onChange={handleChange}
                />

                <button onClick={investigateMatch}>
                    🔍 Investigate Match
                </button>

            </div>

            {loading && (
                <p>⏳ AI is investigating the match...</p>
            )}

            {report && (
                <div className="report-box">

                    <h2>🕵️ Detective Report</h2>

                    <pre>{report}</pre>

                </div>
            )}

        </div>
    );
}

export default AIDetective;