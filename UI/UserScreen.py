# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        Form.setMinimumSize(QtCore.QSize(500, 500))
        Form.setMaximumSize(QtCore.QSize(500, 500))
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 501, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(120, 0, 291, 386))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 20, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(60)
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
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.timeEdit = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.timeEdit.setObjectName("timeEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.timeEdit)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 400, 175, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Select_Payment_Method_Btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Select_Payment_Method_Btn.sizePolicy().hasHeightForWidth())
        self.Select_Payment_Method_Btn.setSizePolicy(sizePolicy)
        self.Select_Payment_Method_Btn.setObjectName("Select_Payment_Method_Btn")
        self.verticalLayout.addWidget(self.Select_Payment_Method_Btn)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 491, 472))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 20, 0, 0)
        self.formLayout_2.setVerticalSpacing(35)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Upcoming_Start_Location_Lbl = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Upcoming_Start_Location_Lbl.setText("")
        self.Upcoming_Start_Location_Lbl.setObjectName("Upcoming_Start_Location_Lbl")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Upcoming_Start_Location_Lbl)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Upcoming_Destination_Lbl = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Upcoming_Destination_Lbl.setText("")
        self.Upcoming_Destination_Lbl.setObjectName("Upcoming_Destination_Lbl")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Upcoming_Destination_Lbl)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.Upcoming_Driver_Name_Lbl = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Upcoming_Driver_Name_Lbl.setText("")
        self.Upcoming_Driver_Name_Lbl.setObjectName("Upcoming_Driver_Name_Lbl")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Upcoming_Driver_Name_Lbl)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.Upcoming_Car_Make_Lbl = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Upcoming_Car_Make_Lbl.setText("")
        self.Upcoming_Car_Make_Lbl.setObjectName("Upcoming_Car_Make_Lbl")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Upcoming_Car_Make_Lbl)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.Upcoming_Car_Color_Lbl = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Upcoming_Car_Color_Lbl.setText("")
        self.Upcoming_Car_Color_Lbl.setObjectName("Upcoming_Car_Color_Lbl")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Upcoming_Car_Color_Lbl)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.Upcoming_Date_Lbl = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Upcoming_Date_Lbl.setText("")
        self.Upcoming_Date_Lbl.setObjectName("Upcoming_Date_Lbl")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Upcoming_Date_Lbl)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.Upcoming_Time_Lbl = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Upcoming_Time_Lbl.setText("")
        self.Upcoming_Time_Lbl.setObjectName("Upcoming_Time_Lbl")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Upcoming_Time_Lbl)
        self.Upcomin_Journey_ID_Lbl = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Upcomin_Journey_ID_Lbl.setText("")
        self.Upcomin_Journey_ID_Lbl.setObjectName("Upcomin_Journey_ID_Lbl")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Upcomin_Journey_ID_Lbl)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Upcoming_ETA = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Upcoming_ETA.setText("")
        self.Upcoming_ETA.setObjectName("Upcoming_ETA")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.Upcoming_ETA)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 491, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 3, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 2, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 3, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 5, 0, 1, 3)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 1, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 2, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 4, 1, 1, 2)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 6, 0, 1, 3)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(200, 250, 221, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab_5)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(60, 150, 361, 31))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_22 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.comboBox_4 = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Start Location : "))
        self.label_2.setText(_translate("Form", "Destination :"))
        self.label_3.setText(_translate("Form", "Car Type :"))
        self.label_4.setText(_translate("Form", "Date : "))
        self.label_5.setText(_translate("Form", "Time : "))
        self.Select_Payment_Method_Btn.setText(_translate("Form", "Select Payment Method"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "New Booking"))
        self.label_16.setText(_translate("Form", "Journey ID : "))
        self.label_6.setText(_translate("Form", "From :"))
        self.label_8.setText(_translate("Form", "To : "))
        self.label_10.setText(_translate("Form", "Driver Name : "))
        self.label_13.setText(_translate("Form", "Car Make : "))
        self.label_14.setText(_translate("Form", "Car Color : "))
        self.label_18.setText(_translate("Form", "Date : "))
        self.label_20.setText(_translate("Form", "Time : "))
        self.label_7.setText(_translate("Form", "ETA :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Upcoming Journeys"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Car Class"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Journey Cost"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Start Location"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "End Location"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Driver Name"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Vehicle Number"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Previous Journeys"))
        self.pushButton_5.setText(_translate("Form", "Change E-Mail"))
        self.label_23.setText(_translate("Form", "First Name : "))
        self.pushButton_6.setText(_translate("Form", "Change Phone Number"))
        self.pushButton_4.setText(_translate("Form", "Change Last Name"))
        self.label_29.setText(_translate("Form", "Phone Number :"))
        self.pushButton_8.setText(_translate("Form", "Change Card Details"))
        self.pushButton_3.setText(_translate("Form", "Change First Name"))
        self.label_25.setText(_translate("Form", "Last Name :"))
        self.label_27.setText(_translate("Form", "E-Mail : "))
        self.pushButton_7.setText(_translate("Form", "Change Password"))
        self.pushButton_9.setText(_translate("Form", "Change PayPal Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Profile"))
        self.pushButton_2.setText(_translate("Form", "Logout"))
        self.label_22.setText(_translate("Form", "Change Theme : "))
        self.comboBox_4.setItemText(0, _translate("Form", "Tiger"))
        self.comboBox_4.setItemText(1, _translate("Form", "Ubuntu"))
        self.comboBox_4.setItemText(2, _translate("Form", "NeonButtons"))
        self.comboBox_4.setItemText(3, _translate("Form", "Material Dark"))
        self.comboBox_4.setItemText(4, _translate("Form", "Manjaro Mix"))
        self.comboBox_4.setItemText(5, _translate("Form", "Elegant Dark"))
        self.comboBox_4.setItemText(6, _translate("Form", "Console Style"))
        self.comboBox_4.setItemText(7, _translate("Form", "Aqua"))
        self.comboBox_4.setItemText(8, _translate("Form", "AMOLED"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
