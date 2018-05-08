# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
# CODE GOES HERE
app = Flask(__name__)


@app.route("/")
def school():
    school_list = ["UCB", "UCD", "UCLA", "UTA", "TAMU"]
    return render_template("home.html", list=school_list)


# @TODO:  Create a route and view function that takes in a list of strings and renders index.html template
# CODE GOES HERE
if __name__ == "__main__":
    app.run(debug=True)
