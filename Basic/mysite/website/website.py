from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
import pandas as pd
#from send_email import send_email


app=Flask(__name__)





@app.route("/")
def index():
    return render_template("home.html")
@app.route("/home", methods=['POST'])
def home():
    return render_template("home.html")
@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        address=request.form["address_name"]
      
        gc = Nominatim()
        real_address = gc.geocode(address)
        latitude = real_address.latitude
        longitude = real_address.longitude

        return render_template("success1.html", lon_coor = longitude, lan_coor = latitude , addy = address)
        



if __name__ == '__main__':
    app.debug = True
    app.run()