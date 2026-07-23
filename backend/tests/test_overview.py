def test_overview_endpoint(client):
    """
    Verify that the /overview endpoint returns
    the expected dashboard statistics.
    """

    response = client.get("/overview")

    # Status code should be OK
    assert response.status_code == 200

    # Response should be JSON
    data = response.json()

    # Verify required fields exist
    assert "matches" in data
    assert "players" in data
    assert "teams" in data
    assert "venues" in data

    # Verify data types
    assert isinstance(data["matches"], int)
    assert isinstance(data["players"], int)
    assert isinstance(data["teams"], int)
    assert isinstance(data["venues"], int)

    # Verify values are non-negative
    assert data["matches"] >= 0
    assert data["players"] >= 0
    assert data["teams"] >= 0
    assert data["venues"] >= 0