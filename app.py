from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

# Static routing


@app.route("/")
def index():
    # return "Hello World!"
    return render_template("index.html")


# @app.route("/about/") default method is GET.
# Also we can use more than one, like this ["GET", "POST"]
@app.route("/about/", methods=["GET"])
def about():
    # return "<h2>About this Flask application</h2>"
    return render_template("about.html",
                           company_name="Flask Skoode Inc.",
                           app="Flask Application",
                           version="2.3.2")


"""
Note about "/" (trailing slash) in URL.
Think like a file system.
✅ when it looks like a folder. "/users/"
❌ when it looks like a file. "/users/1.txt"
"""

# Variable routing
"""
Using type hinting, also the str built-in type is able
to use some string validation function and string transformation

Actually it's called Variable Route Types
string(default), int, path, uuid
"""


@app.route("/hi/<string:name>")
def hi(name):
    """
    A function that takes in a name as a parameter and returns a greeting message.

    Parameters:
    - name (str): The name to be greeted.

    Returns:
    - str: A greeting message based on the provided name.
    """
    if name.isalpha():
        name = f"{escape(name.capitalize())}"
        return render_template("hi.html", name=name)
    else:
        return render_template("hi.html", name="")
