from random import randint
import sqlite3

class BackEnd(object):

    def security_code(self):
       return randint(1, 1000)



connection = sqlite3.connect("assessment2.db")

sql_select_Query = "select * from map_of_locations"
cursor = connection.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()

locations = {
    'luton_mall' : (records[0][2], records[0][3]),
    'luton_train_station' : (records[1][2], records[1][3]),
    'uni' : (records[2][2], records[2][3]),
    'stockwood_park' : (records[3][2], records[3][3]),
    'wardown_house' : (records[4][2], records[4][3]),
    'bedford_park' : (records[5][2], records[5][3]),
    'barkers_lane' : (records[6][2], records[6][3]),
    'jb_museum' : (records[7][2], records[7][3]),
    'light_pyramid' : (records[8][2], records[8][3]),
    'milton_uni_hospital' : (records[8][2], records[8][3]),
    'milton_computer_museum' : (records[9][2], records[9][3]),
    'milton_ikea' : (records[10][2], records[10][3])
}

import haversine as hs
import distanceCheck as dc

def priceCalc(loc1, loc2):
    if loc1 == loc2:
        print("Locations can't be the same")

    else:
        distance_km = dc.distanceCheck(loc1, loc2)
        trip_price = distance_km * 5
        return format(trip_price, '.2f' ) + ' quid for ' + str(format(distance_km, '.2f')) + ' kilometers'

# print(priceCalc(locations['luton_mall'], locations['stockwood_park']))
# print(priceCalc(locations['milton_ikea'], locations['stockwood_park']))
# print(priceCalc(locations['milton_ikea'], locations['milton_ikea']))