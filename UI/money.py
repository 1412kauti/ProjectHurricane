import sys
from PyQt5 import QtWidgets

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
        self.ui8 = Ui_Form8()
        self.ui8.setupUi(self)
        self.ui8.Verify_Now.clicked.connect(self.open_Verification_Screen)
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
class RegisterScreen(QtWidgets.QWidget):
    def __init__(self):
        super(RegisterScreen,self).__init__()
        self.ui3 = Ui_Form3()
        self.ui3.setupUi(self)
        self.ui3.User_Submit_Button.clicked.connect(self.User_Payment)
        self.ui3.Driver_Submit_Button.clicked.connect(self.Driver_Payment)
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
        if self.ui3.comboBox.currentText()=="Card":
            self.ui3.User_Submit_Button.clicked.connect(self.open_User_Card)
        elif self.ui3.comboBox.currentText()=="PayPal":
            self.ui3.User_Submit_Button.clicked.connect(self.open_User_Paypal)
    def Driver_Payment(self):
        if self.ui3.comboBox_2.currentText()=="Card":
            self.ui3.Driver_Submit_Button.clicked.connect(self.open_Driver_Card)
        elif self.ui3.comboBox_2.currentText()=="PayPal":
            self.ui3.Driver_Submit_Button.clicked.connect(self.open_Driver_Paypal)
class LoginScreen(QtWidgets.QWidget):
    def __init__(self):
        super(LoginScreen,self).__init__()
        self.ui2 = Ui_Form2()
        self.ui2.setupUi(self)
        self.ui2.user_ForgotPass.clicked.connect(self.forgetPass)
        self.ui2.driver_ForgotPass.clicked.connect(self.forgetPass)
    def forgetPass(self):
        self.o11 = forgotChoices()
        self.o11.show()

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
