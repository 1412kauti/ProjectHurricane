# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_Driver_Password.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.changePasswordBtn = QtWidgets.QPushButton(Form)
        self.changePasswordBtn.setGeometry(QtCore.QRect(130, 200, 141, 23))
        self.changePasswordBtn.setObjectName("changePasswordBtn")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 90, 341, 75))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.change_Driver_Password_Label = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.change_Driver_Password_Label.setEchoMode(QtWidgets.QLineEdit.Password)
        self.change_Driver_Password_Label.setObjectName("change_Driver_Password_Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.change_Driver_Password_Label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.change_Driver_Confirm_Password_Label = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.change_Driver_Confirm_Password_Label.setEchoMode(QtWidgets.QLineEdit.Password)
        self.change_Driver_Confirm_Password_Label.setObjectName("change_Driver_Confirm_Password_Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.change_Driver_Confirm_Password_Label)
        self.Passwords_Mismatch = QtWidgets.QLabel(Form)
        self.Passwords_Mismatch.setGeometry(QtCore.QRect(30, 30, 341, 41))
        self.Passwords_Mismatch.setText("")
        self.Passwords_Mismatch.setAlignment(QtCore.Qt.AlignCenter)
        self.Passwords_Mismatch.setObjectName("Passwords_Mismatch")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.changePasswordBtn.setText(_translate("Form", "Change Password"))
        self.label.setText(_translate("Form", "New Password :"))
        self.label_2.setText(_translate("Form", "Confirm New Password :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())