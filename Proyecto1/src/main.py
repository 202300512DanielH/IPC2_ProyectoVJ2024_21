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
        super().__init__()#llamando al constructor de la clase padre QWidget
        self.ui = Ui_Form()#creando un objeto de la clase Ui_Form de login.py
        self.ui.setupUi(self)#inicializando la interfaz de usuario de login
        self.ui.verificador.connect(self.ingresoApp) #conectando la señal verificador de la clase Ui_Form a la funcion ingresoApp
        
        self.admin_window = QMainWindow()#creando un objeto de la clase QMainWindow de PyQt5
        self.ui_admin = Ui_MainWindow()#creando un objeto de la clase Ui_MainWindow de ui_admin.py
        self.ui_admin.setupUi(self.admin_window)#inicializando la interfaz de usuario de ui_admin
        self.ui_admin.bt_minus.clicked.connect(lambda: self.ui_admin.minimizar(self.admin_window))#conectando el boton de minimizar a la funcion minimizar
        self.ui_admin.bt_exit.clicked.connect(lambda: self.ui_admin.salir(self.admin_window))#conectando el boton de salir a la funcion salir
        self.ui_admin.verificador.connect(self.ingresoApp)#conectando la señal verificador de la clase Ui_MainWindow a la funcion ingresoApp

    #metodo para verificar el ingreso a la aplicacion 
    def ingresoApp(self, resultado, resultado2 = False):
        
        if resultado or resultado2:
            print("Login Exitoso.")
            #cerrando la ventana de login, aca se abre la ventana del admin o del usuario segun sea el caso
            self.hide()
            # Mostrando la ventana del admin 
            self.admin_window.show()#mostrando la ventana del admin
            
        else:
            #mostrar ventana de error en caso de que los datos sean incorrectos
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())