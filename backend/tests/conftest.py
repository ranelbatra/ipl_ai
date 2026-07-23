from fastapi.testclient import TestClient
from main import app
import pytest


@pytest.fixture
def client():
    """
    Creates a reusable FastAPI TestClient
    for all integration tests.
    """
    return TestClient(app)