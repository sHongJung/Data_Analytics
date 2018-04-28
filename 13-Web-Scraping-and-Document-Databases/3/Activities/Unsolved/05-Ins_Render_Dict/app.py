# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    hurricane_dictionary = {"hurricane_1": "Harvey",
                            "hurricane_2": "Irma"}
    return render_template("index.html", dict=hurricane_dictionary)


if __name__ == "__main__":
    app.run(debug=True)
