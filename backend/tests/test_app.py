from app import app

def test_recommendation_rejects_incomplete_request():
    """The API must reject requests with missing required fields."""

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


def test_recommendation_rejects_unknown_food_type():
    """The API must reject unsupported food categories."""

    client = app.test_client()

    response = client.post(
        "/api/rec",
        json={
            "type": "Unknown",
            "mins": "30",
            "step": "10",
            "ingr": "8",
        },
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Invalid food type"
    }

def test_recommendation_rejects_non_numeric_limit():
    """Recipe limits must contain numbers."""

    client = app.test_client()

    response = client.post(
        "/api/rec",
        json={
            "type": "Veg",
            "mins": "fast",
            "step": "10",
            "ingr": "8",
        },
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Recipe limits must be numeric"
    }