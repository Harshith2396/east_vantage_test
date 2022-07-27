import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from geopy.geocoders import Nominatim

from db.database import Database

app = FastAPI()
db = Database()
geoapp = Nominatim(user_agent="location")


class Address(BaseModel):  # data modeling through pydantic
    name: str
    location: str
    coordinates: str


def JsonifyData():  # to jsonify the data
    listData = []
    for data in db.getData():
        listData.append({"id": data[0],
                         "name": data[1],
                         "location": data[2],
                         "coordinates": coordinates(data[2])})

    return listData


@app.post(path="/add/")  # api to add the data
def addOneAddress(address: Address):
    db.insertOne(address.name, address.location, address.coordinates)

    return JsonifyData()


@app.get(path="/get/")  # api to get the data
def getAddress():
    return JsonifyData()


@app.post(path="/update/{id:int}/")  # api to update the data using id
def updateOneAddressById(id, address: Address):
    db.updateData(id=id, data=[address.name, address.location, address.coordinates])

    return JsonifyData()


@app.delete(path="/delete/{id:int}/")  # api to delete the data using id
def deleteOneAddressById(id):
    db.deleteOFromDb(id)

    return JsonifyData()


def coordinates(locationName):  # function to get the coordinates of a location
    location = geoapp.geocode(locationName).raw
    return location


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)  # we use uvicorn to run or host the fast api app
