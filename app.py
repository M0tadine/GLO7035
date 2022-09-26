from pymongo import MongoClient
from flask  import Flask,jsonify









app = Flask(__name__)

@app.route("/")
def hello_world():
    client = MongoClient('127.0.0.1',
                     username='root',
                     password='toor',)
    db = client['RestosMiam']
    restaurantsCol = db['restaurants']
    return str(restaurantsCol.count_documents({}))
