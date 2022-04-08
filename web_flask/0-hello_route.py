#!/usr/bin/pyhon3
"""Script tha starts a Flask web application"""

from flask import Flask


app = Flask(__name__)

app.url_map.strict_slashes = False

@app.route("/")
def display():
    return "<p>Hello HBNB!</p>"

