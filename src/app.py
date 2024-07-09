# Import the Flask module from the flask package.
from flask import Flask

# Create a Flask application instance.
app = Flask(__name__)


# Define the first endpoint at the root URL.
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Home Page!"


# Define the second endpoint at '/about'.
@app.route("/api/tree", methods=["GET", "POST", "DELETE"])
def about():
    return "This is the About Page."


# Define the third endpoint at '/contact'.
@app.route("/api/graph", methods=["GET", "POST", "DELETE"])
def contact():
    return "Contact us at contact@example.com."


@app.route("/api/linkedList", methods=["GET", "POST", "DELETE"])
def contact():
    return "Contact us at contact@example.com."


# Check if the script is executed directly (not imported).
if __name__ == "__main__":
    # Run the Flask application in debug mode.
    app.run(debug=True)
