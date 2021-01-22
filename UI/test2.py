import sqlite3
from BackEnd import BackEnd
conn = sqlite3.connect("assessment2.db")
c = conn.cursor()

class dataz():
    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Create_Table():
        c.execute("""CREATE TABLE table_name""")
        """
        this function is used to create tables 
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Rename_Table():
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute("ALTER TABLE trip RENAME TO journey")
        """
        function to rename a table has
        """    
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Drop_Table():
        c.execute("DROP TABLE table_name")
        """
        used to delete/drop a table
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Insert_Into_customers(z,y,x,w,v,u):
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute('''PRAGMA journal_mode = WAL''')
        c.execute("INSERT INTO customers (first_name,last_name,email,phone_number,password,payment_method) VALUES(?,?,?,?,?,?)",(z,y,x,w,v,u))
        """
        used to put infomation from the graphical user interface into the customers table in the database
        """
        conn.commit()
    
    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.    
    def Insert_Into_drivers(z,y,x,w,v,u,t,s,r,q,p):
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute('''PRAGMA journal_mode = WAL''')
        c.execute("""INSERT INTO drivers
        (first_name, last_name, email, password, phone_number, driver_license, license_expiry, car_class, car_license_plate_number, car_make, car_colour) VALUES (?,?,?,?,?,?,?,?,?,?,?)""", (z,y,x,w,v,u,t,s,r,q,p))
        """
        used to put infomation from the graphical user interface into the drivers table in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Insert_Into_journey(date,time,jID,user_ID, customer_name, start_point,end_point,driver_ID, driver_name,car_number,car_type,car_make,car_color,price,distance):
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute('''PRAGMA journal_mode = WAL''')
        c.execute("""INSERT INTO journey
        (Date, Time, Journey_ID, user_ID, customer_name, start_location, End_Location, driver_ID, driver_name, car_number, Car_Class, Car_Make, Car_Colour, Price, Distance) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (date,time,jID,user_ID, customer_name, start_point,end_point, driver_ID, driver_name,car_number,car_type,car_make,car_color,price,distance,))
        """
        used to put infomation form the graphical user interface into the journey table in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Delete_Duplicates_Customers():
        c.execute("""DELETE FROM customers
        WHERE rowid NOT IN (SELECT min(rowid) 
        FROM customers GROUP BY first_name,last_name,email,password,phone_number,payment_method)""")
        """
        use to delete duplicate data enters from the customers table in the database if they appear
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Delete_Duplicates_Drivers():
        c.execute("""DELETE FROM drivers
        WHERE rowid NOT IN (SELECT min(rowid) 
        FROM drivers GROUP BY first_name,last_name,email,phone_number,password,car_make,car_colour,car_license_plate_number,driver_license,license_expiry)""")
        """
        use to delete dupilates data enters from the drivers table in the database if they appear
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Check_Duplicates_customers():
        c.execute("""SELECT first_name,last_name,email,phone_number,password,payment_method, COUNT(*)
        FROM customers
        GROUP BY first_name,last_name,email,phone_number,password,payment_method
        HAVING COUNT(*) > 1""")
        """
        checks if there is a duplicate in the customers table in the database
        """
        print(c.fetchall())
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Check_Duplicates_drivers():
        c.execute("""SELECT first_name,last_name,email,phone_number,password,car_make,car_colour,car_license_plate_number,driver_license,license_expiry COUNT(*)
        FROM drivers
        GROUP BY first_name,last_name,email,phone_number,password,car_make,car_colour,car_license_plate_number,driver_license
        HAVING COUNT(*) > 1""")
        """
        checks if there is a duplicate in the drivers table in the database
        """
        print(c.fetchall())
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_customer_userID_by_phone_number(phone_number):
        """
            Takes a phone number as an input. And returns a userID connected do it in the DB.
        :param phone_number:
        :return: user_ID
        """
        if phone_number != '':
            c.execute("""SELECT phone_number, user_ID
            FROM customers
            WHERE phone_number = ?""", (phone_number,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_driver_username_by_id(driver_ID):
        """
            takes the driverID as an input and returns the driver's first name from the database
            used for the profile
        """
        if driver_ID != '':
            c.execute("""SELECT driver_ID, first_name
                FROM drivers
                WHERE driver_ID = ?""", (driver_ID,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_driver_lastname_by_id(driver_ID):
        """
            takes the driverId as an input and returns the driver's last name from the database
            used for the profile
        """
        if driver_ID != '':
            c.execute("""SELECT driver_ID, last_name
                    FROM drivers
                    WHERE driver_ID = ?""", (driver_ID,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_driver_email_by_id(driver_ID):
        """
            takes the driverID as an input and returns the driver's email from the database
            used for the profile
        """
        if driver_ID != '':
            c.execute("""SELECT driver_ID, email
                        FROM drivers
                        WHERE driver_ID = ?""", (driver_ID,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_driver_pn_by_id(driver_ID):
        """
            takes the driverID as an input and returns the driver's phone number 
        """
        if driver_ID != '':
            c.execute("""SELECT driver_ID, phone_number
                        FROM drivers
                        WHERE driver_ID = ?""", (driver_ID,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_customer_userID_by_email(email):
        """
            Takes an email as an input. And returns a userID connected do it in the DB.
        :param email:
        :return: user_ID
        """
        if email != '':
            c.execute("""SELECT email, user_ID
            FROM customers
            WHERE email = ?""", (email,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_customer_userID_by_password(password):
        """
            Takes a password as an input. And returns a userID connected do it in the DB.
        :param password:
        :return: user_ID
        """
        if password != '':
            c.execute("""SELECT email,password,user_ID
            FROM customers
            WHERE password = ?""", (password,))
            var = c.fetchone()
            conn.commit()
            return var[2]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_driver_driverID_by_password(password):
        """
            Takes a password as an input. And returns a driverID connected do it in the DB.
        :param password:
        :return: driver_ID
        """
        if password != '':
            c.execute("""SELECT email,password,driver_ID
            FROM drivers
            WHERE password = ?""", (password,))
            var = c.fetchone()
            conn.commit()
            return var[2]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_driver_driverID_by_email(email):
        """
            Takes an email as an input. And returns a driverID connected do it in the DB.
        :param email:
        :return: driver_ID
        """
        if email != '':
            c.execute("""SELECT email, driver_ID
            FROM drivers
            WHERE email = ?""", (email,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_driver_driverID_by_phone_number(phone_number):
        """
            Takes a phone number as an input. And returns a driverID connected do it in the DB.
        :param phone_number:
        :return: driver_ID
        """
        if phone_number != '':
            c.execute("""SELECT phone_number, driver_ID
            FROM drivers
            WHERE phone_number = ?""", (phone_number,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_driver_driverID_by_first_name(first_name):
        """
            Takes a phone number as an input. And returns a driverID connected do it in the DB.
        :param phone_number:
        :return: driver_ID
        """
        if first_name != '':
            c.execute("""SELECT first_name, driver_ID
                FROM drivers
                WHERE first_name = ?""", (first_name,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_customer_username_by_id(user_ID):
        """
            takes the customerID as an input and return the customer's first name from the database
            used for the profile
        """
        if user_ID != '':
            c.execute("""SELECT user_ID, first_name
                    FROM customers
                    WHERE user_ID = ?""", (user_ID,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_customer_lastname_by_id(user_ID):
        """
            take the customerId as the input and returns the custoemr's last name from the database
            used to create the profile
        """
        if user_ID != '':
            c.execute("""SELECT user_ID, last_name
                        FROM customers
                        WHERE user_ID = ?""", (user_ID,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_customer_email_by_id(user_ID):
        """
            takes the customerID as the input and returns the customer's email from the database
            used for the profile
        """
        if user_ID != '':
            c.execute("""SELECT user_ID, email
                            FROM customers
                            WHERE user_ID = ?""", (user_ID,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def get_customer_phone_number_by_id(user_ID):
        """
            take the customerID as the input and returns the customer's phone_number from the database
            used for the profile
        """
        if user_ID != '':
            c.execute("""SELECT user_ID, phone_number
                            FROM customers
                            WHERE user_ID = ?""", (user_ID,))
            var = c.fetchone()
            conn.commit()
            return var[1]
        else:
            raise OSError("User doesn't exist")

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def input_card_infoamtion_customers(name,number,cvv,first_name):
        c.execute("""UPDATE customers
        SET card_name = ?, card_number = ?, CVV = ? 
        WHERE first_name = ?""", (name,number,cvv,first_name,))
        """
        inputs the card infomation of a specfic customer into the correct row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def input_paypal_infoamtion_customers(paypal_email,paypal_password,first_name):
        c.execute("""UPDATE customers
        SET paypal_email = ?, paypal_password = ?
        WHERE first_name = ?""", (paypal_email,paypal_password,first_name,))
        """
        inputs the paypal infomation of a specfic customer into the correct row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_First_Name_customers(first_name,userID):
        c.execute("""UPDATE customers
        SET first_name = ?
        WHERE user_ID = ?""", (first_name,userID,))
        """
        used to update a customer's first name in a specific row
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_Card_customers(name,number,cvv,userID):
        c.execute("""UPDATE customers
        SET card_name = ?, card_number = ?, CVV = ?
        WHERE user_ID = ?""", (name,number,cvv,userID,))
        """
        uesed to updates the card infomation of a specfic customer in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_Paypal_customers(email,password,userID):
        c.execute("""UPDATE customers
        SET paypal_email = ?, paypal_password = ?
        WHERE user_ID = ?""", (email,password,userID,))
        """
        used to updates the paypal infomation of a specific customer in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_Last_Name_customers(last_name,userID):
        c.execute("""UPDATE customers
        SET last_name = ?
        WHERE user_ID = ?""", (last_name,userID,))
        """
        used to update a customer's last name in a specific row of the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_Email_customers(email,userID):
        c.execute("""UPDATE customers
        SET email = ?
        WHERE user_ID = ?""", (email,userID,))
        """
        used to update the email of a customer on a specific row of the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_Email_drivers(email,userID):
        c.execute("""UPDATE drivers
        SET email = ?
        WHERE driver_ID = ?""", (email,userID,))
        """
        used to update the email of a driver on a specific row of the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_phone_number_customers(phone_number,userID):
        c.execute("""UPDATE customers
        SET phone_number = ?
        WHERE user_ID = ?""", (phone_number,userID,))
        """
        used to update the phone number of a customer on a specific row of the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_password_customers(password,userID):
        c.execute("""UPDATE customers
        SET password = ?
        WHERE user_ID = ?""", (password,userID,))
        """
        used to update the password of a customer on a specific row of the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_payment_method_customers(payment_method,userID):
        c.execute("""UPDATE customers
        SET payment_method = ?
        WHERE user_ID = ?""", (payment_method,userID,))
        """
        used to update the payment methord of a customer on a specific row of the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def input_card_infomation_drivers(name,number,code,first_name):
        c.execute("""UPDATE drivers
        SET account_name = ?, acccount_number = ? , sort_code = ? 
        WHERE first_name = ?""", (name,number,code,first_name,))
        """
        inputs the card infomation of a specific driver into the correct row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def input_paypal_infomation_drivers(payme_link,first_name):
        c.execute("""UPDATE drivers
        SET payme_link = ?
        WHERE first_name = ?""", (payme_link,first_name,))
        """
        inputs the paypal infomation of a specific driver into the correct row in the database
        """
        conn.commit()        

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_first_name_drivers(first_name,driverID):
        c.execute("""UPDATE drivers
        SET first_name = ?
        WHERE driver_ID = ?""", (first_name,driverID,))
        """
        updates the first name of a driver on a specific row of the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_Card_drivers(name,number,code,driverID):
        c.execute("""UPDATE drivers
        SET account_name = ?, acccount_number = ? , sort_code = ?
        WHERE driver_ID = ?""", (name,number,code,driverID,))
        """
        used to update the card infomation of a specific driver in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_Paypal_drivers(payme,driverID):
        c.execute("""UPDATE drivers
        SET payme_link = ?
        WHERE driver_ID = ?""", (payme,driverID,))
        """
        used to update the paypal infomation of a specific driver the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_last_name_drivers(last_name,driverID):
        c.execute("""UPDATE drivers
        SET last_name = ?
        WHERE driver_ID = ?""", (last_name,driverID,))
        """
        updates the  last name of a driver on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_phone_number_drivers(phone_number,driverID):
        c.execute("""UPDATE drivers
        SET phone_number = ?
        WHERE driver_ID = ?""", (phone_number,driverID,))
        """
        update the phone number of a driver on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_password_drivers(password,driverID):
        c.execute("""UPDATE drivers
        SET password = ?
        WHERE driver_ID = ?""", (password,driverID,))
        """
        update the password of a driver on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_car_make_drivers(car_make,driverID):
        c.execute("""UPDATE drivers
        SET car_make = 'someone'
        WHERE driver_ID = 1""", (car_make,driverID,))
        """
        update the car make of a driver on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_car_colour_drivers(car_colour,driverID):
        c.execute("""UPDATE drivers
        SET car_colour = ?
        WHERE driver_ID = ?""", (car_colour,driverID,))
        """
        update the car colour of a driver on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_driver_license_drivers(driver_license,driverID):
        c.execute("""UPDATE drivers
        SET driver_license = ?
        WHERE driver_ID = ?""", (driver_license,driverID,))
        """
        updates the driver license of a driver on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_license_expiry_drivers(license_expiry,driverID):
        c.execute("""UPDATE drivers
        SET license_expiry = ?
        WHERE driver_ID = ?""", (license_expiry,driverID,))
        """
        update the license expiry of a driver on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_bank_account_drivers(bank_account,driverID):
        c.execute("""UPDATE drivers
        SET bank_account = ?
        WHERE driver_ID = ?""", (bank_account,driverID,))
        """
        up the bank account for a driver on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_date_journey(date,journeyID):
        c.execute("""UPDATE journey
        SET date = ?
        WHERE journey_ID = ?""", (date,journeyID,))
        """
        update the date in journey table on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_time_journey(time,journeyID):
        c.execute("""UPDATE journey
        SET time = ?
        WHERE journey_ID = ?""", (time,journeyID,))
        """
        update time in the journey table on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_start_location_journey(start_location,journeyID):
        c.execute("""UPDATE journey
        SET start_location = ?
        WHERE journey_ID = ?""", (start_location,journeyID,))
        """
        update start location on journey table on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_end_location_journey(end_location,journeyID):
        c.execute("""UPDATE journey
        SET end_location = ?
        WHERE journey_ID = ?""", (end_location,journeyID,))
        """
        update end location on the journey table on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_car_class_journey(car_class,journeyID):
        c.execute("""UPDATE journey
        SET Car_Class = ?
        WHERE journey_ID = ?""", (car_class,journeyID,))
        """
        update car class on the journey table on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_car_make_journey(car_make,journeyID):
        c.execute("""UPDATE journey
        SET Car_Make = ?
        WHERE journey_ID = ?""", (car_make,journeyID,))
        """
        update car make on the journey table on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_car_colour_journey(car_colour,journeyID):
        c.execute("""UPDATE journey
        SET Car_Colour = ?
        WHERE journey_ID = ?""", (car_colour,journeyID,))
        """
        update car colour on the journey table on a specific row in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_price_journey(price,journeyID):
        c.execute("""UPDATE journey
        SET Price = ?
        WHERE journey_ID = ?""", (price,journeyID,))
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_distance_journey(distance,journeyID):
        c.execute("""UPDATE journey
        SET Distance = ?
        WHERE journey_ID = ?""", (distance,journeyID,))
        """
        update distance on the journey table on a specific row of the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_status_journey(status,journeyID):
        c.execute("""UPDATE journey
        SET status = ?
        WHERE journey_ID = ?""", (status,journeyID,))
        """
        update statuse on the journey table on a specific row of the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Delete_Row_customers(rowid):
        c.execute("DELETE FROM customers where rowid = ?", (rowid,))
        """
        deletes a specific row of the customer table
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Delete_Row_drivers(rowid):
        c.execute("DELETE FROM drivers where rowid = ?", (rowid,))
        """
        deletes a specific row on the driver table in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Delete_Row_journey(jID):
        c.execute("DELETE FROM journey where Journey_ID = ?", (jID,))
        """
        deletes a specific row on the journey table in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Read_From_Customers():
        c.execute("SELECT*FROM customers")
        print(c.fetchall())
        """
        reads all the data from the customers table in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Read_From_Drivers():
        c.execute("SELECT*FROM drivers")
        print(c.fetchall())
        """
        reads all the data from the drivers table in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Read_From_Journey():
        c.execute("SELECT*FROM journey")
        print(c.fetchall())
        """
        read all the data from the journey table in the database
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_something_by_admin(table, column, row, value):
        c.execute(f"""UPDATE {table}
        SET {column} = ?
        WHERE rowID = ?;""", (value, row,))
        """
        used to update values on specific row of the database through the graphical user interface
        """
        conn.commit()

    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def create_row_by_admin(table):
        dv = 'new'
        if table == 'Journeys':
            dataz().Insert_Into_journey(dv,dv,dv,dv,dv,dv,dv,dv,dv,dv,dv,dv,dv,dv, dv)
        elif table == 'Customers':
            dataz().Insert_Into_customers(dv,dv,dv,dv,dv,dv)
        elif table == 'Drivers':
            dataz().Insert_Into_drivers(dv,dv,dv,dv,dv,dv,dv,dv,dv,dv,dv)
            """
            used to create a new row in other table in the database through the admin graphical user interface the data in that row can also be mannuly changed by the admin
            """


    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Delete_Row_by_admin(table, row):
        c.execute(f"DELETE FROM {table} where rowid = ?", (row,))
        """
        the admin can delete specific row in any table in the database through the graphical user interface
        """
        conn.commit()
    
    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def Update_journey_status(status,id):
        c.execute("""UPDATE journey
        SET status = ?
        WHERE user_ID = ?""", (status,id,))
        """
        update journey status on the journey table on a specific row in the database with customer name as reference
        """
        conn.commit()
    
    @staticmethod
    #staticmethod is used here to make sure that this function can't interact with parts of the database i don't want it to.
    def customer_name_journey(user_id):
        c.execute("""SELECT customer_name FROM journey WHERE user_ID = ?""", (user_id,))
        """
        update journey status on the journey table on a specific row in the database with customer name as reference
        """
        conn.commit()
v = dataz
