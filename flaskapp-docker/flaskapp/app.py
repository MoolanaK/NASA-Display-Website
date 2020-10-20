from flask import Flask, render_template
import bitmex
app = Flask(__name__)

@app.route("/")
def index():
    client = bitmex.bitmex(test=False)
    res=client.Instrument.Instrument_get(symbol='XBTUSD').response().result
    content2 = res[0]['fundingRate']*100
    return render_template("index.html", content = content2)