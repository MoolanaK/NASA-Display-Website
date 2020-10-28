from flask import Flask, render_template

import requests
import nasaAPI

app = Flask(__name__)

#@app.route("/")
#def index():
#    render_template("index.html")

@app.route("/")
def nasa():
    return render_template("index.html")

@app.route("/curiosity")
def curiosity():
    api = nasaAPI.API()
    pics = api.getCuriosity()
    img1, img2, img3, img4, img5, img6 = pics
    return render_template("curiosity.html", img1 = img1, img2 = img2, img3 = img3, img4 = img4,img5 = img5, img6 = img6)

@app.route("/hubble")
def hubble():
    api = nasaAPI.API()
    pics = api.getHubble()
    img1, img2, img3, img4, img5, img6 = pics
    return render_template("hubble.html", img1 = img1, img2 = img2, img3 = img3, img4 = img4,img5 = img5, img6 = img6)