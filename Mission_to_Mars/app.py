from flask import Flask, render_template, redirect
import pymongo
from pymongo import MongoClient
import scrape_mars

try:
    conn = MongoClient("mongodb://localhost:27017/")
    print("Succesful!")
                       
except:
    print("Unsuccesful connection")

mydb = conn["mars"]
mycol = mydb["mars_mission"]

# Create Flask
app = Flask(__name__)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars_wonder = mycol.find_one()
    return render_template("index.html", Updated_title=mars_wonder['Updated_title'], Updated_news=mars_wonder['Updated_news'], Featured_image=mars_wonder['Featured_image'], Weather_update=mars_wonder['Weather_update'], Facts_Mars=mars_wonder['Facts_Mars'], hemisurl_1=mars_wonder['Cerberus_hemisphere'], hemisurl_2=mars_wonder['Schiaparelli_hemisphere'], hemisurl_3=mars_wonder['Syrtis_hemisphere'], hemisurl_4=mars_wonder['Valler_hemisphere'])
                                                                                                   
# Scraping info
@app.route("/scrape")
def scrape():
    full_mars = mycol
    mars_wonder = scrape_mars.scrape()
    full_mars.update({}, mars_wonder, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
