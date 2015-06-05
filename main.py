#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request
import os
import shutil
import re

count = 0
device = "";
resolution = "";
color = "";
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
    command = "scanimage --device-name={:s} --format=tiff -\
-mode={:s} --resolution={:s} >{:d}.tiff".format(device, color, resolution, count)

    os.system(command)

    count = count + 1;
    return render_template("scan.html")

@app.route("/reset")
def resetCmd():
    global count
    count = 0
    return render_template("reset.html")

def extractConf():
    f = open("scanconf.conf", 'r')
    f_content = f.read()
    f.close()

    global device, resolution, color, scanDir

    device = re.split(r'device-name\s?=\s?', \
    re.findall(r'device-name.*=.*\n', f_content)[0])[1].split('\n')[0]

    resolution = re.split(r'resolution\s?=\s?', \
    re.findall(r'resolution.*=.*\n', f_content)[0])[1].split('\n')[0]

    color = re.split(r'color\s?=\s?', \
    re.findall(r'color.*=.*\n', f_content)[0])[1].split('\n')[0]

    scanDir = re.split(r'output-dir\s?=\s?', \
    re.findall(r'output-dir.*=.*\n', f_content)[0])[1].split('\n')[0]



if __name__ == "__main__":
    extractConf() # load the configuration variables from the file
    app.run(host='0.0.0.0')#vizibil tuturor din reteaua locala
