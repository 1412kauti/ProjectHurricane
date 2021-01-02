    def take_driver_inputs(self):
        empty_str = ' '
        if self.ui3.Driver_First_Name_Text.text() == empty_str or self.containsDigits(self.ui3.Driver_First_Name_Text.text()) == True:
            driver_first_name = self.ui3.Driver_First_Name_Text.text()
            if self.ui3.Driver_Last_Name_Text.text() == empty_str or self.containsDigits(self.ui3.Driver_Last_Name_Text.text()) == True:
                driver_last_name = self.ui3.Driver_Last_Name_Text.text()
                if self.ui3.Driver_Email_Text.text() == empty_str and self.emailCheck(self.ui3.Driver_Email_Text.text()) == True:
                    driver_email = self.ui3.Driver_Email_Text.text()
                    if self.ui3.Driver_Password_Text.text() == empty_str:
                        driver_password = self.ui3.Driver_Password_Text.text()
                        if self.ui3.Driver_Phone_Number_Text.text() == empty_str:
                            driver_contact_number = self.ui3.Driver_Phone_Number_Text.text()
                            if self.ui3.Driver_License_Number.text() == empty_str:
                                driver_license = self.ui3.Driver_License_Number.text()
                                if self.ui3.Driver_Car_Number.text() == empty_str:
                                    driver_car_license = self.ui3.Driver_Car_Number.text()
                                    if self.ui3.Driver_Car_Make_Text.text() == empty_str:
                                        driver_car_make = self.ui3.Driver_Car_Make_Text.text()
                                        if self.ui3.Driver_Car_Color.text() == empty_str:
                                            driver_car_color = self.ui3.Driver_Car_Color.text()
                                            if self.ui3.comboBox_2.currentText() == empty_str:
                                                driver_payment = self.ui3.comboBox_2.currentText()
                                            else:
                                                self.ui3.User_Invalid_Password.setText("Payment method can't be empty")
                                        else:
                                            self.ui3.User_Invalid_Password.setText("Car color can't be empty")
                                    else:
                                        self.ui3.User_Invalid_Password.setText("Car make can't be empty")
                                else:
                                    self.ui3.User_Invalid_Password.setText("Car number can't be empty")
                            else:
                                self.ui3.User_Invalid_Password.setText("License number name can't be empty")                       
                        else:
                            self.ui3.User_Invalid_Password.setText("Phone number can't be empty")
                    else:
                        self.ui3.User_Invalid_Password.setText("Password can't be empty")
                else:
                    self.ui3.User_Invalid_Password.setText("Enter a proper email address")
            else:
                self.ui3.User_Invalid_Password.setText("Last name can't be empty or contain numbers")

        else:
            self.ui3.User_Invalid_Password.setText("First name can't be empty or contain numbers")