#!/usr/bin/python3

"""
A script to Start a Flask web application
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Root path"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb path"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """c text path"""
    return f"C {escape(text).replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
