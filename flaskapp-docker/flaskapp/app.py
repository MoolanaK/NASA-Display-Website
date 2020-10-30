from flask import Flask, render_template

import requests
import nasaAPI

app = Flask(__name__)

@app.route("/")
def nasa():
    return render_template("index.html")

@app.route("/earth")
def earth():
    api = nasaAPI.API()
    pics = api.getEarth()
    img1, img2, img3, img4, img5, img6 = pics
    return render_template("earth.html", img1 = img1, img2 = img2, img3 = img3, img4 = img4,img5 = img5, img6 = img6)

@app.route("/hubble")
def hubble():
    api = nasaAPI.API()
    pics = api.getHubble()
    img1, img2, img3, img4, img5, img6 = pics
    return render_template("hubble.html", img1 = img1, img2 = img2, img3 = img3, img4 = img4,img5 = img5, img6 = img6)
