def test_investigate_invalid_payload(client):
    """
    Ensure the API rejects incomplete requests.
    """

    payload = {
        "team1": "Mumbai Indians"
    }

    response = client.post("/investigate", json=payload)

    assert response.status_code == 422