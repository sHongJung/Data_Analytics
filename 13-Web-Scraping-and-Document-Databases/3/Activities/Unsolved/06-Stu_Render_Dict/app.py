# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
# CODE GOES HERE
app = Flask(__name__)


# @TODO:  Create a route and view function that takes in a dictionary and renders index.html template
# CODE GOES HERE
@app.route("/")
def flask_dict():
    dictionary = {"Seohong":"Software Engineer", "Danny":"Process Engineer"}
    return render_template("index.html", dict = dictionary)


if __name__ == "__main__":
    app.run(debug=True)
