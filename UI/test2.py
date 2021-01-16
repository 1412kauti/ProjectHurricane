import sqlite3
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
    def Insert_Into_journey(date,time,jID,start_point,end_point,driver_name,car_type,car_make,car_color,price,distance):
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute('''PRAGMA journal_mode = WAL''')
        c.execute("""INSERT INTO journey
        (Date, Time, Journey_ID, Start_Location, End_Location, driver_name, Car_Class, Car_Make, Car_Colour, Price, Distance, status) VALUES (?,?,?,?,?,?,?,?,?,?,?)""", (date,time,jID,start_point,end_point,driver_name,car_type,car_make,car_color,price,distance))
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
    def Insert_Into_orders(z,y,x):
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()
        c.execute('''PRAGMA journal_mode = WAL''')
        c.execute("""INSERT INTO orders
        (start_location, end_location, order_ID)
        VALUES (?,?,?)""",(z,y,x,))
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
    def update_userID_customers_payments():
        c.execute("""UPDATE customer_payment
        SET user_ID = (SELECT user_ID FROM customers WHERE customer_payment.email = customers.email)""")
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
    def Check_phone_number_drivers(phone_number):
        c.execute("""SELECT phone_number
        FROM drivers
        WHERE phone_number = ?""", (phone_number,))
        var = c.fetchone()
        conn.commit()

    @staticmethod
    def Update_Last_Name_customers():
        c.execute("""UPDATE customers
        SET last_name = 'someone'
        WHERE user_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_Email_customers():
        c.execute("""UPDATE customers
        SET email = 'someone_email'
        WHERE user_ID = 1""")
        conn.commit()
        
    @staticmethod
    def Update_phone_number_customers():
        c.execute("""UPDATE customers
        SET phone_number = '07412566921'
        WHERE user_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_password_customers():
        c.execute("""UPDATE customers
        SET password = '07412566921'
        WHERE user_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_payment_method_customers():
        c.execute("""UPDATE customers
        SET payment_method = '07412566921'
        WHERE user_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_first_name_drivers():
        c.execute("""UPDATE drivers
        SET first_name = 'someone'
        WHERE driver_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_last_name_drivers():
        c.execute("""UPDATE drivers
        SET last_name = 'someone'
        WHERE driver_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_phone_number_drivers():
        c.execute("""UPDATE drivers
        SET phone_number = '07412566921'
        WHERE driver_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_password_drivers():
        c.execute("""UPDATE drivers
        SET password = 'someone'
        WHERE driver_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_car_make_drivers():
        c.execute("""UPDATE drivers
        SET car_make = 'someone'
        WHERE driver_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_car_colour_drivers():
        c.execute("""UPDATE drivers
        SET car_colour = 'someone'
        WHERE driver_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_first_driver_license_drivers():
        c.execute("""UPDATE drivers
        SET driver_license = 'someone'
        WHERE driver_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_license_expiry_drivers():
        c.execute("""UPDATE drivers
        SET license_expiry = 'someone'
        WHERE driver_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_bank_account_drivers():
        c.execute("""UPDATE drivers
        SET bank_account = 'someone'
        WHERE driver_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_first_name_admins():
        c.execute("""UPDATE admins
        SET first_name = 'someone'
        WHERE employee_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_last_name_admins():
        c.execute("""UPDATE admins
        SET last_name = 'someone'
        WHERE employee_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_email_admins():
        c.execute("""UPDATE admins
        SET email = 'someone'
        WHERE employee_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_phone_number_admins():
        c.execute("""UPDATE admins
        SET phone_number = 'someone'
        WHERE employee_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_password_admins():
        c.execute("""UPDATE admins
        SET password = 'someone'
        WHERE employee_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_date_created_journey():
        c.execute("""UPDATE journey
        SET last_name = 'someone'
        WHERE order_ID = 1""")
        conn.commit()
    
    @staticmethod
    def Update_customer_ID_journey():
        c.execute("""UPDATE journey
        SET customer_ID = 'someone'
        WHERE order_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_driver_name_journey():
        c.execute("""UPDATE journey
        SET driver_name = 'someone'
        WHERE order_ID = 1""")
        conn.commit()
    
    @staticmethod
    def Update_status_journey():
        c.execute("""UPDATE journey
        SET status = 'someone'
        WHERE order_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_driver_ID_journey():
        c.execute("""UPDATE journey
        SET driver_ID = 'someone'
        WHERE order_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_start_piont_journey():
        c.execute("""UPDATE journey
        SET start_piont = 'someone'
        WHERE order_ID = 1""")
        conn.commit()

    @staticmethod
    def Update_end_piont_journey():
        c.execute("""UPDATE journey
        SET end_piont = 'someone'
        WHERE order_ID = 1""")
        conn.commit

    @staticmethod
    def Update_price_journey():
        c.execute("""UPDATE journey
        SET price = 'someone'
        WHERE order_ID = 1""")
        conn.commit()


    @staticmethod
    def Update_customer_number_journey():
        c.execute("""UPDATE journey
        SET customer_number = 'someone'
        WHERE order_ID = 1""")
        conn.commit()
        
    @staticmethod
    def Update_name_customer_payment():
        c.execute("""UPDATE customer_payment
        SET name = 'someone'
        WHERE rowid = 1""")
        conn.commit()

    @staticmethod
    def Update_card_customer_payment():
        c.execute("""UPDATE customer_payment
        SET card_number = 'someone'
        WHERE rowid = 1""")
        conn.commit()

    @staticmethod
    def Update_cvv_customer_payment():
        c.execute("""UPDATE customer_payment
        SET cvv = 'someone'
        WHERE rowid = 1""")
        conn.commit()

    @staticmethod
    def Update_email_customer_payment():
        c.execute("""UPDATE customer_payment
        SET email = 'someone'
        WHERE rowid = 1""")
        conn.commit()

    @staticmethod
    def Update_password_customer_payment():
        c.execute("""UPDATE customer_payment
        SET password = 'someone'
        WHERE rowid = 1""")
        conn.commit()

    @staticmethod
    def Update_name_driver_payments():
        c.execute("""UPDATE driver_payments
        SET name = 'someone'
        WHERE rowid = 1""")
        conn.commit()

    @staticmethod
    def Update_account_number_driver_payments():
        c.execute("""UPDATE driver_payments
        SET account_number = 'someone'
        WHERE rowid = 1""")
        conn.commit()

    @staticmethod
    def Update_sort_code_driver_payments():
        c.execute("""UPDATE driver_payments
        SET sort_code = 'someone'
        WHERE rowid = 1""")
        conn.commit()

    @staticmethod
    def Update_payme_link_driver_payments():
        c.execute("""UPDATE driver_payments
        SET payme_link = 'someone'
        WHERE rowid = 1""")
        conn.commit()

    @staticmethod
    def Update_name_driver_payments():
        c.execute("""UPDATE driver_payments
        SET name = 'someone'
        WHERE rowid = 1""")
        conn.commit()

    @staticmethod
    def Delete_Row_customers():
        c.execute("DELETE FROM customers where rowid = 1")
        conn.commit()

    @staticmethod
    def Delete_Row_drivers():
        c.execute("DELETE FROM drivers where rowid = 1")
        conn.commit()

    @staticmethod
    def Delete_Row_admins():
        c.execute("DELETE FROM admins where rowid = 1")
        conn.commit()

    @staticmethod
    def Delete_Row_journey():
        c.execute("DELETE FROM journey where rowid = 1")
        conn.commit()

    @staticmethod
    def Delete_Row_orders(rowid):
        c.execute("DELETE FROM orders where rowid = ?",(rowid))
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

v = dataz()
v.update_userID_customers_payments()