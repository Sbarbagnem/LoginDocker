from conftest import client

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_showSignUp(client):
    response = client.get('/showSignUp')
    assert response.status_code == 200

def test_showSignIn(client):
    response = client.get('/showSignIn')
    assert response.status_code == 200

def test_signUp(client):
    response = client.get('/signUp')
    assert response.status_code == 200
