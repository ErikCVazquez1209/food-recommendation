from flask import Flask, jsonify, request
from recommend import filter_database

HOST = "0.0.0.0"
PORT = 5000

REQUIRED_FIELDS = ("type", "mins", "step", "ingr")

app = Flask(__name__)

@app.route("/")
def api():
    """Return the main API page."""

    return "<h1>API</h1>"


@app.route("/api/test", methods=["GET", "POST"])
def test():
    """Verify that the API accepts GET and POST requests."""

    if request.method == "POST":
        return jsonify({"test": "POST success"})

    return jsonify({"test": "GET success"})


@app.route("/api/rec", methods=["POST"])
def rec():
    """Verify that the API accepts GET and POST requests."""
    
    json_data = request.get_json(silent=True)

    if not isinstance(json_data, dict):
        return jsonify(
            {"error": "Request body must be valid JSON"}
        ), 400

    missing_fields = [
        field
        for field in REQUIRED_FIELDS
        if field not in json_data
    ]

    if missing_fields:
        missing_names = ", ".join(missing_fields)

        return jsonify(
            {
                "error": (
                    f"Missing required fields: {missing_names}"
                )
            }
        ), 400

    user_data = [
        json_data[field]
        for field in REQUIRED_FIELDS
    ]

    try:
        recommendation = filter_database(user_data)
    except (TypeError, ValueError):
        return jsonify(
            {"error": "Recipe limits must be numeric"}
        ), 400

    return jsonify(recommendation)


if __name__ == "__main__":
    app.run(
        host=HOST,
        debug=True,
        port=PORT,
    )



