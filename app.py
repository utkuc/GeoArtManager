import os

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(os.environ['CUSTOMCONNSTR_MongoDB'])
db = client.Geoart
@app.route('/')
def hello_world():
    test_dic = db.test.find_one(dict(name="utku"))
    if test_dic is not None:
        return str(test_dic["name2"])
    else:
        return 'Hello World!'


if __name__ == '__main__':
    app.run()
