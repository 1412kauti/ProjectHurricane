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
        c.execute("ALTER TABLE trip RENAME TO journey")
        conn.commit()
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c = conn.cursor()

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
    def Insert_Into_drivers(z,y,x,w,v,u,t,s,r,q):
        # license_expiry = self..text()
        # bank_account = self..text()
        import sqlite3
        conn = sqlite3.connect("assessment2.db")
        c.execute('''PRAGMA journal_mode = WAL''')
        c.execute("""INSERT INTO drivers
        (first_name, last_name, email, phone_number, password, car_make, car_colour, car_license_plate_number, license_expiry, driver_license, bank_account)
        VALUES (?,?,?,?,?,?,?,?,?,?)""", (z,y,x,w,v,u,t,s,r,q))
        conn.commit()

    @staticmethod
    def Insert_Into_admins():
        c.execute("""INSERT INTO admins
        (first_name, last_name, email, phone_number, password)
        VALUES ('haos', 'zhong', 'hao123', 07412566921, 'password');""")
        conn.commit()

    @staticmethod
    def Insert_Into_journey():
        c.execute("""INSERT INTO journey
        (order_ID, date_created, customer_ID, driver_name, status, driver_ID, start_point, end_point, price, customer_number)
        VALUES(23, 'someday', 1, 'driver', 'finished', 5, 'somewhere', 'somewhere_else', 42, 23);""")
        conn.commit()

    @staticmethod
    def Delete_Duplicates_Customers():
        c.execute("DELETE FROM customers WHERE rowid NOT IN (SELECT min(rowid) FROM customers GROUP BY first_name,email")
        conn.commit() 

    @staticmethod
    def Update_First_Name_customers():
        c.execute("""UPDATE customers
        SET first_name = 'someone'
        WHERE user_ID = 1""")
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
    def Update_email_drivers():
        c.execute("""UPDATE drivers
        SET email = 'someone'
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
    # def Update_date_created_journey():
    #     c.execute("""UPDATE journey
    #     SET date_created = 'somedate'
    #     WHERE order_ID = 1""")
    #     conn.commit()


    # @staticmethod
    # def Update_date_created_journey():
    #     c.execute("""UPDATE journey
    #     SET last_name = 'someone'
    #     WHERE order_ID = 1""")
    #     conn.commit()

    
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
        conn.commit()


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
        c.execute("DELETE FROM journey where rowid = 2")
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
v.Delete_Duplicates_Customers()