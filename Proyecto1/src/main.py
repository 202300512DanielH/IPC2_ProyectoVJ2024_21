import sys
import os
from PyQt5 import QtWidgets
from tkinter import messagebox
from PyQt5.QtWidgets import QApplication, QMainWindow

# agregando la carpeta ventanas al path de python
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, 'ventanas'))

from login import Ui_Form #importando la clase Ui_Form de login.py en la carpeta ventanas
from ui_admin import Ui_MainWindow #importando la clase Ui_MainWindow de ui_admin.py en la carpeta ventanas

#clase principal de la aplicacion
class MainApp(QtWidgets.QWidget):
    
    #constructor de la clase
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.verificador.connect(self.ingresoApp) #conectando la señal verificador de la clase Ui_Form a la funcion ingresoApp

    #metodo para verificar el ingreso a la aplicacion 
    def ingresoApp(self, resultado):
        if resultado:
            print("Login Exitoso.")
            #cerrando la ventana de login, aca se abre la ventana del admin o del usuario segun sea el caso
            self.close()
            admin = Ui_MainWindow()
            admin.show()
        else:
            #mostrar ventana de error en caso de que los datos sean incorrectos
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())