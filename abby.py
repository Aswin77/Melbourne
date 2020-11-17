import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(suburbs,bedroom2,bathroom,car,buildingarea):
    try:
        loc_index = __data_columns.index(suburbs.lower())
    except:
        loc_index = -1

    z = np.zeros(len(__data_columns))
    z[0] = bedroom2
    z[1] = bathroom
    z[2] = car
    z[3] = buildingarea
    if loc_index >= 0:
        z[loc_index] = 1

    return round(__model.predict([z])[0], 3)

def get_location_names():
    return __locations

def load_saved_artifcats():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    with open("./server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]

    with open("./server/artifacts/HousingPrice.pickle", "rb") as f:
        __model = pickle.load(f)
        print("loading saved artifacts...done")
if __name__ == "__main__":
    load_saved_artifcats()
    print(get_location_names())
    print(get_location_names())
    print(get_estimated_price('abbotsford',2, 1,0,79))


