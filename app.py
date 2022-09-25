from pymongo import MongoClient
from initMongoDb import initRestaurantsColl
from flask  import Flask

client = MongoClient('127.0.0.1',
                     username='root',
                     password='toor',)
db = client['RestosMiam']
restaurantsCol = db['restaurants']

initRestaurantsColl(restaurantsCol)




app = Flask(__name__)

#Import the flask module

#Create a Flask constructor. It takes name of the current module as the argument

#Create a route decorator to tell the application, which URL should be called for the #described function and define the function

@app.route('/')
def tutorialspoint():
    cursor = restaurantsCol.find({})
    for document in cursor:
          print(document)
#Create the main driver function
if __name__ == '__main__':
#call the run method
    app.run(debug=True,host='0.0.0.0')
