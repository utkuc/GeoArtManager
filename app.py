import os

from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient(os.environ['CUSTOMCONNSTR_MongoDB'])
db = client.Geoart
@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
