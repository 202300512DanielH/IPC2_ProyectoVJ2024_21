from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication([])

login = uic.loadUi("C:\\Users\\danie.000\\Documents\\IPC2\\Proyecto\\Proyecto 1\\ventanas\\login.ui")

login.show()
sys.exit(app.exec_())

def gui_login():
    name = login.lineedit.text()
    password = login.lineedit_2.text()
    