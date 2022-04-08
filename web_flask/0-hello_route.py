#!/usr/bin/pyhon3
"""Script tha starts a Flask web application
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """Display Hello HBNB!"""
    return "<p>Hello HBNB!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
