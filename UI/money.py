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
from change_User_Password import Ui_Form as ui26
from BackEnd import BackEnd
from random import randint
import numpy as np
import sqlite3
import re

conn = sqlite3.connect("assessment2.db")
c = conn.cursor()
class change_Driver_Password(QtWidgets.QWidget):
    def __init__(self):
        super(change_Driver_Password,self).__init__()
        self.ui26 = ui26()
        self.ui26.setupUi(self)
        self.qss()
        self.ui26.changePasswordBtn.clicked.connect(self.pass_validator)

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        self.o21.show()
        self.close()

    def pass_validator(self):
        new_password = self.ui26.change_User_Password_Label.text()
        conf_new_password = self.ui26.change_User_Confirm_Password_Label.text()
        if new_password == conf_new_password:
            self.hit_Submit()
        else:
            self.ui26.Passwords_Mismatch.setText('Passwords Mismatch')
        
    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        emailn = self.ui26.change_User_Password_Label.text()
        dataz().Update_password_drivers(emailn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_
        
    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
class change_Driver_Phone_Number(QtWidgets.QWidget):
    def __init__(self):
        super(change_Driver_Phone_Number,self).__init__()
        self.ui25 = ui25()
        self.ui25.setupUi(self)
        self.qss()
        self.ui25.changePhoneNumberBtn.clicked.connect(self.hit_Submit)

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        phnn = self.ui25.change_User_PhoneNumber_Label.text()
        dataz().Update_phone_number_drivers(phnn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        self.o21.show()
        self.close()


    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
class change_Driver_Email(QtWidgets.QWidget):
    def __init__(self):
        super(change_Driver_Email,self).__init__()
        self.ui24 = ui24()
        self.ui24.setupUi(self)
        self.qss()
        self.ui24.changeEmailBtn.clicked.connect(self.hit_Submit)

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        self.o21.show()
        self.close()
        
    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        emailn = self.ui24.change_User_Email_Label.text()
        dataz().Update_Email_drivers(emailn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())       
class change_Driver_Last_Name(QtWidgets.QWidget):
    def __init__(self):
        super(change_Driver_Last_Name,self).__init__()
        self.ui23 = ui23()
        self.ui23.setupUi(self)
        self.ui23.ChangeLastNameBtn.clicked.connect(self.hit_Submit)
        self.qss()

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        lastn = self.ui23.change_User_LastName_Label.text()
        dataz().Update_last_name_drivers(lastn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = DriverScreen()
        self.o21.show()
        self.close()

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
class change_Driver_First_Name(QtWidgets.QWidget):
    def __init__(self):
        super(change_Driver_First_Name,self).__init__()
        self.ui22 = ui22()
        self.ui22.setupUi(self)
        self.ui22.ChangeFirstNameBtn.clicked.connect(self.hit_Submit)
        self.qss()

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = DriverScreen()
        self.o21.show()
        self.close()

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        firstn = self.ui22.change_User_FirstName_Label.text()
        dataz().Update_First_Name_customers(firstn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
class AdminScreen(QtWidgets.QWidget):
    def __init__(self):
        super(AdminScreen,self).__init__()
        self.ui21 = ui21()
        self.ui21.setupUi(self)
        self.qss()
        self.loadjourneys()
        self.loadcustomers()
        self.loaddrivers()
        self.ui21.Refresh_Btn.clicked.connect(self.hit_refresh)
        self.ui21.Logout_Btn.clicked.connect(self.hit_Logout)
        self.ui21.UpdateValueBtn.clicked.connect(self.Update_Values)
        self.ui21.DeleteValueBtn.clicked.connect(self.Delete_Row)
        self.ui21.InsertValueBtn.clicked.connect(self.Insert_value)

    def Insert_value(self):
        t = str(self.ui21.comboBox.currentText())
        print(t)
        dataz().create_row_by_admin(t)

    def Update_Values(self):
        table = self.ui21.comboBox.currentText()
        column = self.ui21.select_Column_Label.text()
        row = self.ui21.select_Row_Label.text()
        value = self.ui21.value_Change.text()
        dataz().Update_something_by_admin(table, column, row, value)


    def hit_Logout(self):
        self.oz = LoginScreen()
        self.oz.show()
        self.close()
    def hit_refresh(self):
        self.ui21 = AdminScreen()
        self.ui21.show()
        self.close()
    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def loadjourneys(self):
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
        table = self.ui21.comboBox.currentText()
        #select_Column = self.ui21.select_Column_Label.text()
        row = self.ui21.select_Row_Label.text()
        # change_Value = self.ui21.value_Change.text()
        dataz().Delete_Row_by_admin(table, row)

class change_User_Phone_Number(QtWidgets.QWidget):
    def __init__(self):
        super(change_User_Phone_Number, self).__init__()
        self.ui19 = ui19()
        self.ui19.setupUi(self)
        self.qss()
        self.ui19.changePhoneNumberBtn.clicked.connect(self.hit_Submit)

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        phnn = self.ui19.change_User_PhoneNumber_Label.text()
        dataz().Update_phone_number_customers(phnn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        self.o21.show()
        self.close()


    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

class change_User_Password(QtWidgets.QWidget):
    def __init__(self):
        super(change_User_Password, self).__init__()
        self.ui18 = ui18()
        self.ui18.setupUi(self)
        self.qss()
        self.ui18.changePasswordBtn.clicked.connect(self.pass_validator)

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        self.o21.show()
        self.close()

    def pass_validator(self):
        new_password = self.ui18.change_User_Password_Label.text()
        conf_new_password = self.ui18.change_User_Confirm_Password_Label.text()
        if new_password == conf_new_password:
            self.hit_Submit()
        else:
            self.ui18.Passwords_Mismatch.setText('Passwords Mismatch')
        
    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        emailn = self.ui18.change_User_Password_Label.text()
        dataz().Update_password_customers(emailn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_
        
    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

class change_User_Email(QtWidgets.QWidget):
    def __init__(self):
        super(change_User_Email, self).__init__()
        self.ui17 = ui17()
        self.ui17.setupUi(self)
        self.qss()
        self.ui17.changeEmailBtn.clicked.connect(self.hit_Submit)

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        self.o21.show()
        self.close()
        
    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        emailn = self.ui17.change_User_Email_Label.text()
        dataz().Update_Email_customers(emailn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

class change_User_LastName(QtWidgets.QWidget):
    def __init__(self):
        super(change_User_LastName, self).__init__()
        self.ui16 = ui16()
        self.ui16.setupUi(self)
        self.ui16.ChangeLastNameBtn.clicked.connect(self.hit_Submit)
        self.qss()

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        lastn = self.ui16.change_User_LastName_Label.text()
        dataz().Update_Last_Name_customers(lastn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        self.o21.show()
        self.close()

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())


class change_User_FirstName(QtWidgets.QWidget):
    def __init__(self):
        super(change_User_FirstName, self).__init__()
        self.ui15 = ui15()
        self.ui15.setupUi(self)
        self.ui15.ChangeFirstNameBtn.clicked.connect(self.hit_Submit)
        self.qss()

    def hit_Submit(self):
        self.database_connectinator()
        self.o21 = UserMainScreen()
        self.o21.show()
        self.close()

    def database_connectinator(self):
        pass__ = self.takePass('pass.txt')
        firstn = self.ui15.change_User_FirstName_Label.text()
        dataz().Update_First_Name_customers(firstn,pass__)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

class User_Submit_Payment(QtWidgets.QWidget):
    def __init__(self):
        super(User_Submit_Payment, self).__init__()
        self.ui14 = ui14()
        self.ui14.setupUi(self)
        self.qss()
        self.ui14.User_Submit_Payment_Method.clicked.connect(self.clos)

    def clos(self):
        self.close()

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

class Congratulations(QtWidgets.QWidget):
    def __init__(self):
        super(Congratulations, self).__init__()
        self.ui10 = ui10()
        self.ui10.setupUi(self)
        self.qss()
        self.ui10.go2Login.clicked.connect(self.back2Login)

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def back2Login(self):
        self.o9 = LoginScreen()
        self.o9.show()
        self.close()


class Verification_Screen(QtWidgets.QWidget):
    def __init__(self):
        super(Verification_Screen, self).__init__()
        self.ui9 = ui9()
        self.ui9.setupUi(self)
        self.qss()
        self.ui9.Complete_Verification.clicked.connect(self.go_to_Account_Activated)

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def go_to_Account_Activated(self):
        self.o8 = Congratulations()
        self.o8.show()
        self.close()


class Thank_You(QtWidgets.QWidget):
    def __init__(self):
        super(Thank_You, self).__init__()
        a = randint(0, 1000)
        self.ui8 = ui8()
        self.ui8.setupUi(self)
        self.qss()
        self.ui8.Verify_Now.clicked.connect(self.open_Verification_Screen)
        self.ui8.Security_Code.setText("%d" % a)

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())
        # self.ui8.Security_Code.setText(self.Security_generator)

    def open_Verification_Screen(self):
        self.o7 = Verification_Screen()
        self.o7.show()
        self.close()


class Driver_Paypal(QtWidgets.QWidget):
    def __init__(self):
        super(Driver_Paypal, self).__init__()
        self.ui7 = ui7()
        self.ui7.setupUi(self)
        self.qss()
        self.ui7.Submit_Details4.clicked.connect(self.open_Thankyou)

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def open_Thankyou(self):
        self.o6 = Thank_You()
        self.o6.show()
        self.close()
        self.take_Driver_Paypal_Inputs()

    def take_Driver_Paypal_Inputs(self):
        driver_paypal_payme = self.ui7.Driver_Paypal_payme.text()
        driver_card_name = 0
        driver_card_account_number = 0
        driver_sort_code = 0
        self.d5 = dataz()
        self.d5.payment_method_driver(driver_card_name, driver_card_account_number, driver_sort_code,
                                            driver_paypal_payme,driver_first_name)


class Driver_Card(QtWidgets.QWidget):
    def __init__(self):
        super(Driver_Card, self).__init__()
        self.ui6 = ui6()
        self.ui6.setupUi(self)
        self.qss()
        self.ui6.Submit_Details3.clicked.connect(self.open_Thankyou)

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def open_Thankyou(self):
        self.o6 = Thank_You()
        self.o6.show()
        self.close()
        self.take_Driver_Card_Inputs()

    def take_Driver_Card_Inputs(self):
        driver_card_name = self.ui6.Drive_Card_Name.text()
        driver_card_account_number = self.ui6.Driver_card_account_number.text()
        driver_sort_code1 = self.ui6.Driver_Card_SortCode1.text()
        driver_sort_code2 = self.ui6.Driver_Card_SortCode2.text()
        driver_sort_code3 = self.ui6.Driver_Card_SortCode3.text()
        driver_sort_code = str(driver_sort_code1) + "-" + str(driver_sort_code2) + "-" + str(driver_sort_code3)
        driver_paypal_payme = 0
        self.d4 = dataz()
        self.d4.payment_method_driver(driver_card_name, driver_card_account_number, driver_sort_code,
                                            driver_paypal_payme,driver_first_name)


class User_Paypal(QtWidgets.QWidget):
    def __init__(self):
        super(User_Paypal, self).__init__()
        self.ui5 = ui5()
        self.ui5.setupUi(self)
        self.qss()
        self.ui5.Submit_Details2.clicked.connect(self.open_Thankyou)

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def open_Thankyou(self):
        self.o6 = Thank_You()
        self.o6.show()
        self.close()
        self.take_User_Paypal_Inputs()

    def take_User_Paypal_Inputs(self):
        user_paypal_email = self.ui5.User_Paypal_Email.text()
        user_paypal_password = self.ui5.User_Paypal_Password.text()
        user_card_name = 0
        user_card_number = 0
        user_card_cvv = 0
        self.d3 = dataz()
        self.d3.payment_method_customers(user_card_name, user_card_number, user_card_cvv, user_paypal_email,
                                              user_paypal_password,user_first_name)


class User_Card(QtWidgets.QWidget):
    def __init__(self):
        super(User_Card, self).__init__()
        self.ui4 = ui4()
        self.ui4.setupUi(self)
        self.qss()
        self.ui4.Submit_Details1.clicked.connect(self.open_Thankyou)

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def open_Thankyou(self):
        self.o6 = Thank_You()
        self.o6.show()
        self.close()
        self.take_User_Card_Inputs()

    def take_User_Card_Inputs(self):
        user_card_name = self.ui4.User_Card_Name.text()
        user_card_number = self.ui4.User_Card_Number.text()
        user_card_cvv = self.ui4.User_Card_CVV.text()
        user_paypal_email = 0
        user_paypal_password = 0
        self.d2 = dataz()
        self.d2.payment_method_customers(user_card_name, user_card_number, user_card_cvv, user_paypal_email,
                                              user_paypal_password,user_first_name)


class RegisterScreen(QtWidgets.QWidget):
    def __init__(self):
        super(RegisterScreen, self).__init__()
        self.ui3 = ui3()
        self.ui3.setupUi(self)
        self.qss()
        self.ui3.User_Submit_Button.clicked.connect(self.User_Payment)
        self.ui3.Driver_Submit_Button.clicked.connect(self.Driver_Payment)
        self.user_check_states1()
        self.user_check_states2()
        self.driver_check_states1()
        self.driver_check_states2()

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def driver_check_car_color_state(self):
        input_car_color_name = self.ui3.Driver_Car_Color
        regexp = QtCore.QRegExp(r"^[A-Za-z -]+$")
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_car_color_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_car_make_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_car_license_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_drivers_license_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_confirm_password_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_confirm_password_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_password_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_password_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_last_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_last_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_first_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_first_name.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_email.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_email.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_contact_number.text(), 0)[0]
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
        validator = QtGui.QRegExpValidator(regexp)
        state = validator.validate(input_contact_number.text(), 0)[0]
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
        self.ui3.Driver_Car_Color.textEdited.emit(self.ui3.Driver_Car_Color.text())
        self.ui3.Driver_Car_Make_Text.textEdited.connect(self.driver_check_car_make_state)
        self.ui3.Driver_Car_Make_Text.textEdited.emit(self.ui3.Driver_Car_Make_Text.text())
        self.ui3.Driver_Car_Number.textEdited.connect(self.driver_check_car_license_state)
        self.ui3.Driver_Car_Number.textEdited.emit(self.ui3.Driver_Car_Number.text())
        self.ui3.Driver_License_Number.textEdited.connect(self.driver_check_drivers_license_state)
        self.ui3.Driver_License_Number.textEdited.emit(self.ui3.Driver_License_Number.text())
        self.ui3.Driver_Last_Name_Text.textEdited.connect(self.driver_check_last_name_state)
        self.ui3.Driver_Last_Name_Text.textEdited.emit(self.ui3.Driver_Last_Name_Text.text())
        self.ui3.Driver_First_Name_Text.textEdited.connect(self.driver_check_first_name_state)
        self.ui3.Driver_First_Name_Text.textEdited.emit(self.ui3.Driver_First_Name_Text.text())
        self.ui3.Driver_Email_Text.textEdited.connect(self.driver_check_email_state)
        self.ui3.Driver_Email_Text.textEdited.emit(self.ui3.Driver_Email_Text.text())
        self.ui3.Driver_Phone_Number_Text.textEdited.connect(self.driver_check_contact_state)
        self.ui3.Driver_Phone_Number_Text.textEdited.emit(self.ui3.Driver_Phone_Number_Text.text())
        self.ui3.Driver_Password_Text.textEdited.connect(self.driver_check_password_state)
        self.ui3.Driver_Password_Text.textEdited.emit(self.ui3.Driver_Password_Text.text())
        self.ui3.Driver_Confirm_Password_Text.textEdited.connect(self.driver_check_confirm_password_state)
        self.ui3.Driver_Confirm_Password_Text.textEdited.emit(self.ui3.Driver_Confirm_Password_Text.text())

    def user_check_states2(self):
        self.ui3.User_Last_Name_Text.textEdited.connect(self.user_check_last_name_state)
        self.ui3.User_Last_Name_Text.textEdited.emit(self.ui3.User_Last_Name_Text.text())
        self.ui3.User_First_Name_Text.textEdited.connect(self.user_check_first_name_state)
        self.ui3.User_First_Name_Text.textEdited.emit(self.ui3.User_First_Name_Text.text())
        self.ui3.User_Email_Text.textEdited.connect(self.user_check_email_state)
        self.ui3.User_Email_Text.textEdited.emit(self.ui3.User_Email_Text.text())
        self.ui3.User_Contact_Number_Text.textEdited.connect(self.user_check_contact_state)
        self.ui3.User_Contact_Number_Text.textEdited.emit(self.ui3.User_Contact_Number_Text.text())
        self.ui3.User_Password_Text.textEdited.connect(self.user_check_password_state)
        self.ui3.User_Password_Text.textEdited.emit(self.ui3.User_Password_Text.text())
        self.ui3.User_Confirm_Password_Text.textEdited.connect(self.user_check_confirm_password_state)
        self.ui3.User_Confirm_Password_Text.textEdited.emit(self.ui3.User_Confirm_Password_Text.text())

    def take_user_inputs(self):
        global user_first_name
        user_first_name = self.ui3.User_First_Name_Text.text()
        user_last_name = self.ui3.User_Last_Name_Text.text()
        user_email = self.ui3.User_Email_Text.text()
        user_contact_number = self.ui3.User_Contact_Number_Text.text()
        user_password = self.ui3.User_Password_Text.text()
        user_payment = self.ui3.comboBox.currentText()
        self.d1 = dataz()
        self.d1.Insert_Into_customers(user_first_name, user_last_name, user_email, user_contact_number, user_password, user_payment)

    def take_driver_inputs(self):
        global driver_first_name
        driver_first_name = self.ui3.Driver_First_Name_Text.text()
        driver_last_name = self.ui3.Driver_Last_Name_Text.text()
        driver_email = self.ui3.Driver_Email_Text.text()
        driver_password = self.ui3.Driver_Password_Text.text()
        driver_contact_number = self.ui3.Driver_Phone_Number_Text.text()
        driver_license = self.ui3.Driver_License_Number.text()
        driver_car_license = self.ui3.Driver_Car_Number.text()
        driver_car_make = self.ui3.Driver_Car_Make_Text.text()
        driver_car_color = self.ui3.Driver_Car_Color.text()
        driver_payment = self.ui3.comboBox_2.currentText()
        self.d2 = dataz()
        self.d2.Insert_Into_drivers(driver_first_name, driver_last_name, driver_email, driver_password, driver_contact_number, driver_license, driver_car_license, driver_car_make, driver_car_color, driver_payment)

    def open_User_Card(self):
        self.o2 = User_Card()
        self.o2.show()
        self.close()

    def open_User_Paypal(self):
        self.o3 = User_Paypal()
        self.o3.show()
        self.close()

    def open_Driver_Card(self):
        self.o4 = Driver_Card()
        self.o4.show()
        self.close()

    def open_Driver_Paypal(self):
        self.o5 = Driver_Paypal()
        self.o5.show()
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
        if self.ui3.User_Password_Text.text() == self.ui3.User_Confirm_Password_Text.text():
            if self.ui3.comboBox.currentText() == "Card":
                self.ui3.User_Submit_Button.clicked.connect(self.open_User_Card)
            elif self.ui3.comboBox.currentText() == "PayPal":
                self.ui3.User_Submit_Button.clicked.connect(self.open_User_Paypal)
        else:
            self.ui3.User_Invalid_Password.setText("Passwords Mismatch, try again")

    def Driver_Payment(self):
        self.take_driver_inputs()
        self.Delete_Dup_Drivers()
        if self.ui3.Driver_Password_Text.text() == self.ui3.Driver_Confirm_Password_Text.text():
            if self.ui3.comboBox_2.currentText() == "Card":
                self.ui3.Driver_Submit_Button.clicked.connect(self.open_Driver_Card)
            elif self.ui3.comboBox_2.currentText() == "PayPal":
                self.ui3.Driver_Submit_Button.clicked.connect(self.open_Driver_Paypal)
        else:
            self.ui3.Driver_Invalid_Password.setText("Passwords Mismatch, try again")

    def containsDigits(self, s):
        for char in s:
            if char.isdigit():
                contains_digit = True
            else:
                contains_digit = False
        # return contains_digit

    def emailCheck(self, m):
        if re.match(r"[^@]+@[^@]+\.[^@]+", m):
            return True
        else:
            return False


class LoginScreen(QtWidgets.QWidget):
    def __init__(self):
        super(LoginScreen, self).__init__()
        self.ui2 = ui2()
        self.ui2.setupUi(self)
        self.qss()
        self.ui2.user_Submit.clicked.connect(self.userChecker)
        self.ui2.driver_Submit.clicked.connect(self.driverChecker)
        self.ui2.admin_Submit.clicked.connect(self.adminChecker)

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def openUserLogin(self):
        self.o12 = UserMainScreen()
        self.o12.show()
        self.close()

    def openDriverLogin(self):
        self.o21 = DriverScreen()
        self.o21.show()
        id_ = DriverScreen().takePass('pass.txt')
        self.close()

    def adminChecker(self):
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
            self.ui2.user_login_Fail.setText("Try Again")

    def openAdminLogin(self):
        self.o22 = AdminScreen()
        self.o22.show()
        self.close()

    def pushToTxt(self, file, id):
        with open(file, 'w') as f:
            id = str(id)
            f.write(id)

    def userChecker(self):
        """Login verification for the customers."""
        user_login = str(self.ui2.userLoginEC.text())
        user_Password = str(self.ui2.userPass.text())
        self.o13 = dataz()
        try:
            c = self.o13.get_customer_userID_by_password(user_Password)
        except TypeError:
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
            self.ui2.user_login_Fail.setText("Try Again")

    def driverChecker(self):
        """Login verification for the drivers."""
        driver_login = str(self.ui2.driverLoginEC.text())
        driver_password = str(self.ui2.driverPass.text())
        self.o13 = dataz()
        try:
            c = self.o13.get_driver_driverID_by_password(driver_password)
        except TypeError:
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
            self.ui2.driver_login_Fail.setText('Try Again')


class UserMainScreen(QtWidgets.QWidget):
    def __init__(self):
        super(UserMainScreen, self).__init__()
        self.ui13 = ui13()
        self.ui13.setupUi(self)
        self.loaddata()
        self.ui13.Select_Payment_Method_Btn.clicked.connect(self.open_User_Payment_Options)
        self.ui13.Logout_Btn.clicked.connect(self.open_Start_Screen)
        self.ui13.change_First_Name.clicked.connect(self.open_Change_First_Name)
        self.ui13.change_Last_Name.clicked.connect(self.open_Change_Last_Name)
        self.ui13.change_Email.clicked.connect(self.open_Change_Email)
        self.ui13.change_Phone_Number.clicked.connect(self.open_Change_Phone_Number)
        self.ui13.change_Password.clicked.connect(self.open_Change_Password)
        self.ui13.change_Card.clicked.connect(self.open_Card_Change)
        self.ui13.change_Paypal.clicked.connect(self.open_Paypal_Change)
        self.ui13.Refresh2.clicked.connect(self.hit_refresh)
        self.ui13.Refresh_Btn.clicked.connect(self.hit_refresh)
        self.ui13.pushButton.clicked.connect(self.declineButton)
        self.ui13.pushButton.clicked.connect(self.deleteDeclined)
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
        self.ui13.Upcoming_Date_Lbl.setText('')
        self.ui13.Upcoming_Time_Lbl.setText('')
        self.ui13.Upcomin_Journey_ID_Lbl.setText('')
        self.ui13.Upcoming_Start_Location_Lbl.setText('')
        self.ui13.Upcoming_Destination_Lbl.setText('')
        self.ui13.Upcoming_Driver_Name_Lbl.setText('')
        self.ui13.Car_Class_Label.setText('')
        self.ui13.Upcoming_Car_Make_Lbl.setText('')
        self.ui13.Upcoming_Car_Color_Lbl.setText('')
        self.ui13.Upcoming_ETA.setText('')
        self.ui13.Price_Label.setText('')
        self.ui13.Distance_Label.setText('')
        self.ui13.Car_Number_Lbl.setText('')

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def getCustomer(self, id):
        a = dataz().get_customer_username_by_id(id)
        b = dataz().get_customer_lastname_by_id(id)
        c = dataz().get_customer_email_by_id(id)
        d = dataz().get_customer_phone_number_by_id(id)
        return a, b, c, d

    def phillOut(self, fn, ln, email, pn):
        self.ui13.First_Name_Label.setText(fn)
        self.ui13.Last_Name_Label.setText(ln)
        self.ui13.Email_Label.setText(email)
        self.ui13.Phone_Number_Label.setText(pn)

    def getNewBookingItems(self):
        start_point = self.ui13.comboBox.currentText()
        end_point = self.ui13.comboBox_2.currentText()
        car_type = self.ui13.comboBox_3.currentText()
        distance, price = BackEnd.priceCalc(BackEnd.locations[start_point], BackEnd.locations[end_point])
        distance = format(distance, '.2f') + 'km'
        price = format(price, '.2f') + '£'
        date, time = BackEnd().getDateAndTime()
        jID = BackEnd().getJourneyID()
        driver_name, car_number, car_make, car_color = BackEnd().assignTheDriver()
        eta = BackEnd().getETA()
        self.ui13.Upcoming_Date_Lbl.setText(date)
        self.ui13.Upcoming_Time_Lbl.setText(time)
        self.ui13.Upcomin_Journey_ID_Lbl.setText(jID)
        self.ui13.Upcoming_Start_Location_Lbl.setText(start_point)
        self.ui13.Upcoming_Destination_Lbl.setText(end_point)
        self.ui13.Upcoming_Driver_Name_Lbl.setText(driver_name)
        self.ui13.Car_Class_Label.setText(car_type)
        self.ui13.Car_Number_Lbl.setText(car_number)
        self.ui13.Upcoming_Car_Make_Lbl.setText(car_make)
        self.ui13.Upcoming_Car_Color_Lbl.setText(car_color)
        self.ui13.Upcoming_ETA.setText(eta)
        self.ui13.Price_Label.setText(price)
        self.ui13.Distance_Label.setText(distance)
        userID = self.takePass('pass.txt')
        customer_name, b, c, d = self.getCustomer(userID)
        dataz().Insert_Into_journey(date,time,jID,userID, customer_name, start_point,end_point,driver_name,car_type,car_make,car_color,price,distance)
    def loaddata(self):
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

    def open_User_Payment_Options(self):
        self.o13 = User_Submit_Payment()
        self.o13.show()
        self.getNewBookingItems()

    def open_Start_Screen(self):
        self.o14 = StartScreen()
        self.o14.show()
        self.close()

    def open_Change_First_Name(self):
        self.o15 = change_User_FirstName()
        self.o15.show()
        self.close()
        
    def open_Change_Last_Name(self):
        self.o16 = change_User_LastName()
        self.o16.show()
        self.close()

    def open_Change_Email(self):
        self.o17 = change_User_Email()
        self.o17.show()
        self.close()

    def open_Change_Password(self):
        self.o18 = change_User_Password()
        self.o18.show()
        self.close()

    def open_Change_Phone_Number(self):
        self.o19 = change_User_Phone_Number()
        self.o19.show()
        self.close()

    def open_Card_Change(self):
        self.o20 = User_Card()
        self.o20.show()
        self.close()

    def open_Paypal_Change(self):
        self.o21 = User_Paypal()
        self.o21.show()
        self.close()

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def hit_refresh(self):
        self.ox = UserMainScreen()
        self.ox.show()
        self.close()


class DriverScreen(QtWidgets.QWidget):
    def __init__(self):
        super(DriverScreen, self).__init__()
        self.ui20 = ui20()
        self.ui20.setupUi(self)
        # self.ui20.Select_Payment_Method_Btn.clicked.connect(self.open_User_Payment_Options)
        self.ui20.Logout_Btn.clicked.connect(self.open_Start_Screen)
        self.ui20.change_First_Name.clicked.connect(self.open_Change_First_Name)
        self.ui20.change_Last_Name.clicked.connect(self.open_Change_Last_Name)
        self.ui20.change_Email.clicked.connect(self.open_Change_Email)
        self.ui20.change_Phone_Number.clicked.connect(self.open_Change_Phone_Number)
        self.ui20.change_Password.clicked.connect(self.open_Change_Password)
        self.ui20.change_Card.clicked.connect(self.open_Card_Change)
        self.ui20.change_Paypal.clicked.connect(self.open_Paypal_Change)
        self.qss()
        self.ui20.pushButton.clicked.connect(self.findOrderButton)
        self.ui20.accept_order.clicked.connect(self.emptySomething)
        self.ui20.accept_order.clicked.connect(self.deleteDeclined)
        # accept button has to push to journey table with status accepted
        self.ui20.decline_order.clicked.connect(self.emptyEverything)
        self.ui20.decline_order.clicked.connect(self.deleteDeclined)
        # decline button has to push to journey table with status declined
        self.loaddata()
        #pass__ = self.takePass('pass.txt')
        #a, b, c, d = self.getDriver(pass__)
        #self.phillOut(a, b, c, d)

    def deleteDeclined(self):
        """
            Function calculates amount of orders in orders table and deletes the last one.
        :return:
        """
        last_order_id = BackEnd().getLastRowOrders()
        dataz().Delete_Row_orders(last_order_id)

    def findOrderButton(self):
        start_location, destination, order_id = BackEnd().findLastOrder()
        self.getNewOrder(start_location, destination)
        self.ui20.from_value.setText(start_location)
        self.ui20.To_value.setText(destination)

    def takePass(self, file):
        with open(file, 'r') as f:
            id_ = f.read()
            return id_

    def getDriver(self, v):
        fn = dataz().get_driver_username_by_id(v)
        ln = dataz().get_driver_lastname_by_id(v)
        email = dataz().get_driver_email_by_id(v)
        pn = dataz().get_driver_pn_by_id(v)
        return fn, ln, email, pn

    def phillOut(self, fn, ln, email, pn):
        self.ui20.First_Name_Label.setText(fn)
        self.ui20.Last_Name_Label.setText(ln)
        self.ui20.Email_Label.setText(email)
        self.ui20.Phone_Number_Label.setText(pn)

    def loaddata(self):
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
        self.ui20.sl_value.setText('')
        self.ui20.el_value.setText('')
        self.ui20.from_value.setText('')
        self.ui20.To_value.setText('')

    def emptySomething(self):
        self.ui20.sl_value.setText('')
        self.ui20.el_value.setText('')

    def placeOrderToUpcomingJourney(self, start, end):
        self.ui20.from_value.setText(start)
        self.ui20.To_value.setText(end)

    def open_User_Payment_Options(self):
        self.o13 = User_Submit_Payment()
        self.o13.show()
        self.getNewBookingItems()

    def open_Start_Screen(self):
        self.o14 = StartScreen()
        self.o14.show()
        self.close()

    def open_Change_First_Name(self):
        self.o15 = change_Driver_First_Name()
        self.o15.show()
        self.close()

    def open_Change_Last_Name(self):
        self.o16 = change_Driver_Last_Name()
        self.o16.show()
        self.close()

    def open_Change_Email(self):
        self.o17 = change_Driver_Email()
        self.o17.show()
        self.close()

    def open_Change_Password(self):
        self.o18 = change_Driver_Password()
        self.o18.show()
        self.close()

    def open_Change_Phone_Number(self):
        self.o19 = change_Driver_Phone_Number()
        self.o19.show()
        self.close()

    def open_Card_Change(self):
        self.o20 = Driver_Card()
        self.o20.show()
        self.close()

    def open_Paypal_Change(self):
        self.o21 = Driver_Paypal()
        self.o21.show()
        self.close()

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def getNewOrder(self, start_point, end_point):
        self.ui20.sl_value.setText(start_point)
        self.ui20.el_value.setText(end_point)


class StartScreen(QtWidgets.QWidget):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.ui1 = ui1()
        self.ui1.setupUi(self)
        self.ui1.Login_Button.clicked.connect(self.open_Login)
        self.ui1.Register_Button.clicked.connect(self.open_Register)
        self.qss()
        # qss_file = 'QSS/OrangeDark.qss'
        # with open(qss_file,"r") as fh:
        #     self.setStyleSheet(fh.read())

    def open_Login(self):
        self.o1 = LoginScreen()
        self.o1.show()
        self.close()

    def open_Register(self):
        self.o2 = RegisterScreen()
        self.o2.show()
        self.close()

    def qss(self):
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file, "r") as fh:
            self.setStyleSheet(fh.read())


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = StartScreen()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()