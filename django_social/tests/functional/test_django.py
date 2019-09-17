
def test_django(client, db):
    response = client.get('/')
    assert response.status_code == 200
