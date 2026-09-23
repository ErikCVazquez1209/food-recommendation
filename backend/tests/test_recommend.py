import pandas as pd
import recommend

def test_excludes_recipe_above_requested_minutes(monkeypatch):
    """Una receta no debe de superar el tiempo maximo de petición"""

    recipes = pd.DataFrame(
        {
            "name": ["Slow vegetable recipe"],
            "minutes": [45],
            "n_steps": [5],
            "n_ingredients": [5],
            "food types": ["Veg"],
            "score": [4.9],
        }
    )

    monkeypatch.setattr(recommend, "df", recipes)

    user_data = ["Veg", "30", "10", "10"]

    result = recommend.filter_database(user_data)

    assert result == {"error": 1}




