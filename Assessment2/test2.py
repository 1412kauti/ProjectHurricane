import sqlite3
conn = sqlite3.connect("/home/hao/Documents/Assessment2/assessment2.db")
c = conn.cursor()

def Create_Table():
    c.execute("""CREATE TABLE table_name""")
    conn.commit()

def Rename_Table():
    c.execute("ALTER TABLE trip RENAME TO journey")
    conn.commit()

def Add_Column():
    c.execute("ALTER TABLE table_name ADD COLUMN column_name_add_datetype")
    conn.commit()

def Drop_Column():
    c.execute("ALTER TABLE table_name DROP COLUMN column_name")
    conn.commit()

def Drop_Table():
    c.execute("DROP TABLE table_name")
    conn.commit()

def Insert_Into_customers():
    c.execute("""INSERT INTO customers
    (first_name, last_name, email, phone_number, password, payment_method)
    VALUES ('haos', 'zhong', 'hao123', 7412566921, 'password', 'card');""")
    conn.commit()

def Insert_Into_drivers():
    c.execute("""INSERT INTO drivers
    (first_name, last_name, email, phone_number, password, car_make, car_colour, license_plat_number, driver_license, bank_account)
    VALUES ('haos', 'zhong', 'hao123', 7412566921, 'password', 'car', 'blue', 'lu-74-23', 'driver_license', 'money_go_in');""")
    conn.commit()

def Insert_Into_admins():
    c.execute("""INSERT INTO admins
    (first_name, last_name, email, phone_number, password)
    VALUES ('haos', 'zhong', 'hao123', 07412566921, 'password');""")
    conn.commit()

def Insert_Into_journey():
    c.execute("""INSERT INTO journey
    (order_ID, date_created, customer_ID, driver_name, status, driver_ID, start_piont, end_piont, price, customer_number)
    VALUES(23, 'someday', 1, 'driver', 'finished', 5, 'somewhere', 'somewhere_else', 42, 23);""")
    conn.commit()

def Delete_Row_customers():
    c.execute("DELETE FROM customers where rowid = 1")
    conn.commit()

def Delete_Row_drivers():
    c.execute("DELETE FROM drivers where rowid = 1")
    conn.commit()

def Delete_Row_admins():
    c.execute("DELETE FROM admins where rowid = 1")
    conn.commit()

def Delete_Row_journey():
    c.execute("DELETE FROM journey where rowid = 2")
    conn.commit()

def Read_From_Customers():
    c.execute("SELECT*FROM customers")
    print(c.fetchall())
    conn.commit()

def Read_From_Drivers():
    c.execute("SELECT*FROM drivers")
    print(c.fetchall())
    conn.commit()

def Read_From_Admins():
    c.execute("SELECT*FROM admins")
    print(c.fetchall())
    conn.commit()

def Read_From_Journey():
    c.execute("SELECT*FROM journey")
    print(c.fetchall())
    conn.commit()

