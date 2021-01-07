from random import randint
import sqlite3
import haversine as hs
import distanceCheck as dc

class BackEnd(object):

    def security_code(self):
       return randint(1, 1000)



    connection = sqlite3.connect("assessment2.db")

    sql_select_Query = "select * from map_of_locations"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    locations = {
        'Luton mall' : (records[0][2], records[0][3]),
        'Luton train station' : (records[1][2], records[1][3]),
        'University of Bedfordshire' : (records[2][2], records[2][3]),
        'Stockwood park' : (records[3][2], records[3][3]),
        'Wardown house museum' : (records[4][2], records[4][3]),
        'Bedford park' : (records[5][2], records[5][3]),
        'Barkers lane' : (records[6][2], records[6][3]),
        'John Bunyan Museum and Library' : (records[7][2], records[7][3]),
        'Light Pyramid' : (records[8][2], records[8][3]),
        'Milton Keynes University Hospital' : (records[8][2], records[8][3]),
        'National Museum of Computing' : (records[9][2], records[9][3]),
        'milton keynes IKEA' : (records[10][2], records[10][3])
    }

    def priceCalc(loc1, loc2):
            distance_km = dc.distanceCheck(loc1, loc2)
            trip_price = distance_km * 5
            #print(distance_km, trip_price)
            return distance_km, trip_price


BackEnd.priceCalc(BackEnd.locations['National Museum of Computing'], BackEnd.locations['University of Bedfordshire'])
