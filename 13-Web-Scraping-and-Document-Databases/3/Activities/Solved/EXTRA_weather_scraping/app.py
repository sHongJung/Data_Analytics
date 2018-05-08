# import necessary libraries
from flask import Flask, render_template
import pymongo
import scrape_weather


# create instance of Flask app
app = Flask(__name__)


client = pymongo.MongoClient()
db = client.weather_db
collection = db.weather

@app.route("/scrape")
def scrape():
    forecast = scrape_weather.scrape()
    db.collection.insert_one(forecast)
    return "Scraped some data"

# create route that renders index.html template
@app.route("/")
def home():
    forecasts = list(db.collection.find())
    print(forecasts)



    return render_template("index.html", forecasts=forecasts)


if __name__ == "__main__":
    app.run(debug=True)
