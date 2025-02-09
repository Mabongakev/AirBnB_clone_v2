#!/usr/bin/python3

"""
Starts a Flask web application
"""

from flask import Flask
from flask import render_template
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """python text path"""
    return f"Python {escape(text).replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    "number route"
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """number template route"""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """number_odd_or_even_route"""

    odd_or_even = ""

    if int(n) % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"

    return render_template("6-number_odd_or_even.html",
                           odd_or_even=f"{n} is {odd_or_even}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
