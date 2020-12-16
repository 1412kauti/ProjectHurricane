from PyQt5 import QtWidgets
from StartScreen import Ui_Form
import sys

class StartScreen(QtWidgets.QWidget):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.Login_Button.clicked.connect()
    def open_Login():
        print(0)

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = StartScreen()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()