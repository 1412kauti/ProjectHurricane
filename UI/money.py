from os import sendfile
import sys
from datetime import datetime
from PyQt5 import QtWidgets, QtCore, QtGui
from test2 import dataz
from StartScreen import Ui_Form as ui1
from Login_Screen import Ui_Form as ui2
from Registration_Screen import Ui_Form as ui3
from User_Card import Ui_Form as ui4
from User_Paypal import Ui_Form as ui5
from Driver_Card import Ui_Form as ui6
from Driver_Paypal import Ui_Form as ui7
from Thank_You import Ui_Form as ui8
from Verification_Screen import Ui_Form as ui9
from Congratulations import Ui_Form as ui10
from forgotChoices import Ui_Form as ui11
from changePassword import Ui_Form as ui12
from UserScreen import Ui_Form as ui13
from User_Submit_Payment import Ui_Form as ui14
from change_User_First_Name import Ui_Form as ui15
from change_User_Last_Name import Ui_Form as ui16
from change_User_Email import Ui_Form as ui17
from change_User_Password import Ui_Form as ui18
from change_User_Phone_Number import Ui_Form as ui19
from DriverScreen import Ui_Form as ui20
from AdminScreen import Ui_Form as ui21
from change_Driver_First_Name import Ui_Form as ui22
from change_Driver_Last_Name import Ui_Form as ui23
from change_Driver_Email import Ui_Form as ui24
from change_Driver_Phone_Number import Ui_Form as ui25
from change_Driver_Password import Ui_Form as ui26
from BackEnd import BackEnd
from random import randint
import numpy as np
import sqlite3
import re
#Database Python Connection
conn = sqlite3.connect("assessment2.db")
c = conn.cursor()
#Classes provide a means of bundling data and functionality together
class change_Driver_Paypal(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """              
        self.ui33 = ui7()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui33.setupUi(self)
        #Connecting the button to a function within this class
        self.ui33.Submit_Details4.clicked.connect(self.send2database)
        #initialize the qss function
        self.qss()

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_
    
    def send2database(self):
        """[summary]
        Take Data From UI and Send to Table in Database
        """
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        new_payme = self.ui33.Driver_Paypal_payme.text()
        dataz().Update_Paypal_drivers(new_payme,pass__)
        self.open_Driver_Mainscreen()
        #Closes existing Window
        self.close()

    def open_Driver_Mainscreen(self):
        """[summary]
        open DriverScreen
        """
        self.o40 = DriverScreen()
        self.o40.show()

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
#Classes provide a means of bundling data and functionality together
class change_Driver_Card(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui32 = ui6()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui32.setupUi(self)
        #Connecting the button to a function within this class
        self.ui32.Submit_Details3.clicked.connect(self.send2database)
        #initialize the qss function
        self.qss()

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def send2database(self):
        """[summary]
        Take Data From UI and Send to Table in Database
        """
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        new_account_name = self.ui32.Drive_Card_Name.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        new_account_number = self.ui32.Driver_card_account_number.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        sort_code1 = self.ui32.Driver_Card_SortCode1.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        sort_code2 = self.ui32.Driver_Card_SortCode2.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        sort_code3 = self.ui32.Driver_Card_SortCode3.text()
        sort_code = str(sort_code1) + "-" + str(sort_code2) + "-" + str(sort_code3)
        dataz().Update_Card_drivers(new_account_name,new_account_number,sort_code,pass__)
        self.open_Driver_Mainscreen()
        #Closes existing Window
        self.close()

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
    
    def open_Driver_Mainscreen(self):
        """[summary]
        open DriverScreen
        """
        self.o40 = DriverScreen()
        self.o40.show()
#Classes provide a means of bundling data and functionality together
class change_User_Paypal(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui31 = ui5()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui31.setupUi(self)
        #Connecting the button to a function within this class
        self.ui31.Submit_Details2.clicked.connect(self.send2database)
        #initialize the qss function
        self.qss()
    def send2database(self):
        """[summary]
        Take Data From UI and Send to Table in Database
        """
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        new_paypal_email = self.ui31.User_Paypal_Email.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        new_paypal_password = self.ui31.User_Paypal_Password.text()
        dataz().Update_Paypal_customers(new_paypal_email,new_paypal_password,pass__)
        self.open_User_Mainscreen()
        #Closes existing Window
        self.close()

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
    
    def open_User_Mainscreen(self):
        """[summary]
        Open User Screen
        """
        self.o40 = UserMainScreen()
        self.o40.show()
#Classes provide a means of bundling data and functionality together
class change_User_Card(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui30 = ui4()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui30.setupUi(self)
        #Connecting the button to a function within this class
        self.ui30.Submit_Details1.clicked.connect(self.send2database)
        #initialize the qss function
        self.qss()

    def send2database(self):
        """[summary]
        Take Data From UI and Send to Table in Database
        """
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        new_User_card_name = self.ui30.User_Card_Name.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        new_User_card_number = self.ui30.User_Card_Number.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        new_User_card_cvv = self.ui30.User_Card_CVV.text()
        dataz().Update_Card_customers(new_User_card_name,new_User_card_number,new_User_card_cvv,pass__)
        self.open_User_Mainscreen()
        #Closes existing Window
        self.close()

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_
    
    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
    
    def open_User_Mainscreen(self):
        """[summary]
        Open User Screen
        """
        self.o40 = UserMainScreen()
        self.o40.show()
#Classes provide a means of bundling data and functionality together
class change_Driver_Password(QtWidgets.QWidget):
    """Drivers' password change"""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui26 = ui26()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui26.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui26.changePasswordBtn.clicked.connect(self.pass_validator)

    def hit_Submit(self):
        """Submit button algorithm."""
        self.database_connectinator()
        self.o21 = DriverScreen()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()

    def pass_validator(self):
        """Password validator"""
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        new_password = self.ui26.change_Driver_Password_Label.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        conf_new_password = self.ui26.change_Driver_Confirm_Password_Label.text()
        if new_password == conf_new_password:
            self.hit_Submit()
        else:
            #Setting text on the Label
            self.ui26.Passwords_Mismatch.setText('Passwords Mismatch')
        
    def database_connectinator(self):
        """Update driver's password by id."""
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        emailn = self.ui26.change_Driver_Password_Label.text()
        dataz().Update_password_drivers(emailn,pass__)

    def takePass(self, file):
        """Take data from .txt with current user ID"""
        with open(file, 'r') as f:
            id_ = f.read()
            return id_
        
    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        """CSS"""
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
#Classes provide a means of bundling data and functionality together
class change_Driver_Phone_Number(QtWidgets.QWidget):
    """Change driver's phone number."""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui25 = ui25()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui25.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui25.changePhoneNumberBtn.clicked.connect(self.hit_Submit)

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        phnn = self.ui25.change_Driver_PhoneNumber_Label.text()
        dataz().Update_phone_number_drivers(phnn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = DriverScreen()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()


    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
#Classes provide a means of bundling data and functionality together
class change_Driver_Email(QtWidgets.QWidget):
    """Change driver's email"""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui24 = ui24()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui24.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui24.changeEmailBtn.clicked.connect(self.hit_Submit)

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = DriverScreen()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()
        
    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        emailn = self.ui24.change_Driver_Email_Label.text()
        dataz().Update_Email_drivers(emailn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())       
#Classes provide a means of bundling data and functionality together
class change_Driver_Last_Name(QtWidgets.QWidget):
    """Change driver's last name."""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui23 = ui23()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui23.setupUi(self)
        #Connecting the button to a function within this class
        self.ui23.ChangeLastNameBtn.clicked.connect(self.hit_Submit)
        #initialize the qss function
        self.qss()

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        lastn = self.ui23.change_Driver_LastName_Label.text()
        dataz().Update_last_name_drivers(lastn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = DriverScreen()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
#Classes provide a means of bundling data and functionality together
class change_Driver_First_Name(QtWidgets.QWidget):
    """Change driver's first name."""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui22 = ui22()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui22.setupUi(self)
        #Connecting the button to a function within this class
        self.ui22.ChangeFirstNameBtn.clicked.connect(self.hit_Submit)
        #initialize the qss function
        self.qss()

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = DriverScreen()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        firstn = self.ui22.change_Driver_FirstName_Label.text()
        dataz().Update_first_name_drivers(firstn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
#Classes provide a means of bundling data and functionality together
class AdminScreen(QtWidgets.QWidget):
    """Admin screen window."""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui21 = ui21()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui21.setupUi(self)
        #initialize the qss function
        self.qss()
        self.loadjourneys()
        self.loadcustomers()
        self.loaddrivers()
        #Connecting the button to a function within this class
        self.ui21.Refresh_Btn.clicked.connect(self.hit_refresh)
        #Connecting the button to a function within this class
        self.ui21.Logout_Btn.clicked.connect(self.hit_Logout)
        #Connecting the button to a function within this class
        self.ui21.UpdateValueBtn.clicked.connect(self.Update_Values)
        #Connecting the button to a function within this class
        self.ui21.DeleteValueBtn.clicked.connect(self.Delete_Row)
        #Connecting the button to a function within this class
        self.ui21.InsertValueBtn.clicked.connect(self.Insert_value)

    def Insert_value(self):
        """Create row button algorithm"""
        #currentText() extracts the text from the selected item in the comboBox when executed
        t = str(self.ui21.comboBox.currentText())
        print(t)
        dataz().create_row_by_admin(t)

    def Update_Values(self):
        """Update value button."""
        #currentText() extracts the text from the selected item in the comboBox when executed
        table = self.ui21.comboBox.currentText()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        column = self.ui21.select_Column_Label.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        row = self.ui21.select_Row_Label.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        value = self.ui21.value_Change.text()
        dataz().Update_something_by_admin(table, column, row, value)


    def hit_Logout(self):
        self.oz = LoginScreen()
        #Show New Window
        self.oz.show()
        #Closes existing Window
        self.close()
    def hit_refresh(self):
        self.ui21 = AdminScreen()
        #Show New Window
        self.ui21.show()
        #Closes existing Window
        self.close()
    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def loadjourneys(self):
        """Journeys table inside GUI."""
        connection = sqlite3.connect('assessment2.db')
        cur = connection.cursor()
        sqlstr = """SELECT * FROM journey"""
        tablerow = 0
        results = cur.execute(sqlstr)
        self.ui21.Journeys_Table.setRowCount(40)
        for row in results:
            self.ui21.Journeys_Table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui21.Journeys_Table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui21.Journeys_Table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui21.Journeys_Table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
            self.ui21.Journeys_Table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[6]))
            self.ui21.Journeys_Table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[8]))
            self.ui21.Journeys_Table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[9]))
            self.ui21.Journeys_Table.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[10]))
            self.ui21.Journeys_Table.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[11]))
            self.ui21.Journeys_Table.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[12]))
            self.ui21.Journeys_Table.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(row[13]))
            self.ui21.Journeys_Table.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(row[14]))
            self.ui21.Journeys_Table.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(row[15]))
            tablerow += 1

    def loadcustomers(self):
        """Customers table inside GUI."""
        connection = sqlite3.connect('assessment2.db')
        cur = connection.cursor()
        sqlstr = """SELECT * FROM customers"""
        tablerow = 0
        results = cur.execute(sqlstr)
        self.ui21.Customers_Table.setRowCount(40)
        for row in results:
            self.ui21.Customers_Table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui21.Customers_Table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui21.Customers_Table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui21.Customers_Table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
            self.ui21.Customers_Table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[6]))
            tablerow += 1

    def loaddrivers(self):
        """Drivers table inside GUI."""
        connection = sqlite3.connect('assessment2.db')
        cur = connection.cursor()
        sqlstr = """SELECT * FROM drivers"""
        tablerow = 0
        results = cur.execute(sqlstr)
        self.ui21.Drivers_Table.setRowCount(40)
        for row in results:
            self.ui21.Drivers_Table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui21.Drivers_Table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui21.Drivers_Table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui21.Drivers_Table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
            self.ui21.Drivers_Table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[6]))
            self.ui21.Drivers_Table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[8]))
            self.ui21.Drivers_Table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[9]))
            self.ui21.Drivers_Table.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[10]))
            self.ui21.Drivers_Table.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[11]))
            tablerow += 1
    
    def Delete_Row(self):
        """Delte row button."""
        #currentText() extracts the text from the selected item in the comboBox when executed
        table = self.ui21.comboBox.currentText()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        row = self.ui21.select_Row_Label.text()
        dataz().Delete_Row_by_admin(table, row)
#Classes provide a means of bundling data and functionality together
class change_User_Phone_Number(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui19 = ui19()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui19.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui19.changePhoneNumberBtn.clicked.connect(self.hit_Submit)

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        phnn = self.ui19.change_User_PhoneNumber_Label.text()
        dataz().Update_phone_number_customers(phnn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()


    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
#Classes provide a means of bundling data and functionality together
class change_User_Password(QtWidgets.QWidget):
    """Change user's password."""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui18 = ui18()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui18.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui18.changePasswordBtn.clicked.connect(self.pass_validator)

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()

    def pass_validator(self):
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        new_password = self.ui18.change_User_Password_Label.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        conf_new_password = self.ui18.change_User_Confirm_Password_Label.text()
        if new_password == conf_new_password:
            self.hit_Submit()
        else:
            #Setting text on the Label
            self.ui18.Passwords_Mismatch.setText('Passwords Mismatch')
        
    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        emailn = self.ui18.change_User_Password_Label.text()
        dataz().Update_password_customers(emailn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_
        
    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
#Classes provide a means of bundling data and functionality together
class change_User_Email(QtWidgets.QWidget):
    """Change user's email."""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui17 = ui17()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui17.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui17.changeEmailBtn.clicked.connect(self.hit_Submit)

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()
        
    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        emailn = self.ui17.change_User_Email_Label.text()
        dataz().Update_Email_customers(emailn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
#Classes provide a means of bundling data and functionality together
class change_User_LastName(QtWidgets.QWidget):
    """Change user's last name."""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui16 = ui16()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui16.setupUi(self)
        #Connecting the button to a function within this class
        self.ui16.ChangeLastNameBtn.clicked.connect(self.hit_Submit)
        #initialize the qss function
        self.qss()

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        lastn = self.ui16.change_User_LastName_Label.text()
        dataz().Update_Last_Name_customers(lastn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
#Classes provide a means of bundling data and functionality together
class change_User_FirstName(QtWidgets.QWidget):
    """Change user's first name."""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui15 = ui15()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui15.setupUi(self)
        #Connecting the button to a function within this class
        self.ui15.ChangeFirstNameBtn.clicked.connect(self.hit_Submit)
        #initialize the qss function
        self.qss()

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        firstn = self.ui15.change_User_FirstName_Label.text()
        dataz().Update_First_Name_customers(firstn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
#Classes provide a means of bundling data and functionality together
class Congratulations(QtWidgets.QWidget):
    """Post registration window."""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui10 = ui10()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui10.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui10.go2Login.clicked.connect(self.back2Login)

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def back2Login(self):
        self.o9 = LoginScreen()
        #Show New Window
        self.o9.show()
        #Closes existing Window
        self.close()
#Classes provide a means of bundling data and functionality together
class Verification_Screen(QtWidgets.QWidget):
    """Verification screen"""
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui9 = ui9()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui9.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui9.Complete_Verification.clicked.connect(self.Verify_validator)

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def go_to_Account_Activated(self):
        self.o8 = Congratulations()
        #Show New Window
        self.o8.show()
        #Closes existing Window
        self.close()

    def Verify_validator(self):
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        if str(self.ui9.Security_code_text.text()) == str(VeriCode):
            self.go_to_Account_Activated()
        else:
            #Setting text on the Label
            self.ui9.Mismatch_Label.setText('Try Again')
#Classes provide a means of bundling data and functionality together   
class Thank_You(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        global VeriCode
        VeriCode = randint(0, 1000)
        self.ui8 = ui8()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui8.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui8.Verify_Now.clicked.connect(self.open_Verification_Screen)
        #Setting text on the Label
        self.ui8.Security_Code.setText("%d" % VeriCode)

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def open_Verification_Screen(self):
        self.o7 = Verification_Screen()
        #Show New Window
        self.o7.show()
        #Closes existing Window
        self.close()
#Classes provide a means of bundling data and functionality together
class Driver_Paypal(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui7 = ui7()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui7.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui7.Submit_Details4.clicked.connect(self.open_Thankyou)

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def open_Thankyou(self):
        self.o6 = Thank_You()
        #Show New Window
        self.o6.show()
        #Closes existing Window
        self.close()
        self.take_Driver_Paypal_Inputs()

    def take_Driver_Paypal_Inputs(self):
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_paypal_payme = self.ui7.Driver_Paypal_payme.text()
        driver_card_name = 0
        driver_card_account_number = 0
        driver_sort_code = 0
        self.d5 = dataz()
        self.d5.payment_method_driver(driver_card_name, driver_card_account_number, driver_sort_code,
                                            driver_paypal_payme,driver_first_name)
#Classes provide a means of bundling data and functionality together
class Driver_Card(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui6 = ui6()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui6.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui6.Submit_Details3.clicked.connect(self.open_Thankyou)

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def open_Thankyou(self):
        self.o6 = Thank_You()
        #Show New Window
        self.o6.show()
        #Closes existing Window
        self.close()
        self.take_Driver_Card_Inputs()

    def take_Driver_Card_Inputs(self):
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_card_name = self.ui6.Drive_Card_Name.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_card_account_number = self.ui6.Driver_card_account_number.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_sort_code1 = self.ui6.Driver_Card_SortCode1.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_sort_code2 = self.ui6.Driver_Card_SortCode2.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_sort_code3 = self.ui6.Driver_Card_SortCode3.text()
        driver_sort_code = str(driver_sort_code1) + "-" + str(driver_sort_code2) + "-" + str(driver_sort_code3)
        driver_paypal_payme = 0
        self.d4 = dataz()
        self.d4.payment_method_driver(driver_card_name, driver_card_account_number, driver_sort_code,
                                            driver_paypal_payme,driver_first_name)
#Classes provide a means of bundling data and functionality together
class User_Paypal(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui5 = ui5()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui5.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui5.Submit_Details2.clicked.connect(self.open_Thankyou)

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def open_Thankyou(self):
        self.o6 = Thank_You()
        #Show New Window
        self.o6.show()
        #Closes existing Window
        self.close()
        self.take_User_Paypal_Inputs()

    def take_User_Paypal_Inputs(self):
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_paypal_email = self.ui5.User_Paypal_Email.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_paypal_password = self.ui5.User_Paypal_Password.text()
        user_card_name = 0
        user_card_number = 0
        user_card_cvv = 0
        self.d3 = dataz()
        self.d3.payment_method_customers(user_card_name, user_card_number, user_card_cvv, user_paypal_email,
                                              user_paypal_password,user_first_name)
#Classes provide a means of bundling data and functionality together
class User_Card(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui4 = ui4()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui4.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui4.Submit_Details1.clicked.connect(self.open_Thankyou)

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def open_Thankyou(self):
        self.o6 = Thank_You()
        #Show New Window
        self.o6.show()
        #Closes existing Window
        self.close()
        self.take_User_Card_Inputs()

    def take_User_Card_Inputs(self):
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_card_name = self.ui4.User_Card_Name.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_card_number = self.ui4.User_Card_Number.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_card_cvv = self.ui4.User_Card_CVV.text()
        user_paypal_email = 0
        user_paypal_password = 0
        self.d2 = dataz()
        self.d2.payment_method_customers(user_card_name, user_card_number, user_card_cvv, user_paypal_email,
                                              user_paypal_password,user_first_name)
#Classes provide a means of bundling data and functionality together
class RegisterScreen(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui3 = ui3()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui3.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui3.User_Submit_Button.clicked.connect(self.User_Payment)
        #Connecting the button to a function within this class
        self.ui3.Driver_Submit_Button.clicked.connect(self.Driver_Payment)
        self.user_check_states1()
        self.user_check_states2()
        self.driver_check_states1()
        self.driver_check_states2()

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def driver_check_car_color_state(self):
        input_car_color_name = self.ui3.Driver_Car_Color
        regexp = QtCore.QRegExp(r"^[A-Za-z -]+$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_car_color_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_car_color_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def driver_check_car_make_state(self):
        input_car_make_name = self.ui3.Driver_Car_Make_Text
        regexp = QtCore.QRegExp(r"^[A-Za-z0-9 .-]+$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_car_make_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_car_make_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def driver_check_car_license_state(self):
        input_car_license_name = self.ui3.Driver_Car_Number
        regexp = QtCore.QRegExp(
            r"(^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$)|(^[A-Z][0-9]{1,3}[A-Z]{3}$)|(^[A-Z]{3}[0-9]{1,3}[A-Z]$)|(^[0-9]{1,4}[A-Z]{1,2}$)|(^[0-9]{1,3}[A-Z]{1,3}$)|(^[A-Z]{1,2}[0-9]{1,4}$)|(^[A-Z]{1,3}[0-9]{1,3}$)|(^[A-Z]{1,3}[0-9]{1,4}$)|(^[0-9]{3}[DX]{1}[0-9]{3}$)")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_car_license_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_car_license_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def driver_check_drivers_license_state(self):
        input_drivers_license_name = self.ui3.Driver_License_Number
        regexp = QtCore.QRegExp(r"^[A-Z9]{5}\d{6}[A-Z9]{2}\d[A-Z]{2}$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_drivers_license_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_drivers_license_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def driver_check_confirm_password_state(self):
        input_confirm_password_name = self.ui3.Driver_Confirm_Password_Text
        regexp = QtCore.QRegExp(r"^[A-Za-z0-9 .-_]{7,20}+$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_confirm_password_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_confirm_password_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def user_check_confirm_password_state(self):
        input_confirm_password_name = self.ui3.User_Confirm_Password_Text
        regexp = QtCore.QRegExp(r"^[A-Za-z0-9 .-_]{7,20}+$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_confirm_password_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_confirm_password_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def driver_check_password_state(self):
        input_password_name = self.ui3.Driver_Password_Text
        regexp = QtCore.QRegExp(r"^[A-Za-z0-9 .-_]{7,20}+$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_password_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_password_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def user_check_password_state(self):
        input_password_name = self.ui3.User_Password_Text
        regexp = QtCore.QRegExp(r"^[A-Za-z0-9 .-_]{7,20}+$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_password_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_password_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def driver_check_last_name_state(self):
        input_last_name = self.ui3.Driver_Last_Name_Text
        regexp = QtCore.QRegExp(r"^[A-Za-z .-]+$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_last_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_last_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def user_check_last_name_state(self):
        input_last_name = self.ui3.User_Last_Name_Text
        regexp = QtCore.QRegExp(r"^[A-Za-z .-]+$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_last_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_last_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def driver_check_first_name_state(self):
        input_first_name = self.ui3.Driver_First_Name_Text
        regexp = QtCore.QRegExp(r"^[A-Za-z .-]+$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_first_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_first_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def user_check_first_name_state(self):
        input_first_name = self.ui3.User_First_Name_Text
        regexp = QtCore.QRegExp(r"^[A-Za-z .-]+$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_first_name.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_first_name.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def driver_check_email_state(self):
        input_email = self.ui3.Driver_Email_Text
        regexp = QtCore.QRegExp(r"^([a-z\d.-]+)@([a-z\.d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_email.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_email.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def user_check_email_state(self):
        input_email = self.ui3.User_Email_Text
        regexp = QtCore.QRegExp(r"^([a-z\d.-]+)@([a-z\.d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_email.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_email.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def driver_check_contact_state(self):
        input_contact_number = self.ui3.Driver_Phone_Number_Text
        regexp = QtCore.QRegExp(r"^[0-9\-\+]{9,15}$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_contact_number.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_contact_number.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def user_check_contact_state(self):
        input_contact_number = self.ui3.User_Contact_Number_Text
        regexp = QtCore.QRegExp(r"^[0-9\-\+]{9,15}$")
        #Validating the regular expression
        validator = QtGui.QRegExpValidator(regexp)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        state = validator.validate(input_contact_number.text(), 0)[0]
        #If the Validator Validates the result against the Regular Expression and is Acceptable, then it turns the lineEdit Green 
        if state == QtGui.QValidator.Acceptable:
            color = '#456B19'
        elif state == QtGui.QValidator.Intermediate:
            color = ''
        else:
            color = ''
        input_contact_number.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def driver_check_states1(self):
        self.driver_check_first_name_state()
        self.driver_check_email_state()
        self.driver_check_contact_state()
        self.driver_check_last_name_state()
        self.driver_check_password_state()
        self.driver_check_confirm_password_state()
        self.driver_check_drivers_license_state()
        self.driver_check_car_license_state()
        self.driver_check_car_make_state()
        self.driver_check_car_color_state()

    def user_check_states1(self):
        self.user_check_first_name_state()
        self.user_check_email_state()
        self.user_check_contact_state()
        self.user_check_last_name_state()
        self.user_check_password_state()
        self.user_check_confirm_password_state()

    def driver_check_states2(self):
        self.ui3.Driver_Car_Color.textEdited.connect(self.driver_check_car_color_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.Driver_Car_Color.textEdited.emit(self.ui3.Driver_Car_Color.text())
        self.ui3.Driver_Car_Make_Text.textEdited.connect(self.driver_check_car_make_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.Driver_Car_Make_Text.textEdited.emit(self.ui3.Driver_Car_Make_Text.text())
        self.ui3.Driver_Car_Number.textEdited.connect(self.driver_check_car_license_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.Driver_Car_Number.textEdited.emit(self.ui3.Driver_Car_Number.text())
        self.ui3.Driver_License_Number.textEdited.connect(self.driver_check_drivers_license_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.Driver_License_Number.textEdited.emit(self.ui3.Driver_License_Number.text())
        self.ui3.Driver_Last_Name_Text.textEdited.connect(self.driver_check_last_name_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.Driver_Last_Name_Text.textEdited.emit(self.ui3.Driver_Last_Name_Text.text())
        self.ui3.Driver_First_Name_Text.textEdited.connect(self.driver_check_first_name_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.Driver_First_Name_Text.textEdited.emit(self.ui3.Driver_First_Name_Text.text())
        self.ui3.Driver_Email_Text.textEdited.connect(self.driver_check_email_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.Driver_Email_Text.textEdited.emit(self.ui3.Driver_Email_Text.text())
        self.ui3.Driver_Phone_Number_Text.textEdited.connect(self.driver_check_contact_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.Driver_Phone_Number_Text.textEdited.emit(self.ui3.Driver_Phone_Number_Text.text())
        self.ui3.Driver_Password_Text.textEdited.connect(self.driver_check_password_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.Driver_Password_Text.textEdited.emit(self.ui3.Driver_Password_Text.text())
        self.ui3.Driver_Confirm_Password_Text.textEdited.connect(self.driver_check_confirm_password_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.Driver_Confirm_Password_Text.textEdited.emit(self.ui3.Driver_Confirm_Password_Text.text())

    def user_check_states2(self):
        self.ui3.User_Last_Name_Text.textEdited.connect(self.user_check_last_name_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.User_Last_Name_Text.textEdited.emit(self.ui3.User_Last_Name_Text.text())
        self.ui3.User_First_Name_Text.textEdited.connect(self.user_check_first_name_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.User_First_Name_Text.textEdited.emit(self.ui3.User_First_Name_Text.text())
        self.ui3.User_Email_Text.textEdited.connect(self.user_check_email_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.User_Email_Text.textEdited.emit(self.ui3.User_Email_Text.text())
        self.ui3.User_Contact_Number_Text.textEdited.connect(self.user_check_contact_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.User_Contact_Number_Text.textEdited.emit(self.ui3.User_Contact_Number_Text.text())
        self.ui3.User_Password_Text.textEdited.connect(self.user_check_password_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.User_Password_Text.textEdited.emit(self.ui3.User_Password_Text.text())
        self.ui3.User_Confirm_Password_Text.textEdited.connect(self.user_check_confirm_password_state)
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        self.ui3.User_Confirm_Password_Text.textEdited.emit(self.ui3.User_Confirm_Password_Text.text())

    def take_user_inputs(self):
        global user_first_name
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_first_name = self.ui3.User_First_Name_Text.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_last_name = self.ui3.User_Last_Name_Text.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_email = self.ui3.User_Email_Text.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_contact_number = self.ui3.User_Contact_Number_Text.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_password = self.ui3.User_Password_Text.text()
        #currentText() extracts the text from the selected item in the comboBox when executed 
        user_payment = self.ui3.comboBox.currentText()
        self.d1 = dataz()
        self.d1.Insert_Into_customers(user_first_name, user_last_name, user_email, user_contact_number, user_password, user_payment)

    def take_driver_inputs(self):
        global driver_first_name
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_first_name = self.ui3.Driver_First_Name_Text.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_last_name = self.ui3.Driver_Last_Name_Text.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_email = self.ui3.Driver_Email_Text.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_password = self.ui3.Driver_Password_Text.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_contact_number = self.ui3.Driver_Phone_Number_Text.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_license = self.ui3.Driver_License_Number.text()
        driver_license_expiry = self.ui3.dateEdit.date().toPyDate()
        #currentText() extracts the text from the selected item in the comboBox when executed
        driver_car_class = self.ui3.comboBox_3.currentText()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_car_license = self.ui3.Driver_Car_Number.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_car_make = self.ui3.Driver_Car_Make_Text.text()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_car_color = self.ui3.Driver_Car_Color.text()
        self.d2 = dataz()
        self.d2.Insert_Into_drivers(driver_first_name, driver_last_name, driver_email, driver_password, driver_contact_number, driver_license, driver_license_expiry,driver_car_class, driver_car_license, driver_car_make, driver_car_color)

    def open_User_Card(self):
        self.o2 = User_Card()
        #Show New Window
        self.o2.show()
        #Closes existing Window
        self.close()

    def open_User_Paypal(self):
        self.o3 = User_Paypal()
        #Show New Window
        self.o3.show()
        #Closes existing Window
        self.close()

    def open_Driver_Card(self):
        self.o4 = Driver_Card()
        #Show New Window
        self.o4.show()
        #Closes existing Window
        self.close()

    def open_Driver_Paypal(self):
        self.o5 = Driver_Paypal()
        #Show New Window
        self.o5.show()
        #Closes existing Window
        self.close()

    def Delete_Dup_Customers(self):
        self.d9 = dataz()
        self.d9.Delete_Duplicates_Customers()

    def Delete_Dup_Drivers(self):
        self.d10 = dataz()
        self.d10.Delete_Duplicates_Drivers()

    def User_Payment(self):
        self.user_check_email_state()
        self.take_user_inputs()
        self.Delete_Dup_Customers()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        if self.ui3.User_Password_Text.text() == self.ui3.User_Confirm_Password_Text.text():
            #currentText() extracts the text from the selected item in the comboBox when executed
            if self.ui3.comboBox.currentText() == "Card":
                #Connecting the button to a function within this class
                self.ui3.User_Submit_Button.clicked.connect(self.open_User_Card)
            #currentText() extracts the text from the selected item in the comboBox when executed
            elif self.ui3.comboBox.currentText() == "PayPal":
                #Connecting the button to a function within this class
                self.ui3.User_Submit_Button.clicked.connect(self.open_User_Paypal)
        else:
            #Setting text on the Label
            self.ui3.User_Invalid_Password.setText("Passwords Mismatch, try again")

    def Driver_Payment(self):
        self.take_driver_inputs()
        self.Delete_Dup_Drivers()
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        if self.ui3.Driver_Password_Text.text() == self.ui3.Driver_Confirm_Password_Text.text():
            #currentText() extracts the text from the selected item in the comboBox when executed
            if self.ui3.comboBox_2.currentText() == "Card":
                #Connecting the button to a function within this class
                self.ui3.Driver_Submit_Button.clicked.connect(self.open_Driver_Card)
            #currentText() extracts the text from the selected item in the comboBox when executed
            elif self.ui3.comboBox_2.currentText() == "Paypal":
                #Connecting the button to a function within this class
                self.ui3.Driver_Submit_Button.clicked.connect(self.open_Driver_Paypal)
        else:
            #Setting text on the Label
            self.ui3.Driver_Invalid_Password.setText("Passwords Mismatch, try again")
#Classes provide a means of bundling data and functionality together
class LoginScreen(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui2 = ui2()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui2.setupUi(self)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui2.user_Submit.clicked.connect(self.userChecker)
        #Connecting the button to a function within this class
        self.ui2.driver_Submit.clicked.connect(self.driverChecker)
        #Connecting the button to a function within this class
        self.ui2.admin_Submit.clicked.connect(self.adminChecker)

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def openUserLogin(self):
        self.o12 = UserMainScreen()
        #Show New Window
        self.o12.show()
        #Closes existing Window
        self.close()

    def openDriverLogin(self):
        self.o21 = DriverScreen()
        #Show New Window
        self.o21.show()
        id_ = DriverScreen().takePass('pass.txt')
        #Closes existing Window
        self.close()

    def adminChecker(self):
        """Admin login verification with accounts provided. """
        admin1 = {
            'nick': 'hulksmash',
            'empID': '777',
            'psw': 'qwerty'
        }
        admin2 = {
            'nick': 'kauti',
            'empID': '666',
            'psw': 'qwerty'
        }
        admin3 = {
            'nick': 'evalien',
            'empID': '007',
            'psw': 'qwerty'
        }
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        if self.ui2.adminLoginEC.text() == admin1['nick']  and \
                self.ui2.adminPass.text() == admin1['psw'] and \
                self.ui2.empID.text() == admin1['empID']:
            self.openAdminLogin()
        elif self.ui2.adminLoginEC.text() == admin2['nick']  and \
                self.ui2.adminPass.text() == admin2['psw'] and \
                self.ui2.empID.text() == admin2['empID']:
            self.openAdminLogin()
        elif self.ui2.adminLoginEC.text() == admin3['nick'] and \
                self.ui2.adminPass.text() == admin3['psw'] and \
                self.ui2.empID.text() == admin3['empID']:
            self.openAdminLogin()
        else:
            #Setting text on the Label
            self.ui2.user_login_Fail.setText("Try Again")

    def openAdminLogin(self):
        self.o22 = AdminScreen()
        #Show New Window
        self.o22.show()
        #Closes existing Window
        self.close()

    def pushToTxt(self, file, id):
        """Get current user's ID and write it to .txt"""
        with open(file, 'w') as f:
            id = str(id)
            f.write(id)

    def userChecker(self):
        """Login verification for the customers."""
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_login = str(self.ui2.userLoginEC.text())
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        user_Password = str(self.ui2.userPass.text())
        self.o13 = dataz()
        try:
            c = self.o13.get_customer_userID_by_password(user_Password)
        except TypeError:
            #Setting text on the Label
            self.ui2.user_login_Fail.setText("Try Again")
        list_of_emails = BackEnd().customerEmailList()
        list_of_phone_numbers = BackEnd().customerPhoneNumberList()

        if user_login in list_of_emails:
            a = self.o13.get_customer_userID_by_email(user_login)
            c = self.o13.get_customer_userID_by_password(user_Password)
            if a == c:
                self.pushToTxt('pass.txt', c)
                self.openUserLogin()
        elif user_login in list_of_phone_numbers:
            b = self.o13.get_customer_userID_by_phone_number(user_login)
            c = self.o13.get_customer_userID_by_password(user_Password)
            if b == c:
                self.pushToTxt('pass.txt', c)
                self.openUserLogin()
        else:
            #Setting text on the Label
            self.ui2.user_login_Fail.setText("Try Again")

    def driverChecker(self):
        """Login verification for the drivers."""
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_login = str(self.ui2.driverLoginEC.text())
        #.text() makes it possible to make the text from a QlineEdit into a variable 
        driver_password = str(self.ui2.driverPass.text())
        self.o13 = dataz()
        try:
            c = self.o13.get_driver_driverID_by_password(driver_password)
        except TypeError:
            #Setting text on the Label
            self.ui2.user_login_Fail.setText("Try Again")
        list_of_emails = BackEnd().driverEmailList()
        list_of_phone_numbers = BackEnd().driverPhoneNumberList()

        if driver_login in list_of_emails:
            a = self.o13.get_driver_driverID_by_email(driver_login)
            c = self.o13.get_driver_driverID_by_password(driver_password)
            if a == c:
                self.pushToTxt('pass.txt', c)
                self.openDriverLogin()
        if driver_login in list_of_phone_numbers:
            b = self.o13.get_driver_driverID_by_phone_number(driver_login)
            c = self.o13.get_driver_driverID_by_password(driver_password)
            if b == c:
                self.pushToTxt('pass.txt', c)
                self.openDriverLogin()
        else:
            #Setting text on the Label
            self.ui2.driver_login_Fail.setText('Try Again')
#Classes provide a means of bundling data and functionality together
class UserMainScreen(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui13 = ui13()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui13.setupUi(self)
        self.loaddata()
        #Connecting the button to a function within this class
        self.ui13.Select_Payment_Method_Btn.clicked.connect(self.Book_now)
        #Connecting the button to a function within this class
        self.ui13.Logout_Btn.clicked.connect(self.open_Start_Screen)
        #Connecting the button to a function within this class
        self.ui13.change_First_Name.clicked.connect(self.open_Change_First_Name)
        #Connecting the button to a function within this class
        self.ui13.change_Last_Name.clicked.connect(self.open_Change_Last_Name)
        #Connecting the button to a function within this class
        self.ui13.change_Email.clicked.connect(self.open_Change_Email)
        #Connecting the button to a function within this class
        self.ui13.change_Phone_Number.clicked.connect(self.open_Change_Phone_Number)
        #Connecting the button to a function within this class
        self.ui13.change_Password.clicked.connect(self.open_Change_Password)
        #Connecting the button to a function within this class
        self.ui13.change_Card.clicked.connect(self.open_Card_Change)
        #Connecting the button to a function within this class
        self.ui13.change_Paypal.clicked.connect(self.open_Paypal_Change)
        #Connecting the button to a function within this class
        self.ui13.Refresh2.clicked.connect(self.hit_refresh)
        #Connecting the button to a function within this class
        self.ui13.Refresh_Btn.clicked.connect(self.hit_refresh)
        #Connecting the button to a function within this class
        self.ui13.pushButton.clicked.connect(self.declineButton)
        #Connecting the button to a function within this class
        self.ui13.pushButton.clicked.connect(self.deleteDeclined)
        #initialize the qss function
        self.qss()
        pass__ = self.takePass('pass.txt')
        a, b, c, d = self.getCustomer(pass__)
        self.phillOut(a, b, c, d)

    def deleteDeclined(self):
        """
            Function calculates amount of orders in orders table and deletes the last one.
        :return:
        """
        last_order_id = BackEnd().getLastRowJourneys()
        dataz().Delete_Row_journey(last_order_id)

    def declineButton(self):
        """Empty all the fields in the upcoming journey tab."""
        #Setting text on the Label
        self.ui13.Upcoming_Date_Lbl.setText('')
        #Setting text on the Label
        self.ui13.Upcoming_Time_Lbl.setText('')
        #Setting text on the Label
        self.ui13.Upcomin_Journey_ID_Lbl.setText('')
        #Setting text on the Label
        self.ui13.Upcoming_Start_Location_Lbl.setText('')
        #Setting text on the Label
        self.ui13.Upcoming_Destination_Lbl.setText('')
        #Setting text on the Label
        self.ui13.Upcoming_Driver_Name_Lbl.setText('')
        #Setting text on the Label
        self.ui13.Car_Class_Label.setText('')
        #Setting text on the Label
        self.ui13.Upcoming_Car_Make_Lbl.setText('')
        #Setting text on the Label
        self.ui13.Upcoming_Car_Color_Lbl.setText('')
        #Setting text on the Label
        self.ui13.Upcoming_ETA.setText('')
        #Setting text on the Label
        self.ui13.Price_Label.setText('')
        #Setting text on the Label
        self.ui13.Distance_Label.setText('')
        #Setting text on the Label
        self.ui13.Car_Number_Lbl.setText('')

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def getCustomer(self, id):
        """Get user details by id provided in pass.txt"""
        a = dataz().get_customer_username_by_id(id)
        b = dataz().get_customer_lastname_by_id(id)
        c = dataz().get_customer_email_by_id(id)
        d = dataz().get_customer_phone_number_by_id(id)
        return a, b, c, d

    def phillOut(self, fn, ln, email, pn):
        """Fill out user's details."""
        #Setting text on the Label
        self.ui13.First_Name_Label.setText(fn)
        #Setting text on the Label
        self.ui13.Last_Name_Label.setText(ln)
        #Setting text on the Label
        self.ui13.Email_Label.setText(email)
        #Setting text on the Label
        self.ui13.Phone_Number_Label.setText(pn)

    def getNewBookingItems(self):
        """Set upcoming journey tab."""
        #currentText() extracts the text from the selected item in the comboBox when executed
        start_point = self.ui13.comboBox.currentText()
        #currentText() extracts the text from the selected item in the comboBox when executed
        end_point = self.ui13.comboBox_2.currentText()
        #currentText() extracts the text from the selected item in the comboBox when executed
        car_type = self.ui13.comboBox_3.currentText()
        distance, price = BackEnd.priceCalc(BackEnd.locations[start_point], BackEnd.locations[end_point])
        distance = format(distance, '.2f') + 'km'
        price = format(price, '.2f') + '£'
        date, time = BackEnd().getDateAndTime()
        jID = BackEnd().getJourneyID()
        driver_first_name, driver_last_name, car_number, car_make, car_color = BackEnd().assignTheDriver()
        driver_name = driver_first_name + ' ' + driver_last_name
        eta = BackEnd().getETA()
        #Setting text on the Label
        self.ui13.Upcoming_Date_Lbl.setText(date)
        #Setting text on the Label
        self.ui13.Upcoming_Time_Lbl.setText(time)
        #Setting text on the Label
        self.ui13.Upcomin_Journey_ID_Lbl.setText(jID)
        #Setting text on the Label
        self.ui13.Upcoming_Start_Location_Lbl.setText(start_point)
        #Setting text on the Label
        self.ui13.Upcoming_Destination_Lbl.setText(end_point)
        #Setting text on the Label
        self.ui13.Upcoming_Driver_Name_Lbl.setText(driver_name)
        #Setting text on the Label
        self.ui13.Car_Class_Label.setText(car_type)
        #Setting text on the Label
        self.ui13.Car_Number_Lbl.setText(car_number)
        #Setting text on the Label
        self.ui13.Upcoming_Car_Make_Lbl.setText(car_make)
        #Setting text on the Label
        self.ui13.Upcoming_Car_Color_Lbl.setText(car_color)
        #Setting text on the Label
        self.ui13.Upcoming_ETA.setText(eta)
        #Setting text on the Label
        self.ui13.Price_Label.setText(price)
        #Setting text on the Label
        self.ui13.Distance_Label.setText(distance)
        userID = self.takePass('pass.txt')
        customer_name, b, c, d = self.getCustomer(userID)
        driverID = dataz().get_driver_driverID_by_first_name(driver_first_name)
        dataz().Insert_Into_journey(date,time,jID,userID, customer_name, start_point,end_point, driverID, driver_name, car_number, car_type,car_make,car_color,price,distance)

    #This function displays data from the database to the GUI using the QTableWidget
    def loaddata(self):
        """Previous trips tab"""
        connection = sqlite3.connect('assessment2.db')
        cur = connection.cursor()
        sqlstr = """SELECT * FROM journey WHERE user_ID = 6 AND status = 'complete'"""
        tablerow = 0
        results = cur.execute(sqlstr)
        self.ui13.tableWidget.setRowCount(40)
        for row in results:
            self.ui13.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui13.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui13.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui13.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
            self.ui13.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[6]))
            self.ui13.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[8]))
            self.ui13.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[9]))
            self.ui13.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[10]))
            self.ui13.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[11]))
            self.ui13.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[12]))
            self.ui13.tableWidget.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(row[13]))
            self.ui13.tableWidget.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(row[14]))
            tablerow += 1

    def Book_now(self):
        self.getNewBookingItems()

    def open_Start_Screen(self):
        self.o14 = StartScreen()
        #Show New Window
        self.o14.show()
        #Closes existing Window
        self.close()

    def open_Change_First_Name(self):
        self.o15 = change_User_FirstName()
        #Show New Window
        self.o15.show()
        #Closes existing Window
        self.close()
        
    def open_Change_Last_Name(self):
        self.o16 = change_User_LastName()
        self.o16.show()
        #Closes existing Window
        self.close()

    def open_Change_Email(self):
        self.o17 = change_User_Email()
        #Show New Window
        self.o17.show()
        #Closes existing Window
        self.close()

    def open_Change_Password(self):
        self.o18 = change_User_Password()
        #Show New Window
        self.o18.show()
        #Closes existing Window
        self.close()

    def open_Change_Phone_Number(self):
        self.o19 = change_User_Phone_Number()
        #Show New Window
        self.o19.show()
        #Closes existing Window
        self.close()

    def open_Card_Change(self):
        self.o20 = change_User_Card()
        #Show New Window
        self.o20.show()
        #Closes existing Window
        self.close()

    def open_Paypal_Change(self):
        self.o21 = change_User_Paypal()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def hit_refresh(self):
        self.ox = UserMainScreen()
        #Show New Window
        self.ox.show()
        #Closes existing Window
        self.close()
#Classes provide a means of bundling data and functionality together
class DriverScreen(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui20 = ui20()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui20.setupUi(self)
        #Connecting the button to a function within this class
        self.ui20.Logout_Btn.clicked.connect(self.open_Start_Screen)
        #Connecting the button to a function within this class
        self.ui20.change_First_Name.clicked.connect(self.open_Change_First_Name)
        #Connecting the button to a function within this class
        self.ui20.change_Last_Name.clicked.connect(self.open_Change_Last_Name)
        #Connecting the button to a function within this class
        self.ui20.change_Email.clicked.connect(self.open_Change_Email)
        #Connecting the button to a function within this class
        self.ui20.change_Phone_Number.clicked.connect(self.open_Change_Phone_Number)
        #Connecting the button to a function within this class
        self.ui20.change_Password.clicked.connect(self.open_Change_Password)
        #Connecting the button to a function within this class
        self.ui20.change_Card.clicked.connect(self.open_Card_Change)
        #Connecting the button to a function within this class
        self.ui20.change_Paypal.clicked.connect(self.open_Paypal_Change)
        #initialize the qss function
        self.qss()
        #Connecting the button to a function within this class
        self.ui20.pushButton.clicked.connect(self.findOrderButton)
        #Connecting the button to a function within this class
        self.ui20.accept_order.clicked.connect(self.emptySomething)
        #Connecting the button to a function within this class
        self.ui20.decline_order.clicked.connect(self.emptyEverything)
        # Updates the status to declined
        self.ui20.decline_order.clicked.connect(self.statusDeclined)
        # Updates the status to declined
        self.ui20.Completed_button.clicked.connect(self.statusAccepted)
        self.loaddata()
        pass__ = self.takePass('pass.txt')
        a, b, c, d = self.getDriver(pass__)
        self.phillOut(a, b, c, d)

    def statusDeclined(self):
        """
            Function updates the last row's status in journey table to declined.
        :return:
        """
        last_order_id = BackEnd().getLastRowJourneys()
        dataz().Update_status_journey('Declined', last_order_id)

    def statusAccepted(self):
        """
            Function updates the last row's status in journey table to accepted.
        :return:
        """
        last_order_id = BackEnd().getLastRowJourneys()
        dataz().Update_status_journey('Accepted', last_order_id)

    def findOrderButton(self):
        """Get last row from journey table and print its details"""
        start_location, destination, order_id = BackEnd().findLastJourney()
        self.getNewOrder(start_location, destination)
        #Setting text on the Label
        self.ui20.from_value.setText(start_location)
        #Setting text on the Label
        self.ui20.To_value.setText(destination)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def getDriver(self, v):
        """Get account details by id provided in pass.txt"""
        fn = dataz().get_driver_username_by_id(v)
        ln = dataz().get_driver_lastname_by_id(v)
        email = dataz().get_driver_email_by_id(v)
        pn = dataz().get_driver_pn_by_id(v)
        return fn, ln, email, pn

    def phillOut(self, fn, ln, email, pn):
        """Fill out account details."""
        #Setting text on the Label
        self.ui20.First_Name_Label.setText(fn)
        #Setting text on the Label
        self.ui20.Last_Name_Label.setText(ln)
        #Setting text on the Label
        self.ui20.Email_Label.setText(email)
        #Setting text on the Label
        self.ui20.Phone_Number_Label.setText(pn)
    #This function displays data from the database to the GUI using the QTableWidget
    def loaddata(self):
        """Previous trips table for current user."""
        connection = sqlite3.connect('assessment2.db')
        cur = connection.cursor()
        driverID = 1
        sqlstr = 'SELECT * FROM journey WHERE driver_ID = ?'
        tablerow = 0
        results = cur.execute(sqlstr, (driverID,))
        self.ui20.tableWidget.setRowCount(40)
        for row in results:
            self.ui20.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui20.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui20.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[5]))
            self.ui20.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[6]))
            self.ui20.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[13]))
            self.ui20.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[14]))
            tablerow += 1

    def emptyEverything(self):
        """Empty all the fields."""
        #Setting text on the Label
        self.ui20.sl_value.setText('')
        #Setting text on the Label
        self.ui20.el_value.setText('')
        #Setting text on the Label
        self.ui20.from_value.setText('')
        #Setting text on the Label
        self.ui20.To_value.setText('')

    def emptySomething(self):
        """Empty find order tab"""
        #Setting text on the Label
        self.ui20.sl_value.setText('')
        #Setting text on the Label
        self.ui20.el_value.setText('')

    def placeOrderToUpcomingJourney(self, start, end):
        """Setup upcoming journey tab"""
        #Setting text on the Label
        self.ui20.from_value.setText(start)
        #Setting text on the Label
        self.ui20.To_value.setText(end)


    def open_Start_Screen(self):
        self.o14 = StartScreen()
        #Show New Window
        self.o14.show()
        #Closes existing Window
        self.close()

    def open_Change_First_Name(self):
        self.o15 = change_Driver_First_Name()
        #Show New Window
        self.o15.show()
        #Closes existing Window
        self.close()

    def open_Change_Last_Name(self):
        self.o16 = change_Driver_Last_Name()
        #Show New Window
        self.o16.show()
        #Closes existing Window
        self.close()

    def open_Change_Email(self):
        self.o17 = change_Driver_Email()
        #Show New Window
        self.o17.show()
        #Closes existing Window
        self.close()

    def open_Change_Password(self):
        self.o18 = change_Driver_Password()
        #Show New Window
        self.o18.show()
        #Closes existing Window
        self.close()

    def open_Change_Phone_Number(self):
        self.o19 = change_Driver_Phone_Number()
        #Show New Window
        self.o19.show()
        #Closes existing Window
        self.close()

    def open_Card_Change(self):
        self.o20 = change_Driver_Card()
        #Show New Window
        self.o20.show()
        #Closes existing Window
        self.close()

    def open_Paypal_Change(self):
        self.o21 = change_Driver_Paypal()
        #Show New Window
        self.o21.show()
        #Closes existing Window
        self.close()

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def getNewOrder(self, start_point, end_point):
        self.ui20.sl_value.setText(start_point)
        self.ui20.el_value.setText(end_point)
#Classes provide a means of bundling data and functionality together
class StartScreen(QtWidgets.QWidget):
    def __init__(self):
        """[summary]
        The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        """
        super().__init__()
        """[summary]
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        """       
        self.ui1 = ui1()
        #setupUi takes a singe argument(widget) in which the user interface is created
        self.ui1.setupUi(self)
        #Connecting the button to a function within this class
        self.ui1.Login_Button.clicked.connect(self.open_Login)
        #Connecting the button to a function within this class
        self.ui1.Register_Button.clicked.connect(self.open_Register)
        #initialize the qss function
        self.qss()

    def open_Login(self):
        self.o1 = LoginScreen()
        #Show New Window
        self.o1.show()
        #Closes existing Window
        self.close()

    def open_Register(self):
        self.o2 = RegisterScreen()
        #Show New Window
        self.o2.show()
        #Closes existing Window
        self.close()

    def qss(self):
        """
        [summary]
        This loads a predefined Stylesheet which is in .qss fileformat
        """
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

#Intializes the Main method
#The main methods launches the application when the python file is run
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = StartScreen()
    #Show Window
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()