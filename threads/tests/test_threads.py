import pytest
from app import app  # Ensure your threads/app.py defines 'app'

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_root_endpoint(client):
    response = client.get('/')
    assert b'Threads task' in response.data

def test_host_endpoint(client):
    response = client.get('/host')
    # Verify that some hostname is returned.
    assert response.status_code == 200
    assert response.data != b""

def test_ip_endpoint(client):
    response = client.get('/ip')
    # Verify that an IP address is returned.
    assert response.status_code == 200
    assert response.data != b""
