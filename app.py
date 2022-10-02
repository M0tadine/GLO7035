from pymongo import MongoClient
from flask  import Flask,jsonify





app = Flask(__name__)

@app.route("/heartbeat")
def hello_world():
    return {'villeChoisie':'Quebec'}


if __name__ == "__main__":
    app.run(host="0.0.0.0",port='5000' debug=True)