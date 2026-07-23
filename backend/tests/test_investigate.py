from unittest.mock import patch


def test_investigate_success(client):
    """
    Verify that the AI investigation endpoint
    successfully processes a valid request.
    """

    payload = {
        "team1": "Mumbai Indians",
        "team2": "Chennai Super Kings",
        "winner": "Mumbai Indians",
        "powerplay": "MI: 55/1, CSK: 48/2",
        "middleOvers": "MI: 120/3, CSK: 105/5",
        "deathOvers": "MI: 185/6, CSK: 170/8",
        "playerOfMatch": "Rohit Sharma",
        "venue": "Wankhede Stadium",
        "result": "MI won by 15 runs"
    }

    with patch("main.generate_report") as mock_generate_report:
        mock_generate_report.return_value = "This is a sample AI report."

        response = client.post("/investigate", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "report" in data
    assert data["report"] == "This is a sample AI report."