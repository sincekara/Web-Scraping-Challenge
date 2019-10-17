from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

conn = 'mongodb://localhost:27017/mars'

client = pymongo.MongoClient(conn)


# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    marsmission = client.db.mars_mission.find_one()
    return render_template("index.html", marsmission=marsmission)

# Scraping info
@app.route("/scrape")
def scrape():
    marsmission = client.db.mars_mission
    mars_info = scrape_mars.scrape()
    marsmission.update({}, mars_info)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
