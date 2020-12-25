import sys
from PyQt5 import QtWidgets
from test2 import dataz
from StartScreen import Ui_Form1
from Login_Screen import Ui_Form2
from Registration_Screen import Ui_Form3
from User_Card import Ui_Form4
from User_Paypal import Ui_Form5
from Driver_Card import Ui_Form6
from Driver_Paypal import Ui_Form7
from Thank_You import Ui_Form8
from Verification_Screen import Ui_Form9
from Congratulations import Ui_Form10
from forgotChoices import Ui_Form11
from changePassword import Ui_Form12
from UserScreen import Ui_Form13
from BackEnd import BackEnd
from random import randint
import numpy as np
import sqlite3
conn = sqlite3.connect("assessment2.db")
c = conn.cursor()
        
class UserMainScreen(QtWidgets.QWidget):
    def __init__(self):
        super(UserMainScreen,self).__init__()
        self.ui13 = Ui_Form13()
        self.ui13.setupUi(self)
class changePassword(QtWidgets.QWidget):
    def __init__(self):
        super(changePassword,self).__init__()
        self.ui12 = Ui_Form12()
        self.ui12.setupUi(self)
        self.ui12.changePassword.clicked.connect(self.clos)
    def clos(self):
        self.close()
class forgotChoices(QtWidgets.QWidget):
    def __init__(self):
        super(forgotChoices,self).__init__()
        self.ui11 = Ui_Form11()
        self.ui11.setupUi(self)
        self.ui11.verify_button.clicked.connect(self.verify)
    def verify(self):
        self.o10 = changePassword()
        self.o10.show()
        self.close()
class Congratulations(QtWidgets.QWidget):
    def __init__(self):
        super(Congratulations,self).__init__()
        self.ui10 = Ui_Form10()
        self.ui10.setupUi(self)
        self.ui10.go2Login.clicked.connect(self.back2Login)
    def back2Login(self):
        self.o9 = LoginScreen()
        self.o9.show()
        self.close()
class Verification_Screen(QtWidgets.QWidget):
    def __init__(self):
        super(Verification_Screen,self).__init__()
        self.ui9 = Ui_Form9()
        self.ui9.setupUi(self)
        self.ui9.Complete_Verification.clicked.connect(self.go_to_Account_Activated)

    def go_to_Account_Activated(self):
        self.o8 = Congratulations()
        self.o8.show()
        self.close()
class Thank_You(QtWidgets.QWidget):
    def __init__(self):
        super(Thank_You,self).__init__()
        a = randint(0,1000)
        self.ui8 = Ui_Form8()
        self.ui8.setupUi(self)
        self.ui8.Verify_Now.clicked.connect(self.open_Verification_Screen)
        self.ui8.Security_Code.setText("%d"%a)
        # self.ui8.Security_Code.setText(self.Security_generator)
    def open_Verification_Screen(self):
        self.o7 = Verification_Screen()
        self.o7.show()
        self.close()  
class Driver_Paypal(QtWidgets.QWidget):
    def __init__(self):
        super(Driver_Paypal,self).__init__()
        self.ui7 = Ui_Form7()
        self.ui7.setupUi(self)
        self.ui7.Submit_Details4.clicked.connect(self.open_Thankyou)
    def open_Thankyou(self):
        self.o6 = Thank_You()
        self.o6.show()
        self.close()
    def take_Driver_Paypal_Inputs(self):
        driver_paypal_payme = self.ui7.Driver_Paypal_payme.text()
class Driver_Card(QtWidgets.QWidget):
    def __init__(self):
        super(Driver_Card,self).__init__()
        self.ui6 = Ui_Form6()
        self.ui6.setupUi(self)
        self.ui6.Submit_Details3.clicked.connect(self.open_Thankyou)
    def open_Thankyou(self):
        self.o6 = Thank_You()
        self.o6.show()
        self.close()
    def take_Driver_Card_Inputs(self):
        driver_card_name = self.ui6.Drive_Card_Name.text()
        driver_card_account_number = self.ui6.Driver_card_account_number.text()
        driver_sort_code1 = self.ui6.Driver_Card_SortCode1.text()
        driver_sort_code2 = self.ui6.Driver_Card_SortCode2.text()
        driver_sort_code3 = self.ui6.Driver_Card_SortCode3.text() 
class User_Paypal(QtWidgets.QWidget):
    def __init__(self):
        super(User_Paypal,self).__init__()
        self.ui5 = Ui_Form5()
        self.ui5.setupUi(self)
        self.ui5.Submit_Details2.clicked.connect(self.open_Thankyou)
    def open_Thankyou(self):
        self.o6 = Thank_You()
        self.o6.show()
        self.close()
    def take_User_Paypal_Inputs(self):
        user_paypal_email =  self.ui5.User_Paypal_Email.text()
        user_paypal_password = self.ui5.User_Paypal_Password.text()
class User_Card(QtWidgets.QWidget):
    def __init__(self):
        super(User_Card,self).__init__()
        self.ui4 = Ui_Form4()
        self.ui4.setupUi(self)
        self.ui4.Submit_Details1.clicked.connect(self.open_Thankyou)
    def open_Thankyou(self):
        self.o6 = Thank_You()
        self.o6.show()
        self.close()
    def take_User_Card_Inputs(self):
        user_card_name = self.ui4.User_Card_Name.text()
        user_card_number = self.ui4.User_Card_Number.text()
        user_card_cvv = self.ui4.User_Card_CVV.text()
class RegisterScreen(QtWidgets.QWidget):
    def __init__(self):
        super(RegisterScreen,self).__init__()
        self.ui3 = Ui_Form3()
        self.ui3.setupUi(self)
        self.ui3.User_Submit_Button.clicked.connect(self.User_Payment)
        self.ui3.Driver_Submit_Button.clicked.connect(self.Driver_Payment)
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
    def take_user_inputs(self):
        user_first_name = self.ui3.User_First_Name_Text.text()
        user_last_name = self.ui3.User_Last_Name_Text.text()
        user_email = self.ui3.User_Email_Text.text()
        user_contact_number = self.ui3.User_Contact_Number_Text.text()
        user_password = self.ui3.User_Password_Text.text()
        user_payment = self.ui3.comboBox.currentText()
        self.d1=dataz()
        self.d1.Insert_Into_customers(user_first_name,user_last_name,user_email,user_contact_number,user_password,user_payment)
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
    def User_Payment(self):
        self.take_user_inputs()
        if self.ui3.User_Password_Text.text() == self.ui3.User_Confirm_Password_Text.text():
            if self.ui3.comboBox.currentText()=="Card":
                self.ui3.User_Submit_Button.clicked.connect(self.open_User_Card)
            elif self.ui3.comboBox.currentText()=="PayPal":
                self.ui3.User_Submit_Button.clicked.connect(self.open_User_Paypal)
        else:
            self.ui3.User_Invalid_Password.setText("Passwords Mismatch, try again")
    def Driver_Payment(self):
        self.take_driver_inputs()
        if self.ui3.Driver_Password_Text.text() == self.ui3.Driver_Confirm_Password_Text.text():
            if self.ui3.comboBox_2.currentText()=="Card":
                self.ui3.Driver_Submit_Button.clicked.connect(self.open_Driver_Card)
            elif self.ui3.comboBox_2.currentText()=="PayPal":
                self.ui3.Driver_Submit_Button.clicked.connect(self.open_Driver_Paypal)
        else:
            self.ui3.Driver_Invalid_Password.setText("Passwords Mismatch, try again")
class LoginScreen(QtWidgets.QWidget):
    def __init__(self):
        super(LoginScreen,self).__init__()
        self.ui2 = Ui_Form2()
        self.ui2.setupUi(self)
        self.ui2.user_ForgotPass.clicked.connect(self.forgetPass)
        self.ui2.driver_ForgotPass.clicked.connect(self.forgetPass)
        self.ui2.user_Submit.clicked.connect(self.openLogin)
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
        self.ui1 = Ui_Form1()
        self.ui1.setupUi(self)
        self.ui1.Login_Button.clicked.connect(self.open_Login)
        self.ui1.Register_Button.clicked.connect(self.open_Register)    
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
