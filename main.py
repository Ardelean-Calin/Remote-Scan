#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request
import os
import shutil

count = 0
scanDir = "/home/calin/Documents/Scanner"

app = Flask(__name__)

@app.route("/")
def hello(name = None):
    for item in os.listdir():
        if item.endswith(".tiff"):
            shutil.copy(item, scanDir)
            os.remove(item)
    return render_template("index.html", count=count)

@app.route("/scan")
def scanCmd():          # se executa la GET request. cand se incarca pagina
    global count
    print("Scan initiated")
    command = "scanimage --device-name=hpaio:/net/Deskjet_3050_J610_series?zc=HP0BF9DD --format=tiff -\
-mode=Gray --resolution=200 >{:d}.tiff".format(count)

    os.system(command)

    count = count + 1;
    return render_template("scan.html")

@app.route("/reset")
def resetCmd():
    global count
    count = 0
    return render_template("reset.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')#vizibil tuturor din reteaua locala
