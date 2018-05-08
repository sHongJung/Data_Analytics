from flask import Flask, render_template
import pymongo

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.hurricane
collection = db.hurricane

db.collection.insert_many(
    [
        {
            "name": "Harvey",
            "cat": "Category 4"
        },
        {
            "name": "Irma",
            "cat": "Category 5"
        }
    ]
)


@app.route("/")
def index():
    hurricanes = list(db.collection.find())
    print(hurricanes)
    return render_template("index.html", hurricanes=hurricanes)


if __name__ == "__main__":
    app.run(debug=True)
