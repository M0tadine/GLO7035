def FetchRestaurants(requestIndex) :
    res = requests.get(
        'https://api.yelp.com/v3/businesses/search?term=restaurant&location=Quebec&limit=50&radius=40000&offset=' + str(requestIndex * 50),
        headers={"Authorization": yelpAPIKey})
    resJson = json.loads(res.text)
    businesses = resJson['businesses']
    return businesses

def initRestaurantsColl():
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

    cursor = restaurantsCol.find({})
    for document in cursor:
        print(document)


