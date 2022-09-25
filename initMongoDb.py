import requests
import pandas as pd
import json
from pymongo import MongoClient


yelpAPIKey = 'Bearer LCDj57HpMzWDMxioeRYVuhuN1NlLY04Kagqtfzh_Vx09pYs-To53519ZqAWVR9PuRqxekaJgcxZa01QzGFOkXI7KgOjDhM401RtxGfu0Yv7N9n-k8UY6OONSJ54aY3Yx'
yelpClientId = '7ymC55hnHxZyYnivO4J41Q'

def FetchRestaurants(requestIndex) :
    res = requests.get(
        'https://api.yelp.com/v3/businesses/search?term=restaurant&location=Quebec&limit=50&radius=40000&offset=' + str(requestIndex * 50),
        headers={"Authorization": yelpAPIKey})
    resJson = json.loads(res.text)
    businesses = resJson['businesses']
    return businesses

def initRestaurantsColl(restaurantsCol):
    requestIndex = 0
    businesses = FetchRestaurants(requestIndex)
    justOneFetch = False
    totalNumberOfResto = 0

    while justOneFetch or (len(businesses) > 0 and not justOneFetch) :
        totalNumberOfResto += len(businesses)
        for business in businesses:
            restoId = restaurantsCol.insert_one(business).inserted_id

        print(totalNumberOfResto)
        requestIndex+=1
        businesses = FetchRestaurants(requestIndex)

        if justOneFetch:
            break



