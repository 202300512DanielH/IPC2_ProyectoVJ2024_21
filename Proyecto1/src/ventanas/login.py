from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os


# Obteniendo la ruta del directorio actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Subiendo dos niveles en la jerarquia de directorios
ruta_proyecto = os.path.dirname(os.path.dirname(script_dir))

# Accediendo a la carpeta controller
ruta_controller = os.path.join(ruta_proyecto, 'controller')

# Asegurándose de que Python puede importar desde la carpeta controller
if ruta_controller not in sys.path:
    sys.path.append(ruta_controller)

from cargaMasivaUsuarios import cargaMasivaUsuarios

class Ui_Form(QtCore.QObject):  # poniendo QtCore.QObject como clase padre para poder usar señales
        
    verificador = QtCore.pyqtSignal(str)  # inicializando la señal verificador como una señal de tipo
    id_user = QtCore.pyqtSignal(str)  # inicializando la señal id_user como una señal de tipo str

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 565)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)#quitando los bordes de la ventana
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)#haciendo la ventana transparente
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.Form = Form
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.widget.setStyleSheet("QPushButton#button_login{\n"
" background-color: rgb(236, 253, 212);\n"
"    color: rgb(0,0,0); \n"
"    border: 2px solid rgb(199, 255, 193);\n"
"    border-bottom-width: 4px; \n"
"    border-bottom-color: rgb(150, 204, 144); \n"
"    border-radius: 15px; \n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton#button_login:hover{\n"
"  background-color: rgb(150, 204, 144); \n"
" border: 2px solid rgb(236, 253, 212);\n"
"    color: white; \n"
"}")
        self.widget.setObjectName("widget")
        self.fondo = QtWidgets.QLabel(self.widget)
        self.fondo.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.fondo.setStyleSheet("border-image:url(:/images/login.jpg);\n"
"border-top-left-radius: 50px;")
        self.fondo.setText("")
        self.fondo.setScaledContents(True)
        self.fondo.setObjectName("fondo")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-top-left-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 240, 430))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"    background-color: rgba(255, 255, 255, 1);\n"
"    border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 390, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/images/carretilla.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(110, 400, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255,255,255)\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(340, 60, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.user_name_label = QtWidgets.QLineEdit(self.widget)
        self.user_name_label.setGeometry(QtCore.QRect(295, 200, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.user_name_label.setFont(font)
        self.user_name_label.setStyleSheet("width: 100%;\n"
"    height: 150px;\n"
"    padding: 12px 20px;\n"
"    border: 2px solid rgb(253, 229, 212);\n"
"    border-bottom-width: 4px; \n"
"    border-bottom-color: rgb(255, 165, 0);\n"
"    border-radius: 15px;\n"
"    background-color: rgb(253, 236, 224);\n"
"    font-size: 16px;")
        self.user_name_label.setObjectName("user_name_label")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(370, 121, 42, 5))
        self.label_7.setStyleSheet("border-radius:10%;\n"
"background-color:rgb(255, 170, 0)")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.password_label = QtWidgets.QLineEdit(self.widget)
        self.password_label.setGeometry(QtCore.QRect(295, 270, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.password_label.setFont(font)
        self.password_label.setMouseTracking(True)
        self.password_label.setAcceptDrops(True)
        self.password_label.setStyleSheet("width: 100%;\n"
"    height: 150px;\n"
"    padding: 12px 20px;\n"
"    border: 2px solid rgb(253, 229, 212);\n"
"    border-bottom-width: 4px; \n"
"    border-bottom-color: rgb(255, 165, 0);\n"
"    border-radius: 15px;\n"
"    background-color: rgb(253, 236, 224);\n"
"    font-size: 16px;")
        self.password_label.setText("")
        self.password_label.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_label.setObjectName("password_label")
        self.button_login = QtWidgets.QPushButton(self.widget)
        self.button_login.setGeometry(QtCore.QRect(295, 380, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")

        self.fondo.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 255)))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 255)))
        self.button_login.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 255)))

        self.button_login.clicked.connect(lambda: self.login()) #conectando el boton con la funcion login 

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # funcion que valida el login
    def login(self):
        # Obtener los datos del usuario
        username = self.user_name_label.text()
        password = self.password_label.text()
        
        #recorriendo la lista de usuarios 
        usuario_encontrado = False
        #llamando a la lista de usuarios en la carga masiva
        self.carga_masiva_usuarios = cargaMasivaUsuarios()
        usuario = self.carga_masiva_usuarios.lista_usuarios.buscar(username)
        usuario_encontrado = False

        if usuario is not None and usuario.id == username and usuario.password == password:
            usuario_encontrado = True        

        # validacion del login, si los datos son correctos devuelve True y si no False
        if username == "1" and password == "1":
            self.verificador.emit("admin") #enviando la señal de que el login fue exitoso
            #limpiando los campos de texto
            self.user_name_label.setText("")
            self.password_label.setText("")
            #Cerrando la ventana 
            self.Form.close()
        elif usuario_encontrado:
            self.verificador.emit("usuario") #enviando la señal de que el login fue exitoso
            #enviando el id del usuario a la señal
            self.id_user.emit(username)
            #Limpiando los campos de texto
            self.user_name_label.setText("")
            self.password_label.setText("")
            #Cerrando la ventana
            self.Form.close()
        else:
            self.verificador.emit("error") #enviando la señal de que el login fue incorrecto
            #Limpiando los campos de texto
            self.user_name_label.setText("")
            self.password_label.setText("")
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "IPC2market"))
        self.label_6.setText(_translate("Form", "Log In"))
        self.user_name_label.setPlaceholderText(_translate("Form", "Nombre de Usuario"))
        self.password_label.setPlaceholderText(_translate("Form", "Contraseña"))
        self.button_login.setText(_translate("Form", "I n g r e s a r"))
