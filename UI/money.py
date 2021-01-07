import sys
from PyQt5 import QtWidgets, QtCore , QtGui
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
from BackEnd import BackEnd
from random import randint
import numpy as np
import sqlite3
import re
conn = sqlite3.connect("assessment2.db")
c = conn.cursor()
print("Check")

class UserMainScreen(QtWidgets.QWidget):
    def __init__(self):
        super(UserMainScreen,self).__init__()
        self.ui13 = ui13()
        self.ui13.setupUi(self)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
            self.setStyleSheet(fh.read())
        self.loaddata()

        start_point = self.ui13.comboBox.currentText()
        end_point = self.ui13.comboBox.currentText()
        car_type = self.ui13.comboBox.currentText()
    def loaddata(self):
        connection = sqlite3.connect('assessment2.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM journey'
        tablerow=0
        results = cur.execute(sqlstr)
        self.ui13.tableWidget.setRowCount(40)
        for row in results:
            self.ui13.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui13.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui13.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1


class changePassword(QtWidgets.QWidget):
    def __init__(self):
        super(changePassword,self).__init__()
        self.ui12 = ui12()
        self.ui12.setupUi(self)
        self.ui12.changePassword.clicked.connect(self.clos)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
            self.setStyleSheet(fh.read())
    def clos(self):
        self.close()
class forgotChoices(QtWidgets.QWidget):
    def __init__(self):
        super(forgotChoices,self).__init__()
        self.ui11 = ui11()
        self.ui11.setupUi(self)
        self.ui11.verify_button.clicked.connect(self.verify)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
            self.setStyleSheet(fh.read())
    def verify(self):
        self.o10 = changePassword()
        self.o10.show()
        self.close()
class Congratulations(QtWidgets.QWidget):
    def __init__(self):
        super(Congratulations,self).__init__()
        self.ui10 = ui10()
        self.ui10.setupUi(self)
        self.ui10.go2Login.clicked.connect(self.back2Login)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
            self.setStyleSheet(fh.read())        
    def back2Login(self):
        self.o9 = LoginScreen()
        self.o9.show()
        self.close()
class Verification_Screen(QtWidgets.QWidget):
    def __init__(self):
        super(Verification_Screen,self).__init__()
        self.ui9 = ui9()
        self.ui9.setupUi(self)
        self.ui9.Complete_Verification.clicked.connect(self.go_to_Account_Activated)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
            self.setStyleSheet(fh.read())
    def go_to_Account_Activated(self):
        self.o8 = Congratulations()
        self.o8.show()
        self.close()
class Thank_You(QtWidgets.QWidget):
    def __init__(self):
        super(Thank_You,self).__init__()
        a = randint(0,1000)
        self.ui8 = ui8()
        self.ui8.setupUi(self)
        self.ui8.Verify_Now.clicked.connect(self.open_Verification_Screen)
        self.ui8.Security_Code.setText("%d"%a)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
            self.setStyleSheet(fh.read())
        # self.ui8.Security_Code.setText(self.Security_generator)
    def open_Verification_Screen(self):
        self.o7 = Verification_Screen()
        self.o7.show()
        self.close()  
class Driver_Paypal(QtWidgets.QWidget):
    def __init__(self):
        super(Driver_Paypal,self).__init__()
        self.ui7 = ui7()
        self.ui7.setupUi(self)
        self.ui7.Submit_Details4.clicked.connect(self.open_Thankyou)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
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
        self.d5.Insert_into_driver_payments(driver_card_name,driver_card_account_number,driver_sort_code,driver_paypal_payme) 
class Driver_Card(QtWidgets.QWidget):
    def __init__(self):
        super(Driver_Card,self).__init__()
        self.ui6 = ui6()
        self.ui6.setupUi(self)
        self.ui6.Submit_Details3.clicked.connect(self.open_Thankyou)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
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
        self.d4.Insert_into_driver_payments(driver_card_name,driver_card_account_number,driver_sort_code,driver_paypal_payme) 
class User_Paypal(QtWidgets.QWidget):
    def __init__(self):
        super(User_Paypal,self).__init__()
        self.ui5 = ui5()
        self.ui5.setupUi(self)
        self.ui5.Submit_Details2.clicked.connect(self.open_Thankyou)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
            self.setStyleSheet(fh.read())
    def open_Thankyou(self):
        self.o6 = Thank_You()
        self.o6.show()
        self.close()
        self.take_User_Paypal_Inputs()
    def take_User_Paypal_Inputs(self):
        user_paypal_email =  self.ui5.User_Paypal_Email.text()
        user_paypal_password = self.ui5.User_Paypal_Password.text()
        user_card_name = 0
        user_card_number = 0
        user_card_cvv = 0
        self.d3 = dataz()
        self.d3.Insert_into_customer_payments(user_card_name,user_card_number,user_card_cvv,user_paypal_email,user_paypal_password)
class User_Card(QtWidgets.QWidget):
    def __init__(self):
        super(User_Card,self).__init__()
        self.ui4 = ui4()
        self.ui4.setupUi(self)
        self.ui4.Submit_Details1.clicked.connect(self.open_Thankyou)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
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
        self.d2=dataz()
        self.d2.Insert_into_customer_payments(user_card_name,user_card_number,user_card_cvv,user_paypal_email,user_paypal_password)
class RegisterScreen(QtWidgets.QWidget):
    def __init__(self):
        super(RegisterScreen,self).__init__()
        self.ui3 = ui3()
        self.ui3.setupUi(self)
        self.ui3.User_Submit_Button.clicked.connect(self.User_Payment)
        self.ui3.Driver_Submit_Button.clicked.connect(self.Driver_Payment)
        self.check_states1()
        self.check_states2()
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
            self.setStyleSheet(fh.read())
    def check_confirm_password_state(self):
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
    def check_password_state(self):
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
    def check_last_name_state(self):
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
    def check_first_name_state(self):
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
    def check_email_state(self):
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
    def check_contact_state(self):
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
    def check_states1(self):
        self.check_first_name_state()
        self.check_email_state()
        self.check_contact_state()
        self.check_last_name_state()
        self.check_password_state()
        self.check_confirm_password_state()
    def check_states2(self):
        self.ui3.User_Last_Name_Text.textEdited.connect(self.check_last_name_state)
        self.ui3.User_Last_Name_Text.textEdited.emit(self.ui3.User_Last_Name_Text.text())
        self.ui3.User_First_Name_Text.textEdited.connect(self.check_first_name_state)
        self.ui3.User_First_Name_Text.textEdited.emit(self.ui3.User_First_Name_Text.text())
        self.ui3.User_Email_Text.textEdited.connect(self.check_email_state)
        self.ui3.User_Email_Text.textEdited.emit(self.ui3.User_Email_Text.text())
        self.ui3.User_Contact_Number_Text.textEdited.connect(self.check_contact_state)
        self.ui3.User_Contact_Number_Text.textEdited.emit(self.ui3.User_Contact_Number_Text.text())
        self.ui3.User_Password_Text.textEdited.connect(self.check_password_state)
        self.ui3.User_Password_Text.textEdited.emit(self.ui3.User_Password_Text.text())
        self.ui3.User_Confirm_Password_Text.textEdited.connect(self.check_confirm_password_state)
        self.ui3.User_Confirm_Password_Text.textEdited.emit(self.ui3.User_Confirm_Password_Text.text())

    def take_user_inputs(self):
        # self.validate_user_email()
        user_first_name = self.ui3.User_First_Name_Text.text()
        user_last_name = self.ui3.User_Last_Name_Text.text()
        user_email = self.ui3.User_Email_Text.text()
        user_contact_number = self.ui3.User_Contact_Number_Text.text()
        user_password = self.ui3.User_Password_Text.text()
        user_payment = self.ui3.comboBox.currentText()
        self.d1=dataz()
        self.d1.Insert_Into_customers(user_first_name,user_last_name,user_email,user_contact_number,user_password,user_payment)
    def take_driver_inputs(self):
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
        self.d2=dataz()
        self.d2.Insert_Into_drivers(driver_first_name,driver_last_name,driver_email,driver_password,driver_contact_number,driver_license,driver_car_license,driver_car_make,driver_car_color,driver_payment)
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
        self.d9=dataz()
        self.d9.Delete_Duplicates_Customers()
    def Delete_Dup_Drivers(self):
        self.d10=dataz()
        self.d10.Delete_Duplicates_Drivers()
    def User_Payment(self):
        self.check_email_state()
        self.take_user_inputs()
        self.Delete_Dup_Customers() 
        if self.ui3.User_Password_Text.text() == self.ui3.User_Confirm_Password_Text.text():
            if self.ui3.comboBox.currentText()=="Card":
                self.ui3.User_Submit_Button.clicked.connect(self.open_User_Card)
            elif self.ui3.comboBox.currentText()=="PayPal":
                self.ui3.User_Submit_Button.clicked.connect(self.open_User_Paypal)
        else:
            self.ui3.User_Invalid_Password.setText("Passwords Mismatch, try again")

    def Driver_Payment(self):
        self.take_driver_inputs()
        self.Delete_Dup_Drivers()
        if self.ui3.Driver_Password_Text.text() == self.ui3.Driver_Confirm_Password_Text.text():
            if self.ui3.comboBox_2.currentText()=="Card":
                self.ui3.Driver_Submit_Button.clicked.connect(self.open_Driver_Card)
            elif self.ui3.comboBox_2.currentText()=="PayPal":
                self.ui3.Driver_Submit_Button.clicked.connect(self.open_Driver_Paypal)
        else:
            self.ui3.Driver_Invalid_Password.setText("Passwords Mismatch, try again")
    def containsDigits(self, s):
        for char in s:
            if char.isdigit():
                contains_digit = True
            else:
                contains_digit = False
        return contains_digit
    def emailCheck(self, m):
        if re.match(r"[^@]+@[^@]+\.[^@]+", m):
            return True
        else:
            return False

class LoginScreen(QtWidgets.QWidget):
    def __init__(self):
        super(LoginScreen,self).__init__()
        self.ui2 = ui2()
        self.ui2.setupUi(self)
        self.ui2.user_ForgotPass.clicked.connect(self.forgetPass)
        self.ui2.driver_ForgotPass.clicked.connect(self.forgetPass)
        self.ui2.user_Submit.clicked.connect(self.openLogin)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
            self.setStyleSheet(fh.read())
    def forgetPass(self):
        self.o11 = forgotChoices()
        self.o11.show()
    def openLogin(self):
        self.o12 = UserMainScreen()
        self.o12.show()
        self.close()
class StartScreen(QtWidgets.QWidget):
    def __init__(self):
        super(StartScreen,self).__init__()
        self.ui1 = ui1()
        self.ui1.setupUi(self)
        self.ui1.Login_Button.clicked.connect(self.open_Login)
        self.ui1.Register_Button.clicked.connect(self.open_Register)
        qss_file = 'QSS/OrangeDark.qss'
        with open(qss_file,"r") as fh:
            self.setStyleSheet(fh.read())    
    def open_Login(self):
        self.o1 = LoginScreen()
        self.o1.show()
        self.close()
    def open_Register(self):
        self.o2 = RegisterScreen()
        self.o2.show()
        self.close()
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = StartScreen()
    application.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()