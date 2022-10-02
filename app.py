from pymongo import MongoClient
from flask  import Flask,jsonify





app = Flask(__name__)

@app.route("/heartbeat")
def hello_world():
    return {'villeChoisie':'Quebec'}
