# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registration_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(500, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 500))
        Form.setMaximumSize(QtCore.QSize(500, 500))
        Form.setStyleSheet("")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 30, 491, 401))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 0, 15)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(40)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.User_First_Name_Text = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.User_First_Name_Text.setObjectName("User_First_Name_Text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.User_First_Name_Text)
        self.User_Last_Name_Text = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.User_Last_Name_Text.setObjectName("User_Last_Name_Text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.User_Last_Name_Text)
        self.User_Email_Text = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.User_Email_Text.setObjectName("User_Email_Text")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.User_Email_Text)
        self.User_Password_Text = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.User_Password_Text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.User_Password_Text.setObjectName("User_Password_Text")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.User_Password_Text)
        self.User_Confirm_Password_Text = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.User_Confirm_Password_Text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.User_Confirm_Password_Text.setObjectName("User_Confirm_Password_Text")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.User_Confirm_Password_Text)
        self.User_Contact_Number_Text = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.User_Contact_Number_Text.setMaxLength(10)
        self.User_Contact_Number_Text.setObjectName("User_Contact_Number_Text")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.User_Contact_Number_Text)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 430, 491, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.User_Submit_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.User_Submit_Button.sizePolicy().hasHeightForWidth())
        self.User_Submit_Button.setSizePolicy(sizePolicy)
        self.User_Submit_Button.setObjectName("User_Submit_Button")
        self.verticalLayout.addWidget(self.User_Submit_Button)
        self.User_Invalid_Password = QtWidgets.QLabel(self.tab)
        self.User_Invalid_Password.setGeometry(QtCore.QRect(0, 5, 481, 21))
        self.User_Invalid_Password.setText("")
        self.User_Invalid_Password.setAlignment(QtCore.Qt.AlignCenter)
        self.User_Invalid_Password.setObjectName("User_Invalid_Password")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 491, 411))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(10, 10, 0, 5)
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(14)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Driver_First_Name_Text = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.Driver_First_Name_Text.setObjectName("Driver_First_Name_Text")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Driver_First_Name_Text)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.Driver_Last_Name_Text = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.Driver_Last_Name_Text.setObjectName("Driver_Last_Name_Text")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Driver_Last_Name_Text)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.Driver_Email_Text = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.Driver_Email_Text.setObjectName("Driver_Email_Text")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Driver_Email_Text)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.Driver_Password_Text = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.Driver_Password_Text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Driver_Password_Text.setObjectName("Driver_Password_Text")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Driver_Password_Text)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.Driver_Confirm_Password_Text = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.Driver_Confirm_Password_Text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Driver_Confirm_Password_Text.setObjectName("Driver_Confirm_Password_Text")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Driver_Confirm_Password_Text)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.Driver_Phone_Number_Text = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.Driver_Phone_Number_Text.setMaxLength(10)
        self.Driver_Phone_Number_Text.setObjectName("Driver_Phone_Number_Text")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Driver_Phone_Number_Text)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.Driver_License_Number = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.Driver_License_Number.setObjectName("Driver_License_Number")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Driver_License_Number)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.Driver_Car_Number = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.Driver_Car_Number.setObjectName("Driver_Car_Number")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.Driver_Car_Number)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.Driver_Car_Make_Text = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.Driver_Car_Make_Text.setObjectName("Driver_Car_Make_Text")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.Driver_Car_Make_Text)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.Driver_Car_Color = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.Driver_Car_Color.setObjectName("Driver_Car_Color")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.Driver_Car_Color)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 430, 491, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Driver_Submit_Button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Driver_Submit_Button.sizePolicy().hasHeightForWidth())
        self.Driver_Submit_Button.setSizePolicy(sizePolicy)
        self.Driver_Submit_Button.setObjectName("Driver_Submit_Button")
        self.verticalLayout_2.addWidget(self.Driver_Submit_Button)
        self.Driver_Invalid_Password = QtWidgets.QLabel(self.tab_2)
        self.Driver_Invalid_Password.setGeometry(QtCore.QRect(0, 0, 491, 21))
        self.Driver_Invalid_Password.setText("")
        self.Driver_Invalid_Password.setAlignment(QtCore.Qt.AlignCenter)
        self.Driver_Invalid_Password.setObjectName("Driver_Invalid_Password")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "First Name: "))
        self.label_2.setText(_translate("Form", "Last Name:"))
        self.label_3.setText(_translate("Form", "E-Mail:"))
        self.label_4.setText(_translate("Form", "Password:"))
        self.label_5.setText(_translate("Form", "Confirm Password:"))
        self.label_6.setText(_translate("Form", "Contact Number:"))
        self.label_7.setText(_translate("Form", "Payment:"))
        self.comboBox.setItemText(0, _translate("Form", "--Select Method--"))
        self.comboBox.setItemText(1, _translate("Form", "Card"))
        self.comboBox.setItemText(2, _translate("Form", "PayPal"))
        self.User_Submit_Button.setText(_translate("Form", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "User"))
        self.label_8.setText(_translate("Form", "First Name: "))
        self.label_9.setText(_translate("Form", "Last Name:"))
        self.label_10.setText(_translate("Form", "E-Mail:"))
        self.label_11.setText(_translate("Form", "Password:"))
        self.label_12.setText(_translate("Form", "Confirm Password: "))
        self.label_13.setText(_translate("Form", "Phone Number:"))
        self.label_14.setText(_translate("Form", "License Number:"))
        self.label_15.setText(_translate("Form", "License Expiry:"))
        self.dateEdit.setDisplayFormat(_translate("Form", "M/yyyy"))
        self.label_20.setText(_translate("Form", "Car Class : "))
        self.label_16.setText(_translate("Form", "Car License Number:"))
        self.label_17.setText(_translate("Form", "Car Make:"))
        self.label_18.setText(_translate("Form", "Car Colour:"))
        self.label_19.setText(_translate("Form", "Payment: "))
        self.comboBox_2.setItemText(0, _translate("Form", "--Select Method--"))
        self.comboBox_2.setItemText(1, _translate("Form", "Card"))
        self.comboBox_2.setItemText(2, _translate("Form", "Paypal"))
        self.comboBox_3.setItemText(0, _translate("Form", "Mini"))
        self.comboBox_3.setItemText(1, _translate("Form", "Micro"))
        self.comboBox_3.setItemText(2, _translate("Form", "Sedan"))
        self.comboBox_3.setItemText(3, _translate("Form", "Luxury"))
        self.comboBox_3.setItemText(4, _translate("Form", "XL"))
        self.comboBox_3.setItemText(5, _translate("Form", "XXL"))
        self.Driver_Submit_Button.setText(_translate("Form", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Driver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
