import pandas as pd
from pathlib import Path

"""

    Description:
        This file defines a function for recommendation from database according to input.

    Functions:
        filter_database([array])

"""

DEFAULT_MAX_MINUTES = 999
DEFAULT_MAX_STEPS = 99
DEFAULT_MAX_INGREDIENTS = 99

FOOD_TYPE_MAP = {
    "Healthy": "Healthy",
    "Veg": "Veg",
    "Non-Veg": "Non-veg",
    "Veg_Dessert": "Veg dessert",
    "Non-Veg_Dessert": "Non-Veg dessert",
}

def _parse_limit(value, default_value):
    """Convert a user limit without modifying the original input."""

    if value == "":
        return default_value

    parsed_value = int(value)

    if parsed_value < 0:
        return default_value

    return parsed_value

# database_file = "backend/database/recipeData.csv"                   # direct path for windows development

database_file = Path.cwd() / "database" / "recipeData.csv"          # for getting path in docker

df = pd.read_csv(database_file)     # Main data frame


def filter_database(user_data):
    """

    Description:
        This function filters dataset according to input and gives recommendation in (dict) format for easy jsonify.
      
    Parameters:
        user_data (list): User preferences and maximum recipe limits.
    
    Returns:
        df_final (dict): Recipe recommendation.

    Used by:
        Only called by app.py.

    Requires:
        Main database in recipeData.csv file in /database folder.

    """

    food_type = user_data[0]
    max_minutes = _parse_limit(
        user_data[1],
        DEFAULT_MAX_MINUTES,
    )
    max_steps = _parse_limit(
        user_data[2],
        DEFAULT_MAX_STEPS,
    )
    max_ingredients = _parse_limit(
        user_data[3],
        DEFAULT_MAX_INGREDIENTS,
    )

    # Filter data by type of food
       # Validate and translate the requested food category
    if food_type not in FOOD_TYPE_MAP:
        raise ValueError("Invalid food type")

    dataset_food_type = FOOD_TYPE_MAP[food_type]

    df_filtered = df[
        df["food types"] == dataset_food_type
    ]



    #Filter recipes using inclusive maximum limits
    df_filtered = df_filtered[
        df_filtered["minutes"] <= max_minutes
    ]

    df_filtered = df_filtered[
        df_filtered["n_steps"] <= max_steps
    ]

    df_filtered = df_filtered[
        df_filtered["n_ingredients"] <= max_ingredients
    ]
      # final filtered data frame 



    # Sorting data by score which is based on average rating and number of votes
    df_sorted = df_filtered.sort_values('score',ascending = False).head(50)         # Taking top 50 best recipes  

    
    if df_sorted.empty:
        return {'error' : 1}

    # Taking a random recipe from top sorted, to prevent same recommendation
    df_final = df_sorted.sample(1)

    # Converting to dict with orient for easy data access in frontend
    df_final = df_final.to_dict(orient='list')

    return df_final





# for testing only
# userData = ['Non-Veg', '120', '10', '9']
# filter_database(userData)
