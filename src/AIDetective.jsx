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
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {

    setError("");

    setMatchData({
        ...matchData,
        [e.target.name]: e.target.value
    });

};

    const investigateMatch = async () => {

    // Basic validation
    if (
        !matchData.team1 ||
        !matchData.team2 ||
        !matchData.winner
    ) {
        setError("Please fill in all required fields.");
        return;
    }

    setLoading(true);
    setError("");
    setReport("");

    try {

        const response = await axios.post(
            "http://127.0.0.1:8000/investigate",
            matchData,
            {
                timeout: 30000
            }
        );

        setReport(response.data.report);

    } catch (error) {

        if (error.code === "ECONNABORTED") {

            setError("⏳ The server took too long to respond.");

        } else if (error.response) {

            setError(error.response.data.detail || "Server error.");

        } else if (error.request) {

            setError("🔌 Unable to connect to the backend.");

        } else {

            setError("Something went wrong.");
        }

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

                <button onClick={investigateMatch} disabled={loading}>
                {loading ? "Investigating..." : "🔍 Investigate Match"}
                </button>

            </div>

            {loading && (
                <div className="loading-box">
    <p>🧠 AI is analyzing the match...</p>
    <p>Please wait...</p>
</div>
            )}

            {
    error && (
        <div className="error-box">
            <p>{error}</p>

            <button onClick={investigateMatch}>
                Retry
            </button>

        </div>
    )
}

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