import sqlite3
from BackEnd import BackEnd
conn = sqlite3.connect("assessment2.db")
c = conn.cursor()

class dataz():
    @staticmethod
    def Create_Table():
        c.execute("""CREATE TABLE table_name""")
        conn.commit()

    @staticmethod
    def Rename_Table():
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute("ALTER TABLE trip RENAME TO journey")        
        conn.commit()
    @staticmethod
    def Drop_Table():
        c.execute("DROP TABLE table_name")
        conn.commit()

    @staticmethod
    def Insert_Into_customers(z,y,x,w,v,u):
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute('''PRAGMA journal_mode = WAL''')
        c.execute("INSERT INTO customers (first_name,last_name,email,phone_number,password,payment_method) VALUES(?,?,?,?,?,?)",(z,y,x,w,v,u))
        conn.commit()
    
    @staticmethod    
    def Insert_Into_drivers(z,y,x,w,v,u,t,s,r,q,p):
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute('''PRAGMA journal_mode = WAL''')
        c.execute("""INSERT INTO drivers
        (first_name, last_name, email, password, phone_number, driver_license, license_expiry, car_class, car_license_plate_number, car_make, car_colour) VALUES (?,?,?,?,?,?,?,?,?,?)""", (z,y,x,w,v,u,t,s,r,q,p))
        conn.commit()

    @staticmethod
    def Insert_Into_admins():
        c.execute("""INSERT INTO admins
        (first_name, last_name, email, phone_number, password) VALUES ('haos', 'zhong', 'hao123', 07412566921, 'password')""")
        conn.commit()

    @staticmethod
    def Insert_Into_journey(date,time,jID,user_ID, customer_name, start_point,end_point,driver_name,car_number,car_type,car_make,car_color,price,distance):
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute('''PRAGMA journal_mode = WAL''')
        c.execute("""INSERT INTO journey
        (Date, Time, Journey_ID, user_ID, customer_name, start_location, End_Location, driver_name, car_number, Car_Class, Car_Make, Car_Colour, Price, Distance) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""", (date,time,jID,user_ID, customer_name, start_point,end_point,driver_name,car_number,car_type,car_make,car_color,price,distance,))
        conn.commit()

    @staticmethod
    def Insert_into_customer_payments(z,y,x,w,v):
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute('''PRAGMA journal_mode = WAL''')
        c.execute("""INSERT INTO customer_payment
        (name, card_number, cvv, email, password)
        VALUES (?,?,?,?,?)""", (z,y,x,w,v))
        conn.commit()

    @staticmethod
    def Insert_into_driver_payments(z,y,x,w,v,u):
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute("""INSERT INTO driver_payments
        (name, account_number, sort_code, payme_link)
        VALUES (?,?,?,?,?,?)""", (z,y,x,w,v,u))
        conn.commit()

    @staticmethod
    def Delete_Duplicates_Customers():
        c.execute("""DELETE FROM customers
        WHERE rowid NOT IN (SELECT min(rowid) 
        FROM customers GROUP BY first_name,last_name,email,password,phone_number,payment_method)""")
        conn.commit()

    @staticmethod
    def Delete_Duplicates_Drivers():
        c.execute("""DELETE FROM drivers
        WHERE rowid NOT IN (SELECT min(rowid) 
        FROM drivers GROUP BY first_name,last_name,email,phone_number,password,car_make,car_colour,car_license_plate_number,driver_license,license_expiry,bank_account)""")
        conn.commit()

    @staticmethod
    def Delete_Duplicates_Admins():
        c.execute("""DELETE FROM admins
        WHERE rowid NOT IN (SELECT min(rowid) 
        FROM admins GROUP BY first_name,last_name,email,phone_number,password)""")
        conn.commit()

    @staticmethod
    def Check_Duplicates_customers():
        c.execute("""SELECT first_name,last_name,email,phone_number,password,payment_method, COUNT(*)
        FROM customers
        GROUP BY first_name,last_name,email,phone_number,password,payment_method
        HAVING COUNT(*) > 1""")
        print(c.fetchall())
        conn.commit()

    @staticmethod
    def Check_Duplicates_drivers():
        c.execute("""SELECT first_name,last_name,email,phone_number,password,car_make,car_colour,car_license_plate_number,driver_license,license_expiry COUNT(*)
        FROM drivers
        GROUP BY first_name,last_name,email,phone_number,password,car_make,car_colour,car_license_plate_number,driver_license
        HAVING COUNT(*) > 1""")
        print(c.fetchall())
        conn.commit()

    @staticmethod
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
    def get_driver_username_by_id(driver_ID):
        """
            ...
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
    def get_driver_lastname_by_id(driver_ID):
        """
            ...
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
    def get_driver_email_by_id(driver_ID):
        """
            ...
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
    def get_driver_pn_by_id(driver_ID):
        """
            ...
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
    def get_customer_username_by_id(user_ID):
        """
            ...
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
    def get_customer_lastname_by_id(user_ID):
        """
            ...
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
    def get_customer_email_by_id(user_ID):
        """
            ...
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
    def get_customer_phone_number_by_id(user_ID):
        """
            ...
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
    def Update_First_Name_customers(first_name,userID):
        c.execute("""UPDATE customers
        SET first_name = ?
        WHERE user_ID = ?""", (first_name,userID,))
        conn.commit()

    @staticmethod
    def Update_Last_Name_customers(last_name,userID):
        c.execute("""UPDATE customers
        SET last_name = ?
        WHERE user_ID = ?""", (last_name,userID,))
        conn.commit()

    @staticmethod
    def Update_Email_customers(email,userID):
        c.execute("""UPDATE customers
        SET email = ?
        WHERE user_ID = ?""", (email,userID,))
        conn.commit()
        
    @staticmethod
    def Update_phone_number_customers(phone_number,userID):
        c.execute("""UPDATE customers
        SET phone_number = ?
        WHERE user_ID = ?""", (phone_number,userID,))
        conn.commit()

    @staticmethod
    def Update_password_customers(password,userID):
        c.execute("""UPDATE customers
        SET password = ?
        WHERE user_ID = ?""", (password,userID,))
        conn.commit()

    @staticmethod
    def Update_payment_method_customers(payment_method,userID):
        c.execute("""UPDATE customers
        SET payment_method = ?
        WHERE user_ID = ?""", (payment_method,userID,))
        conn.commit()

    @staticmethod
    def Update_first_name_drivers(first_name,driverID):
        c.execute("""UPDATE drivers
        SET first_name = ?
        WHERE driver_ID = ?""", (first_name,driverID,))
        conn.commit()

    @staticmethod
    def Update_last_name_drivers(last_name,driverID):
        c.execute("""UPDATE drivers
        SET last_name = ?
        WHERE driver_ID = ?""", (last_name,driverID,))
        conn.commit()

    @staticmethod
    def Update_phone_number_drivers(phone_number,driverID):
        c.execute("""UPDATE drivers
        SET phone_number = ?
        WHERE driver_ID = ?""", (phone_number,driverID,))
        conn.commit()

    @staticmethod
    def Update_password_drivers(password,driverID):
        c.execute("""UPDATE drivers
        SET password = ?
        WHERE driver_ID = ?""", (password,driverID,))
        conn.commit()

    @staticmethod
    def Update_car_make_drivers(car_make,driverID):
        c.execute("""UPDATE drivers
        SET car_make = 'someone'
        WHERE driver_ID = 1""", (car_make,driverID,))
        conn.commit()

    @staticmethod
    def Update_car_colour_drivers(car_colour,driverID):
        c.execute("""UPDATE drivers
        SET car_colour = ?
        WHERE driver_ID = ?""", (car_colour,driverID,))
        conn.commit()

    @staticmethod
    def Update_driver_license_drivers(driver_license,driverID):
        c.execute("""UPDATE drivers
        SET driver_license = ?
        WHERE driver_ID = ?""", (driver_license,driverID,))
        conn.commit()

    @staticmethod
    def Update_license_expiry_drivers(license_expiry,driverID):
        c.execute("""UPDATE drivers
        SET license_expiry = ?
        WHERE driver_ID = ?""", (license_expiry,driverID,))
        conn.commit()

    @staticmethod
    def Update_bank_account_drivers(bank_account,driverID):
        c.execute("""UPDATE drivers
        SET bank_account = ?
        WHERE driver_ID = ?""", (bank_account,driverID,))
        conn.commit()

    @staticmethod
    def Update_first_name_admins(first_name,employeeID):
        c.execute("""UPDATE admins
        SET first_name = ?
        WHERE employee_ID = ?""", (first_name,employeeID,))
        conn.commit()

    @staticmethod
    def Update_last_name_admins(last_name,employeeID):
        c.execute("""UPDATE admins
        SET last_name = ?
        WHERE employee_ID = ?""", (last_name,employeeID,))
        conn.commit()

    @staticmethod
    def Update_email_admins(email,employeeID):
        c.execute("""UPDATE admins
        SET email = ?
        WHERE employee_ID = ?""", (email,employeeID,))
        conn.commit()

    @staticmethod
    def Update_phone_number_admins(phone_number,employeeID):
        c.execute("""UPDATE admins
        SET phone_number = ?
        WHERE employee_ID = ?""", (phone_number,employeeID,))
        conn.commit()

    @staticmethod
    def Update_password_admins(password,employeeID):
        c.execute("""UPDATE admins
        SET password = ?
        WHERE employee_ID = ?""", (password,employeeID,))
        conn.commit()
        
    @staticmethod
    def update_userID_by_name_journey():
        c.execute("""UPDATE journey
        SET user_ID = (SELECT user_ID FROM customers WHERE journey.customer_name = customers.first_name)""")
        conn.commit()

    @staticmethod
    def Update_date_journey(date,journeyID):
        c.execute("""UPDATE journey
        SET date = ?
        WHERE journey_ID = ?""", (date,journeyID,))
        conn.commit()

    @staticmethod
    def Update_time_journey(time,journeyID):
        c.execute("""UPDATE journey
        SET time = ?
        WHERE journey_ID = ?""", (time,journeyID,))
        conn.commit()

    @staticmethod
    def Update_start_location_journey(start_location,journeyID):
        c.execute("""UPDATE journey
        SET start_location = ?
        WHERE journey_ID = ?""", (start_location,journeyID,))
        conn.commit()

    @staticmethod
    def Update_end_location_journey(end_location,journeyID):
        c.execute("""UPDATE journey
        SET end_location = ?
        WHERE journey_ID = ?""", (end_location,journeyID,))
        conn.commit()

    @staticmethod
    def Update_car_class_journey(car_class,journeyID):
        c.execute("""UPDATE journey
        SET Car_Class = ?
        WHERE journey_ID = ?""", (car_class,journeyID,))
        conn.commit()

    @staticmethod
    def Update_car_make_journey(car_make,journeyID):
        c.execute("""UPDATE journey
        SET Car_Make = ?
        WHERE journey_ID = ?""", (car_make,journeyID,))
        conn.commit()

    @staticmethod
    def Update_car_colour_journey(car_colour,journeyID):
        c.execute("""UPDATE journey
        SET Car_Colour = ?
        WHERE journey_ID = ?""", (car_colour,journeyID,))
        conn.commit()

    @staticmethod
    def Update_price_journey(price,journeyID):
        c.execute("""UPDATE journey
        SET Price = ?
        WHERE journey_ID = ?""", (price,journeyID,))
        conn.commit()

    @staticmethod
    def Update_distance_journey(distance,journeyID):
        c.execute("""UPDATE journey
        SET Distance = ?
        WHERE journey_ID = ?""", (distance,journeyID,))
        conn.commit()

    @staticmethod
    def Update_status_journey(status,journeyID):
        c.execute("""UPDATE journey
        SET status = ?
        WHERE journey_ID = ?""", (status,journeyID,))
        conn.commit()

    @staticmethod
    def update_userID_by_email_customers_payments():
        c.execute("""UPDATE customer_payment
        SET user_ID = (SELECT user_ID FROM customers WHERE customer_payment.email = customers.email)""")
        conn.commit()

    @staticmethod
    def update_userID_by_name_customers_payments():
        c.execute("""UPDATE customer_payment
        SET user_ID = (SELECT user_ID FROM customers WHERE customer_payment.name = customers.first_name)""")
        conn.commit()

    @staticmethod
    def Update_name_customer_payment(name,userID):
        c.execute("""UPDATE customer_payment
        SET name = ?
        WHERE user_ID = ?""", (name,userID,))
        conn.commit()

    @staticmethod
    def Update_card_number_customer_payment(card_number,userID):
        c.execute("""UPDATE customer_payment
        SET card_number = ?
        WHERE user_ID = ?""", (card_number,userID,))
        conn.commit()

    @staticmethod
    def Update_cvv_customer_payment(cvv,userID):
        c.execute("""UPDATE customer_payment
        SET cvv = ?
        WHERE user_ID = ?""", (cvv,userID,))
        conn.commit()

    @staticmethod
    def Update_email_customer_payment(email,userID):
        c.execute("""UPDATE customer_payment
        SET email = ?
        WHERE user_ID = ?""", (email,userID,))
        conn.commit()

    @staticmethod
    def Update_password_customer_payment(password,userID):
        c.execute("""UPDATE customer_payment
        SET password = ?
        WHERE user_ID = ?""", (password,userID,))
        conn.commit()

    @staticmethod
    def update_driverID_by_email_driver_payment():
        c.execute("""UPDATE driver_payment
        SET driver_ID = (SELECT driver_ID FROM drivers WHERE driver_payment.email = drivers.email)""")
        conn.commit()

    @staticmethod
    def update_driverID_by_email_driver_payment():
        c.execute("""UPDATE driver_payment
        SET driver_ID = (SELECT driver_ID FROM drivers WHERE driver_payment.name = drivers.first_name)""")
        conn.commit()

    @staticmethod
    def Update_name_driver_payments(name,driverID):
        c.execute("""UPDATE driver_payments
        SET name = ?
        WHERE driver_ID = ?""", (name,driverID,))
        conn.commit()

    @staticmethod
    def Update_account_number_driver_payments(account_number,driverID):
        c.execute("""UPDATE driver_payments
        SET account_number = ?
        WHERE driver_ID = ?""", (account_number,driverID,))
        conn.commit()

    @staticmethod
    def Update_sort_code_driver_payments(sort_code,driverID):
        c.execute("""UPDATE driver_payments
        SET sort_code = ?
        WHERE driver_ID = ?""", (sort_code,driverID,))
        conn.commit()

    @staticmethod
    def Update_payme_link_driver_payments(payme_link,driverID):
        c.execute("""UPDATE driver_payments
        SET payme_link = ?
        WHERE driver_ID = ?""", (payme_link,driverID,))
        conn.commit()

    @staticmethod
    def Delete_Row_customers(rowid):
        c.execute("DELETE FROM customers where rowid = ?", (rowid,))
        conn.commit()

    @staticmethod
    def Delete_Row_drivers(rowid):
        c.execute("DELETE FROM drivers where rowid = ?", (rowid,))
        conn.commit()

    @staticmethod
    def Delete_Row_admins(rowid):
        c.execute("DELETE FROM admins where rowid = ?", (rowid,))
        conn.commit()

    @staticmethod
    def Delete_Row_journey(jID):
        c.execute("DELETE FROM journey where Journey_ID = ?", (jID,))
        conn.commit()

    @staticmethod
    def Read_From_customer_payment():
        c.execute("SELECT*FROM customer_payment")
        print(c.fetchall())
        conn.commit()

    @staticmethod
    def Read_From_Customers():
        c.execute("SELECT*FROM customers")
        print(c.fetchall())
        conn.commit()

    @staticmethod
    def Read_From_Drivers():
        c.execute("SELECT*FROM drivers")
        print(c.fetchall())
        conn.commit()

    @staticmethod
    def Read_From_Admins():
        c.execute("SELECT*FROM admins")
        print(c.fetchall())
        conn.commit()

    @staticmethod
    def Read_From_Journey():
        c.execute("SELECT*FROM journey")
        print(c.fetchall())
        conn.commit()

    @staticmethod
    def Update_something_by_admin(table, column, row, value):
        c.execute(f"""UPDATE {table}
        SET {column} = ?
        WHERE rowID = ?;""", (value, row,))
        conn.commit()

    @staticmethod
    def create_row_by_admin(table):
        dv = 'new'
        if table == 'Journey':
            dataz().Insert_Into_journey(dv,dv,dv,dv,dv,dv,dv,dv,dv,dv,dv,dv,dv,dv)
        elif table == 'Customers':
            dataz().Insert_Into_customers(dv,dv,dv,dv,dv,dv)
        elif table == 'Drivers':
            dataz().Insert_Into_drivers(dv,dv,dv,dv,dv,dv,dv,dv,dv,dv,dv)


    @staticmethod
    def Delete_Row_by_admin(table, row):
        c.execute(f"DELETE FROM {table} where rowid = ?", (row,))
        conn.commit()

v = dataz
v.create_row_by_admin('Journey')
v.create_row_by_admin('Customers')
v.create_row_by_admin('Drivers')