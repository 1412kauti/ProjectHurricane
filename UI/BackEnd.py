from random import randint
import sqlite3
import haversine as hs
import distanceCheck as dc
import datetime
from UserScreen import Ui_Form as ui13

class BackEnd(object):
    """
        Main class with BackEnd functions.
    """
    connection = sqlite3.connect("assessment2.db")

    sql_select_Query = "select * from map_of_locations"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    # dictionary with the locations' coordinates
    locations = {
        'Luton Mall' : (records[0][2], records[0][3]),
        'Luton Train Station' : (records[1][2], records[1][3]),
        'University of Bedfordshire' : (records[2][2], records[2][3]),
        'Stockwood Park' : (records[3][2], records[3][3]),
        'Wardown House Museum and Gallery' : (records[4][2], records[4][3]),
        'Bedford Park' : (records[5][2], records[5][3]),
        "Barker's Lane" : (records[6][2], records[6][3]),
        'John Bunyan Museum and Library' : (records[7][2], records[7][3]),
        'Light Pyramid' : (records[8][2], records[8][3]),
        'Milton Keynes University Hospital' : (records[8][2], records[8][3]),
        'National Museum of Computing' : (records[9][2], records[9][3]),
        'Milton Keynes IKEA ' : (records[10][2], records[10][3])
    }

    def priceCalc(loc1, loc2):
        """
            Calculates the distance form point A to point B.
        :param loc2:
        :return: Distance in km, price for the distance.
        """
        distance_km = dc.distanceCheck(loc1, loc2)
        trip_price = distance_km * 5
        return distance_km, trip_price

    def getDateAndTime(self):
        """
            Get current time.
        :return: date, time
        """
        today = (datetime.date.today())
        now = (datetime.datetime.now())
        current_time = (now.strftime("%H:%M"))
        return str(today), str(current_time)

    def getJourneyID(self):
        """
            Creates journey ID.
        :return: random integer 1 - 10**6
        """
        id = randint(1, 1000000)
        return '#' + str(id)

    def getETA(self):
        """
            Creates ETA.
        :return: random integer 3 - 15
        """
        eta = randint(3, 15)
        return str(eta) + ' minutes'

    def assignTheDriver(self):
        """Returns a rondom driver's name, car number, car make and car color."""
        connection = sqlite3.connect("assessment2.db")
        sql_select_Query = "select * from drivers"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        r = randint(0, len(records) - 1)
        driver = records[r]
        driver_first_name = str(driver[0])
        driver_last_name = str(driver[1])
        car_number = driver[8]
        car_make = driver[9]
        car_color = driver[10]
        return driver_first_name, driver_last_name, car_number, car_make, car_color

    def customerEmailList(self):
        """List with the customers' emails"""
        connection = sqlite3.connect("assessment2.db")

        sql_select_Query = "select * from customers"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        list_of_emails = []
        for record in records:
            list_of_emails.append(record[2])
        return list_of_emails

    def driverEmailList(self):
        """List with the drivers' emails"""
        connection = sqlite3.connect("assessment2.db")

        sql_select_Query = "select * from drivers"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        list_of_emails = []
        for record in records:
            list_of_emails.append(record[2])
        return list_of_emails

    def customerPhoneNumberList(self):
        """List with the customers' phone numbers"""
        connection = sqlite3.connect("assessment2.db")

        sql_select_Query = "select * from customers"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        list_of_phone_numbers = []
        for record in records:
            list_of_phone_numbers.append(record[3])
        return list_of_phone_numbers

    def driverPhoneNumberList(self):
        """List with the drivers' phone numbers"""
        connection = sqlite3.connect("assessment2.db")

        sql_select_Query = "select * from drivers"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        list_of_phone_numbers = []
        for record in records:
            list_of_phone_numbers.append(record[4])
        return list_of_phone_numbers

    def findLastJourney(self):
        """
            Selects the last order.
        :return: start_location, destination, order_id
        """
        connection = sqlite3.connect("assessment2.db")

        sql_select_Query = "select * from journey"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        start_location = records[len(records) - 1][5]
        destination = records[len(records) - 1][6]
        order_id = records[len(records) - 1][2]
        return start_location, destination, order_id

    def getLastRowJourneys(self):
        """
            Get last journey.
        :return: Last row from journey table.
        """
        connection = sqlite3.connect("assessment2.db")

        sql_select_Query = "select * from journey"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        return records[len(records) - 1][2]