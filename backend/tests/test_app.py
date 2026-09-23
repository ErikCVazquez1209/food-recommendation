from app import app

def test_recommendation_rejects_incomplete_request():
    """La API debe de rechazar solicitudes con campos obligatorios incompletos"""

    client = app.test_client()

    response = client.post(
        "/api/rec",
        json={
            "type": "Veg",
            "mins": "30",
        },
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Missing required fields: step, ingr"
    }