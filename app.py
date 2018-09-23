from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_nasa
from selenium import webdriver

app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/nasa_app"
# mongo = PyMongo(app)

mongo = PyMongo(app, uri="mongodb://localhost:27017/nasa_app")

nasa_data = {}

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    nasa_data = scrape_nasa.scrape()
    mars.update({}, nasa_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)