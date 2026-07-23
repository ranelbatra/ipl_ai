from unittest.mock import patch


def test_investigate_response_contract(client):
    """
    Verify the response schema of the investigate endpoint.
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
        mock_generate_report.return_value = "Sample AI Report"

        response = client.post("/investigate", json=payload)

    assert response.status_code == 200

    data = response.json()

    # Contract validation
    assert isinstance(data, dict)
    assert "report" in data
    assert isinstance(data["report"], str)