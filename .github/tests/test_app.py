def test_home_endpoint():
    from app import app
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
