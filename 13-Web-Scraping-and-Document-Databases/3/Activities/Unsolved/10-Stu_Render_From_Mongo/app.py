from flask import Flask, render_template
import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.hurricane
collection = db.hurricane
# @TODO: create a list of dictionaries to insert into the db
db.collection.insert_many(
    [
        {"name":"Ken1",
         "hobby":"Music2"
         },
        {
         "name":"Danny1",
         "hobby":"Dance2"
        }

    ]
)


@app.route('/')
def index():
    # @TODO: write a statement that finds all the items in the db and sets it to a variable
    # CODE GOES HERE
    lists = list(db.collection.find())
    # @TODO: render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", lists=lists)

if __name__ == "__main__":
    app.run(debug=True)
