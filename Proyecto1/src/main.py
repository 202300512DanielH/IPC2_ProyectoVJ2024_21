import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from tkinter import messagebox

# Agregando la carpeta ventanas al path de python
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, 'ventanas'))

from login import Ui_Form as LoginForm  # Renombrando la clase Ui_Form a LoginForm
from ui_admin import Ui_MainWindow as AdminForm  # Renombrando la clase Ui_MainWindow a AdminForm
from usuarios import Ui_Form as UserForm  # Renombrando la clase Ui_Form a UserForm

# Clase principal de la aplicación
class MainApp(QtWidgets.QWidget):

    # Constructor de la clase
    def __init__(self):
        super().__init__()  # Llamando al constructor de la clase padre QWidget

        self.login_window = QWidget()  # Creando un objeto de la clase QWidget para el login
        self.ui_login = LoginForm()  # Creando un objeto de la clase LoginForm
        self.ui_login.setupUi(self.login_window)  # Inicializando la interfaz de usuario de login
        self.ui_login.verificador.connect(self.ingresoApp)  # Conectando la señal verificador de la clase LoginForm a la función ingresoApp

        self.user_window = QWidget()  # Creando un objeto de la clase QWidget para el usuario
        self.ui_user = UserForm(self.login_window, self.ui_login)  # Creando un objeto de la clase UserForm de usuarios.py
        self.ui_user.setupUi(self.user_window)  # Inicializando la interfaz de usuario de usuarios
        
        self.admin_window = QMainWindow()  # Creando un objeto de la clase QMainWindow de PyQt5
        self.ui_admin = AdminForm(self.login_window, self.ui_user)  # Creando un objeto de la clase AdminForm
        self.ui_admin.setupUi(self.admin_window)  # Inicializando la interfaz de usuario de ui_admin
        self.ui_admin.bt_minus.clicked.connect(lambda: self.ui_admin.minimizar(self.admin_window))  # Conectando el botón de minimizar a la función minimizar
        self.ui_admin.bt_exit.clicked.connect(lambda: self.ui_admin.salir(self.admin_window))  # Conectando el botón de salir a la función salir

    # Método para verificar el ingreso a la aplicación
    def ingresoApp(self, resultado):
        # Si el resultado es admin se muestra la ventana de administrador
        if resultado == "admin":
            print("Login Exitoso, como admin")
            # Mostrando la ventana del admin
            self.admin_window.show()  # Mostrando la ventana del admin
        # Si el resultado es user se muestra la ventana de usuario
        elif resultado == "usuario":
            print("Login Exitoso, como usuario")
            # Mostrando la ventana del usuario
            self.user_window.show()
        else:
            # Mostrar ventana de error en caso de que los datos sean incorrectos
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainApp()
    main_window.login_window.show()# Mostrando la ventana de login
    sys.exit(app.exec_())