#!usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

app.route("/")
def hello():
    """Function to print Hello HBNB!"""
    return "Hello HBNB!"

app.route("/hbnb")
def hbnb():
    """Function to print HBNB"""
    return "HBNB"

app.route("/c/<text>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
