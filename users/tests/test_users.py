import pytest
from app import app  # Ensure your users/app.py defines 'app'

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_root_endpoint(client):
    response = client.get('/')
    assert b'User task' in response.data

def test_host_endpoint(client):
    response = client.get('/host')
    # Optionally, check that some value is returned (non-empty)
    assert response.status_code == 200
    assert response.data != b""

def test_ip_endpoint(client):
    response = client.get('/ip')
    # Check that an IP address (or non-empty string) is returned
    assert response.status_code == 200
    assert response.data != b""
