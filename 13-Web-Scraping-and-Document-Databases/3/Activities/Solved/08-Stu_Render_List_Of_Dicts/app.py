# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template


@app.route("/")
def index():
    hurricanes = [{"Harvey": "Category 4"}, {"Irma": "Category 5"}]
    return render_template("index.html", list=hurricanes)


if __name__ == "__main__":
    app.run(debug=True)
