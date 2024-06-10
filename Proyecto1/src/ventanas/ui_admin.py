from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation
import sys, os, res
from PyQt5.QtWidgets import QFileDialog

# agregando la carpeta ventanas al path de python
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, 'ventanas'))

from login import Ui_Form #importando la clase Ui_Form de login.py en la carpeta ventanas

# subiendo dos niveles para acceder a la carpeta que contiene la carpeta controller
parent_dir = os.path.dirname(os.path.dirname(script_dir))

# Navega a la carpeta controller y agrega la ruta al path de python
sys.path.append(os.path.join(parent_dir, 'controller'))

from cargaMasivaEmpleados import cargaMasivaEmpleados
from cargaMasivaProducto import CargaMasivaProducto
from cargaMasivaUsuarios import cargaMasivaUsuarios

class Ui_MainWindow(QtCore.QObject):
    
    #constructor de la clase
    def __init__(self, ui_login):
        super().__init__()
        self.ui_login = ui_login
        
    def setupUi(self, MainWindow):
        self.bt_up_cargaMasivaUsuarios = QtWidgets.QPushButton(MainWindow)
        self.bt_up_cargaMasivaUsuarios.setObjectName("bt_up_cargaMasivaUsuarios")

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 752)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)#quitando los bordes de la ventana
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)#haciendo la ventana transparente
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1081, 751))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FrameSuperior = QtWidgets.QFrame(self.frame)
        self.FrameSuperior.setStyleSheet("background-color: rgb(253,229,212);\n"
"")
        self.FrameSuperior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameSuperior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameSuperior.setObjectName("FrameSuperior")
        self.bt_exit = QtWidgets.QPushButton(self.FrameSuperior)
        self.bt_exit.setGeometry(QtCore.QRect(970, 10, 71, 51))
        self.bt_exit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    border: 2px solid #dd9300; \n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#dd9300; \n"
"    border: 2px solid #dd9300; \n"
"}")
        self.bt_exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/bt_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_exit.setIcon(icon)
        self.bt_exit.setIconSize(QtCore.QSize(38, 38))
        self.bt_exit.setObjectName("bt_exit")
        self.bt_minus = QtWidgets.QPushButton(self.FrameSuperior)
        self.bt_minus.setGeometry(QtCore.QRect(890, 10, 71, 51))
        self.bt_minus.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    border: 2px solid #dd9300; \n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#dd9300; \n"
"    border: 2px solid #dd9300; \n"
"}")
        self.bt_minus.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/bt_minimizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_minus.setIcon(icon1)
        self.bt_minus.setIconSize(QtCore.QSize(38, 38))
        self.bt_minus.setObjectName("bt_minus")
        self.bt_option = QtWidgets.QPushButton(self.FrameSuperior)
        self.bt_option.setGeometry(QtCore.QRect(20, 10, 291, 61))
        self.bt_option.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    border: 2px solid #dd9300; \n"
"    color: white;\n"
"    font-weight: bold;\n"
"    min-width: 135px;\n"
"    min-height: 0px;\n"
"    padding: 0px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#dd9300; \n"
"    border: 2px solid #dd9300; \n"
"}")
        self.bt_option.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/bt_opciones.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_option.setIcon(icon3)
        self.bt_option.setIconSize(QtCore.QSize(38, 38))
        self.bt_option.setObjectName("bt_option")
        self.verticalLayout.addWidget(self.FrameSuperior)
        self.FrameInferior = QtWidgets.QFrame(self.frame)
        self.FrameInferior.setStyleSheet("QFrame {\n"
"    border: 3px solid orange;\n"
"}\n"
"")
        self.FrameInferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameInferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameInferior.setObjectName("FrameInferior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.FrameInferior)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frameBotones = QtWidgets.QFrame(self.FrameInferior)
        self.frameBotones.setMinimumSize(QtCore.QSize(300, 0))
        self.frameBotones.setMaximumSize(QtCore.QSize(0, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.frameBotones.setFont(font)
        self.frameBotones.setStyleSheet("/* Estilo para el QFrame */\n"
"QFrame {\n"
"    border: 2px solid #FFA500; /* Naranja */\n"
"    background-color: rgb(253,229,212);\n"
"    padding: 10px;\n"
"}\n"
"\n"
"/* Estilo para los QLineEdit */\n"
"QLineEdit {\n"
"    border: 2px solid #FFA500; /* Naranja */\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: #FFEBCC; /* Color crema claro */\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"    margin-bottom: 10px; /* Espacio entre los campos de entrada */\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    border: 2px solid #dd9300; /* Verde oscuro */\n"
"    color: rgb(221, 147, 0);\n"
"    color: rgb(200, 133, 0);\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    min-width: 135px;\n"
"    min-height: 50px;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#dd9300; /* Verde más claro */\n"
"    border: 2px solid #dd9300; /* Verde oscuro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #689F38; /* Verde oscuro */\n"
"    border: 2px solid #33691E; /* Verde más oscuro */\n"
"}\n"
"\n"
"\n"
"/* Estilo para el QLabel (título) */\n"
"QLabel#title {\n"
"    color: #333333;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Estilo para el QLabel (subtítulo) */\n"
"QLabel#subtitle {\n"
"    color: #FFA500;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.frameBotones.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBotones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBotones.setObjectName("frameBotones")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameBotones)
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bt_menu_cargar = QtWidgets.QPushButton(self.frameBotones)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/bt_upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu_cargar.setIcon(icon4)
        self.bt_menu_cargar.setIconSize(QtCore.QSize(38, 38))
        self.bt_menu_cargar.setObjectName("bt_menu_cargar")
        self.verticalLayout_2.addWidget(self.bt_menu_cargar)
        self.bt_menu_reportes = QtWidgets.QPushButton(self.frameBotones)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/bt_reports.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu_reportes.setIcon(icon5)
        self.bt_menu_reportes.setIconSize(QtCore.QSize(38, 38))
        self.bt_menu_reportes.setObjectName("bt_menu_reportes")
        self.verticalLayout_2.addWidget(self.bt_menu_reportes)
        self.bt_menu_actividades = QtWidgets.QPushButton(self.frameBotones)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/bt_activities.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu_actividades.setIcon(icon6)
        self.bt_menu_actividades.setIconSize(QtCore.QSize(38, 38))
        self.bt_menu_actividades.setObjectName("bt_menu_actividades")
        self.verticalLayout_2.addWidget(self.bt_menu_actividades)
        self.bt_menu_compras = QtWidgets.QPushButton(self.frameBotones)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/bt_shop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu_compras.setIcon(icon7)
        self.bt_menu_compras.setIconSize(QtCore.QSize(38, 38))
        self.bt_menu_compras.setObjectName("bt_menu_compras")
        self.verticalLayout_2.addWidget(self.bt_menu_compras)
        self.horizontalLayout.addWidget(self.frameBotones)
        self.frame_3 = QtWidgets.QFrame(self.FrameInferior)
        self.frame_3.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_3)
        self.stackedWidget.setMinimumSize(QtCore.QSize(694, 584))
        self.stackedWidget.setMaximumSize(QtCore.QSize(694, 584))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Inicial = QtWidgets.QWidget()
        self.Inicial.setObjectName("Inicial")
        self.go_login_inicio = QtWidgets.QPushButton(self.Inicial)
        self.go_login_inicio.setGeometry(QtCore.QRect(420, 20, 265, 51))
        self.go_login_inicio.setStyleSheet("QPushButton {\n"
"    background-color: #ff7676;\n"
"    border: 2px solid #e00000; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#c20000; \n"
"    border: 2px solid #c20000; \n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/bt_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_login_inicio.setIcon(icon8)
        self.go_login_inicio.setIconSize(QtCore.QSize(30, 30))
        self.go_login_inicio.setObjectName("go_login_inicio")
        self.pushButton_6 = QtWidgets.QPushButton(self.Inicial)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 120, 391, 331))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: #f0c348;\n"
"    border: 2px solid #f0c348; \n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    min-width: 135px;\n"
"    min-height: 50px;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"")
        self.pushButton_6.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/img_admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon9)
        self.pushButton_6.setIconSize(QtCore.QSize(250, 250))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.Inicial)
        self.label.setGeometry(QtCore.QRect(20, 470, 621, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.Inicial)
        self.Carga = QtWidgets.QWidget()
        self.Carga.setObjectName("Carga")
        self.bt_cargar_productos = QtWidgets.QPushButton(self.Carga)
        self.bt_cargar_productos.setGeometry(QtCore.QRect(370, 100, 311, 201))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.bt_cargar_productos.setFont(font)
        self.bt_cargar_productos.setStyleSheet("QPushButton {\n"
"    background-color: #8cebdb;\n"
"    border: 2px solid #25D9B9; \n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    min-width: 135px;\n"
"    min-height: 50px;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#25D9B9;\n"
"    border: 2px solid #25D9B9; \n"
"}\n"
"\n"
"")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/up_products.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cargar_productos.setIcon(icon10)
        self.bt_cargar_productos.setIconSize(QtCore.QSize(150, 145))
        self.bt_cargar_productos.setObjectName("bt_cargar_productos")
        self.bt_cargar_usuarios = QtWidgets.QPushButton(self.Carga)
        self.bt_cargar_usuarios.setGeometry(QtCore.QRect(0, 100, 311, 201))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.bt_cargar_usuarios.setFont(font)
        self.bt_cargar_usuarios.setStyleSheet("QPushButton {\n"
"    background-color: #c0f5a2;\n"
"    border: 2px solid #9ee67a; \n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    min-width: 135px;\n"
"    min-height: 50px;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#9ee67a;\n"
"    border: 2px solid #9ee67a; \n"
"}\n"
"\n"
"\n"
"")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/up_users.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cargar_usuarios.setIcon(icon11)
        self.bt_cargar_usuarios.setIconSize(QtCore.QSize(150, 150))
        self.bt_cargar_usuarios.setObjectName("bt_cargar_usuarios")
        self.bt_cargar_empleados = QtWidgets.QPushButton(self.Carga)
        self.bt_cargar_empleados.setGeometry(QtCore.QRect(10, 360, 311, 201))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.bt_cargar_empleados.setFont(font)
        self.bt_cargar_empleados.setStyleSheet("QPushButton {\n"
"    background-color: #9ee1ff;\n"
"    border: 2px solid #66c6f2; \n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    min-width: 135px;\n"
"    min-height: 50px;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#66c6f2;\n"
"    border: 2px solid #66c6f2; \n"
"}\n"
"")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/up_employee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cargar_empleados.setIcon(icon12)
        self.bt_cargar_empleados.setIconSize(QtCore.QSize(150, 150))
        self.bt_cargar_empleados.setObjectName("bt_cargar_empleados")
        self.bt_cargar_actividades = QtWidgets.QPushButton(self.Carga)
        self.bt_cargar_actividades.setGeometry(QtCore.QRect(370, 360, 311, 201))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.bt_cargar_actividades.setFont(font)
        self.bt_cargar_actividades.setStyleSheet("QPushButton {\n"
"    background-color: #c4c2ff;\n"
"    border: 2px solid #7f7ce6; \n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    min-width: 135px;\n"
"    min-height: 50px;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#7f7ce6;\n"
"    border: 2px solid #7f7ce6; \n"
"}\n"
"")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/up_activities.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cargar_actividades.setIcon(icon13)
        self.bt_cargar_actividades.setIconSize(QtCore.QSize(150, 150))
        self.bt_cargar_actividades.setObjectName("bt_cargar_actividades")
        self.go_login_cargar = QtWidgets.QPushButton(self.Carga)
        self.go_login_cargar.setGeometry(QtCore.QRect(420, 20, 265, 51))
        self.go_login_cargar.setStyleSheet("QPushButton {\n"
"    background-color: #ff7676;\n"
"    border: 2px solid #e00000; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#c20000; \n"
"    border: 2px solid #c20000; \n"
"}")
        self.go_login_cargar.setIcon(icon8)
        self.go_login_cargar.setIconSize(QtCore.QSize(30, 30))
        self.go_login_cargar.setObjectName("go_login_cargar")
        self.stackedWidget.addWidget(self.Carga)
        self.Reporte = QtWidgets.QWidget()
        self.Reporte.setObjectName("Reporte")
        self.label_2 = QtWidgets.QLabel(self.Reporte)
        self.label_2.setGeometry(QtCore.QRect(70, 0, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.bt_reporte_usuarios = QtWidgets.QPushButton(self.Reporte)
        self.bt_reporte_usuarios.setGeometry(QtCore.QRect(0, 150, 331, 71))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bt_reporte_usuarios.setFont(font)
        self.bt_reporte_usuarios.setStyleSheet("QPushButton {\n"
"    background-color: #ffcea3;\n"
"    border: 2px solid #Faa255; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#Faa255;\n"
"    border: 2px solid #Faa255; \n"
"}\n"
"\n"
"\n"
"")
        self.bt_reporte_usuarios.setIcon(icon12)
        self.bt_reporte_usuarios.setIconSize(QtCore.QSize(50, 100))
        self.bt_reporte_usuarios.setObjectName("bt_reporte_usuarios")
        self.go_login_reportes = QtWidgets.QPushButton(self.Reporte)
        self.go_login_reportes.setGeometry(QtCore.QRect(420, 20, 265, 51))
        self.go_login_reportes.setStyleSheet("QPushButton {\n"
"    background-color: #ff7676;\n"
"    border: 2px solid #e00000; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#c20000; \n"
"    border: 2px solid #c20000; \n"
"}")
        self.go_login_reportes.setIcon(icon8)
        self.go_login_reportes.setIconSize(QtCore.QSize(30, 30))
        self.go_login_reportes.setObjectName("go_login_reportes")
        self.bt_reporte_productos = QtWidgets.QPushButton(self.Reporte)
        self.bt_reporte_productos.setGeometry(QtCore.QRect(-10, 270, 331, 71))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bt_reporte_productos.setFont(font)
        self.bt_reporte_productos.setStyleSheet("QPushButton {\n"
"    background-color: #FBE692;\n"
"    border: 2px solid #F0C348; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#F0C348;\n"
"    border: 2px solid #F0C348; \n"
"}\n"
"\n"
"\n"
"")
        self.bt_reporte_productos.setIcon(icon10)
        self.bt_reporte_productos.setIconSize(QtCore.QSize(50, 100))
        self.bt_reporte_productos.setObjectName("bt_reporte_productos")
        self.bt_reportes_COLA = QtWidgets.QPushButton(self.Reporte)
        self.bt_reportes_COLA.setGeometry(QtCore.QRect(0, 390, 331, 71))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bt_reportes_COLA.setFont(font)
        self.bt_reportes_COLA.setStyleSheet("QPushButton {\n"
"    background-color: #ecb4f5;\n"
"    border: 2px solid #e27cf1; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#e27cf1;\n"
"    border: 2px solid #e27cf1; \n"
"}\n"
"\n"
"\n"
"")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("rp_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_reportes_COLA.setIcon(icon14)
        self.bt_reportes_COLA.setIconSize(QtCore.QSize(50, 100))
        self.bt_reportes_COLA.setObjectName("bt_reportes_COLA")
        self.bt_reporte_compras = QtWidgets.QPushButton(self.Reporte)
        self.bt_reporte_compras.setGeometry(QtCore.QRect(360, 150, 331, 71))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bt_reporte_compras.setFont(font)
        self.bt_reporte_compras.setStyleSheet("QPushButton {\n"
"    background-color: #FAB4D7;\n"
"    border: 2px solid #f562AC; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#f562AC;\n"
"    border: 2px solid #f562AC; \n"
"}\n"
"\n"
"\n"
"")
        self.bt_reporte_compras.setIcon(icon7)
        self.bt_reporte_compras.setIconSize(QtCore.QSize(50, 100))
        self.bt_reporte_compras.setObjectName("bt_reporte_compras")
        self.bt_reporte_vendedores = QtWidgets.QPushButton(self.Reporte)
        self.bt_reporte_vendedores.setGeometry(QtCore.QRect(360, 270, 331, 71))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bt_reporte_vendedores.setFont(font)
        self.bt_reporte_vendedores.setStyleSheet("QPushButton {\n"
"    background-color: #feb1b1;\n"
"    border: 2px solid #EB5959; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#EB5959;\n"
"    border: 2px solid #EB5959; \n"
"}\n"
"\n"
"\n"
"")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/img_admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_reporte_vendedores.setIcon(icon15)
        self.bt_reporte_vendedores.setIconSize(QtCore.QSize(50, 100))
        self.bt_reporte_vendedores.setObjectName("bt_reporte_vendedores")
        self.bt_reporte_actividades = QtWidgets.QPushButton(self.Reporte)
        self.bt_reporte_actividades.setGeometry(QtCore.QRect(360, 390, 331, 71))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bt_reporte_actividades.setFont(font)
        self.bt_reporte_actividades.setStyleSheet("QPushButton {\n"
"    background-color: #78EBA8;\n"
"    border: 2px solid #50D989; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#50D989;\n"
"    border: 2px solid #50D989; \n"
"}\n"
"\n"
"\n"
"")
        self.bt_reporte_actividades.setIcon(icon13)
        self.bt_reporte_actividades.setIconSize(QtCore.QSize(50, 100))
        self.bt_reporte_actividades.setObjectName("bt_reporte_actividades")
        self.stackedWidget.addWidget(self.Reporte)
        self.Actividades = QtWidgets.QWidget()
        self.Actividades.setObjectName("Actividades")
        self.label_3 = QtWidgets.QLabel(self.Actividades)
        self.label_3.setGeometry(QtCore.QRect(40, 0, 371, 121))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.area_actividades_panel = QtWidgets.QScrollArea(self.Actividades)
        self.area_actividades_panel.setGeometry(QtCore.QRect(40, 120, 621, 431))
        self.area_actividades_panel.setStyleSheet("border-color: rgb(255, 170, 0);")
        self.area_actividades_panel.setWidgetResizable(True)
        self.area_actividades_panel.setObjectName("area_actividades_panel")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 615, 425))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalLayout_4.addWidget(self.verticalScrollBar)
        self.area_actividades_panel.setWidget(self.scrollAreaWidgetContents)
        self.go_login_actividades = QtWidgets.QPushButton(self.Actividades)
        self.go_login_actividades.setGeometry(QtCore.QRect(420, 20, 265, 51))
        self.go_login_actividades.setStyleSheet("QPushButton {\n"
"    background-color: #ff7676;\n"
"    border: 2px solid #e00000; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#c20000; \n"
"    border: 2px solid #c20000; \n"
"}")
        self.go_login_actividades.setIcon(icon8)
        self.go_login_actividades.setIconSize(QtCore.QSize(30, 30))
        self.go_login_actividades.setObjectName("go_login_actividades")
        self.stackedWidget.addWidget(self.Actividades)
        self.Compras = QtWidgets.QWidget()
        self.Compras.setObjectName("Compras")
        self.label_4 = QtWidgets.QLabel(self.Compras)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 371, 121))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.area_compras_panel = QtWidgets.QWidget(self.Compras)
        self.area_compras_panel.setGeometry(QtCore.QRect(20, 140, 451, 381))
        self.area_compras_panel.setStyleSheet("QWidget {\n"
"    border: 2px solid #FFA500; /* Naranja */\n"
"    background-color: rgb(253,229,212);\n"
"    padding: 10px;\n"
"}")
        self.area_compras_panel.setObjectName("area_compras_panel")
        self.go_login_compras = QtWidgets.QPushButton(self.Compras)
        self.go_login_compras.setGeometry(QtCore.QRect(420, 20, 265, 51))
        self.go_login_compras.setStyleSheet("QPushButton {\n"
"    background-color: #ff7676;\n"
"    border: 2px solid #e00000; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#c20000; \n"
"    border: 2px solid #c20000; \n"
"}")
        self.go_login_compras.setIcon(icon8)
        self.go_login_compras.setIconSize(QtCore.QSize(30, 30))
        self.go_login_compras.setObjectName("go_login_compras")
        self.bt_compras_ok = QtWidgets.QPushButton(self.Compras)
        self.bt_compras_ok.setGeometry(QtCore.QRect(494, 260, 191, 51))
        self.bt_compras_ok.setStyleSheet("QPushButton {\n"
"    background-color: #C0F5A2;\n"
"    border: 2px solid #9EE67A; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#9EE67A; \n"
"    border: 2px solid #9EE67A; \n"
"}")
        self.bt_compras_ok.setIconSize(QtCore.QSize(30, 30))
        self.bt_compras_ok.setObjectName("bt_compras_ok")
        self.bt_compras_no = QtWidgets.QPushButton(self.Compras)
        self.bt_compras_no.setGeometry(QtCore.QRect(500, 340, 191, 51))
        self.bt_compras_no.setStyleSheet("QPushButton {\n"
"    background-color: #ff7676;\n"
"    border: 2px solid #e00000; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#c20000; \n"
"    border: 2px solid #c20000; \n"
"}")
        self.bt_compras_no.setIconSize(QtCore.QSize(30, 30))
        self.bt_compras_no.setObjectName("bt_compras_no")
        self.stackedWidget.addWidget(self.Compras)
        self.CargaMasivaUsuarios = QtWidgets.QWidget()
        self.CargaMasivaUsuarios.setObjectName("CargaMasivaUsuarios")
        self.label_5 = QtWidgets.QLabel(self.CargaMasivaUsuarios)
        self.label_5.setGeometry(QtCore.QRect(160, 90, 351, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.go_login_CM_usuarios = QtWidgets.QPushButton(self.CargaMasivaUsuarios)
        self.go_login_CM_usuarios.setGeometry(QtCore.QRect(420, 20, 265, 51))
        self.go_login_CM_usuarios.setStyleSheet("QPushButton {\n"
"    background-color: #ff7676;\n"
"    border: 2px solid #e00000; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#c20000; \n"
"    border: 2px solid #c20000; \n"
"}")
        self.go_login_CM_usuarios.setIcon(icon8)
        self.go_login_CM_usuarios.setIconSize(QtCore.QSize(30, 30))
        self.go_login_CM_usuarios.setObjectName("go_login_CM_usuarios")
        self.bt_up_cargaMasivaUsuarios = QtWidgets.QPushButton(self.CargaMasivaUsuarios)
        self.bt_up_cargaMasivaUsuarios.setGeometry(QtCore.QRect(200, 240, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.bt_up_cargaMasivaUsuarios.setFont(font)
        self.bt_up_cargaMasivaUsuarios.setStyleSheet("QPushButton {\n"
"    background-color: #C0F5A2;\n"
"    border: 2px solid #9EE67A; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#9EE67A; \n"
"    border: 2px solid #9EE67A; \n"
"}")
        self.bt_up_cargaMasivaUsuarios.setIcon(icon4)
        self.bt_up_cargaMasivaUsuarios.setIconSize(QtCore.QSize(100, 100))
        self.bt_up_cargaMasivaUsuarios.setObjectName("bt_up_cargaMasivaUsuarios")
        self.stackedWidget.addWidget(self.CargaMasivaUsuarios)
        self.cargaMasivaProductos = QtWidgets.QWidget()
        self.cargaMasivaProductos.setObjectName("cargaMasivaProductos")
        self.go_login_CM_productos = QtWidgets.QPushButton(self.cargaMasivaProductos)
        self.go_login_CM_productos.setGeometry(QtCore.QRect(420, 20, 265, 51))
        self.go_login_CM_productos.setStyleSheet("QPushButton {\n"
"    background-color: #ff7676;\n"
"    border: 2px solid #e00000; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#c20000; \n"
"    border: 2px solid #c20000; \n"
"}")
        self.go_login_CM_productos.setIcon(icon8)
        self.go_login_CM_productos.setIconSize(QtCore.QSize(30, 30))
        self.go_login_CM_productos.setObjectName("go_login_CM_productos")
        self.bt_up_cargaMasivaProductos = QtWidgets.QPushButton(self.cargaMasivaProductos)
        self.bt_up_cargaMasivaProductos.setGeometry(QtCore.QRect(200, 240, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.bt_up_cargaMasivaProductos.setFont(font)
        self.bt_up_cargaMasivaProductos.setStyleSheet("QPushButton {\n"
"    background-color: #C0F5A2;\n"
"    border: 2px solid #9EE67A; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#9EE67A; \n"
"    border: 2px solid #9EE67A; \n"
"}")
        self.bt_up_cargaMasivaProductos.setIcon(icon4)
        self.bt_up_cargaMasivaProductos.setIconSize(QtCore.QSize(100, 100))
        self.bt_up_cargaMasivaProductos.setObjectName("bt_up_cargaMasivaProductos")
        self.label_6 = QtWidgets.QLabel(self.cargaMasivaProductos)
        self.label_6.setGeometry(QtCore.QRect(160, 90, 371, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.cargaMasivaProductos)
        self.cargaMasivaEmpleados = QtWidgets.QWidget()
        self.cargaMasivaEmpleados.setObjectName("cargaMasivaEmpleados")
        self.label_7 = QtWidgets.QLabel(self.cargaMasivaEmpleados)
        self.label_7.setGeometry(QtCore.QRect(160, 90, 391, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.go_login_CM_empleados = QtWidgets.QPushButton(self.cargaMasivaEmpleados)
        self.go_login_CM_empleados.setGeometry(QtCore.QRect(420, 20, 265, 51))
        self.go_login_CM_empleados.setStyleSheet("QPushButton {\n"
"    background-color: #ff7676;\n"
"    border: 2px solid #e00000; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#c20000; \n"
"    border: 2px solid #c20000; \n"
"}")
        self.go_login_CM_empleados.setIcon(icon8)
        self.go_login_CM_empleados.setIconSize(QtCore.QSize(30, 30))
        self.go_login_CM_empleados.setObjectName("go_login_CM_empleados")
        self.bt_up_cargaMasivaEmpleados = QtWidgets.QPushButton(self.cargaMasivaEmpleados)
        self.bt_up_cargaMasivaEmpleados.setGeometry(QtCore.QRect(200, 240, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.bt_up_cargaMasivaEmpleados.setFont(font)
        self.bt_up_cargaMasivaEmpleados.setStyleSheet("QPushButton {\n"
"    background-color: #C0F5A2;\n"
"    border: 2px solid #9EE67A; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#9EE67A; \n"
"    border: 2px solid #9EE67A; \n"
"}")
        self.bt_up_cargaMasivaEmpleados.setIcon(icon4)
        self.bt_up_cargaMasivaEmpleados.setIconSize(QtCore.QSize(100, 100))
        self.bt_up_cargaMasivaEmpleados.setObjectName("bt_up_cargaMasivaEmpleados")
        self.stackedWidget.addWidget(self.cargaMasivaEmpleados)
        self.cargaMasivaActividades = QtWidgets.QWidget()
        self.cargaMasivaActividades.setObjectName("cargaMasivaActividades")
        self.panel_CM_Actividades = QtWidgets.QWidget(self.cargaMasivaActividades)
        self.panel_CM_Actividades.setGeometry(QtCore.QRect(20, 300, 631, 251))
        self.panel_CM_Actividades.setStyleSheet("QWidget {\n"
"    border: 2px solid #FFA500; /* Naranja */\n"
"    background-color: rgb(253,229,212);\n"
"    padding: 10px;\n"
"}")
        self.panel_CM_Actividades.setObjectName("panel_CM_Actividades")
        self.bt_up_cargaMasivaActividades = QtWidgets.QPushButton(self.cargaMasivaActividades)
        self.bt_up_cargaMasivaActividades.setGeometry(QtCore.QRect(80, 130, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.bt_up_cargaMasivaActividades.setFont(font)
        self.bt_up_cargaMasivaActividades.setStyleSheet("QPushButton {\n"
"    background-color: #C0F5A2;\n"
"    border: 2px solid #9EE67A; \n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#9EE67A; \n"
"    border: 2px solid #9EE67A; \n"
"}")
        self.bt_up_cargaMasivaActividades.setIcon(icon4)
        self.bt_up_cargaMasivaActividades.setIconSize(QtCore.QSize(100, 100))
        self.bt_up_cargaMasivaActividades.setObjectName("bt_up_cargaMasivaActividades")
        self.label_8 = QtWidgets.QLabel(self.cargaMasivaActividades)
        self.label_8.setGeometry(QtCore.QRect(0, -20, 411, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.go_login_CM_Actividades = QtWidgets.QPushButton(self.cargaMasivaActividades)
        self.go_login_CM_Actividades.setGeometry(QtCore.QRect(420, 20, 265, 51))
        self.go_login_CM_Actividades.setStyleSheet("QPushButton {\n"
"    background-color: #ff7676;\n"
"    border: 2px solid #e00000; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#c20000; \n"
"    border: 2px solid #c20000; \n"
"}")
        self.go_login_CM_Actividades.setIcon(icon8)
        self.go_login_CM_Actividades.setIconSize(QtCore.QSize(30, 30))
        self.go_login_CM_Actividades.setObjectName("go_login_CM_Actividades")
        self.stackedWidget.addWidget(self.cargaMasivaActividades)
        self.showReport = QtWidgets.QWidget()
        self.showReport.setObjectName("showReport")
        self.label_9 = QtWidgets.QLabel(self.showReport)
        self.label_9.setGeometry(QtCore.QRect(0, -20, 411, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.panel_imagen_reporteCreado = QtWidgets.QWidget(self.showReport)
        self.panel_imagen_reporteCreado.setGeometry(QtCore.QRect(10, 120, 681, 451))
        self.panel_imagen_reporteCreado.setStyleSheet("QWidget {\n"
"    border: 2px solid #FFA500; /* Naranja */\n"
"    background-color: rgb(253,229,212);\n"
"    padding: 10px;\n"
"}")
        self.panel_imagen_reporteCreado.setObjectName("panel_imagen_reporteCreado")
        self.go_login_CM_Actividades_2 = QtWidgets.QPushButton(self.showReport)
        self.go_login_CM_Actividades_2.setGeometry(QtCore.QRect(420, 20, 265, 51))
        self.go_login_CM_Actividades_2.setStyleSheet("QPushButton {\n"
"    background-color: #ff7676;\n"
"    border: 2px solid #e00000; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#c20000; \n"
"    border: 2px solid #c20000; \n"
"}")
        self.go_login_CM_Actividades_2.setIcon(icon8)
        self.go_login_CM_Actividades_2.setIconSize(QtCore.QSize(30, 30))
        self.go_login_CM_Actividades_2.setObjectName("go_login_CM_Actividades_2")
        self.stackedWidget.addWidget(self.showReport)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.FrameInferior)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        # Agregando sombras a los botones de la barra de navegación
        self.bt_option.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=10, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 255)))
        self.bt_minus.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=10, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 255)))
        self.bt_exit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=10, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 255)))
        
        # Haciendo que por defecto se muestre la pantalla de inicio 
        self.stackedWidget.setCurrentIndex(0)
        
        # Conexiones de los botones de la barra de navegación 
        self.bt_menu_cargar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.bt_menu_reportes.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.bt_menu_actividades.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.bt_menu_compras.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        
        # Conexiones de los botones de la pestaña Cargar 
        self.bt_cargar_usuarios.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.bt_cargar_productos.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.bt_cargar_empleados.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        self.bt_cargar_actividades.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))
        
        # Conexiones de los botones de la pestaña Reportes
        self.bt_reporte_usuarios.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.bt_reporte_productos.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.bt_reportes_COLA.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.bt_reporte_compras.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.bt_reporte_vendedores.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.bt_reporte_actividades.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))

        # Conexiones de los botones de la barra de navegación
        self.bt_option.clicked.connect(self.mover_menu)
        self.bt_minus.clicked.connect(lambda: self.minimizar(MainWindow))
        self.bt_exit.clicked.connect(lambda: self.salir(MainWindow))    
        
        # Conexion del boton para regresar a la ventana del login 
        self.go_login_inicio.clicked.connect(lambda: self.show_login(MainWindow))
        self.go_login_cargar.clicked.connect(lambda: self.show_login(MainWindow))
        self.go_login_reportes.clicked.connect(lambda: self.show_login(MainWindow))
        self.go_login_actividades.clicked.connect(lambda: self.show_login(MainWindow))
        self.go_login_compras.clicked.connect(lambda: self.show_login(MainWindow))
        self.go_login_CM_usuarios.clicked.connect(lambda: self.show_login(MainWindow))
        self.go_login_CM_productos.clicked.connect(lambda: self.show_login(MainWindow))
        self.go_login_CM_empleados.clicked.connect(lambda: self.show_login(MainWindow))
        self.go_login_CM_Actividades.clicked.connect(lambda: self.show_login(MainWindow))
        self.go_login_CM_Actividades_2.clicked.connect(lambda: self.show_login(MainWindow))
        
        #Conexión de botones para cargar un archivo XML
        self.bt_up_cargaMasivaUsuarios.clicked.connect(lambda: self.open_xml_file("Usuarios"))
        self.bt_up_cargaMasivaEmpleados.clicked.connect(lambda: self.open_xml_file("Empleados"))
        self.bt_up_cargaMasivaProductos.clicked.connect(lambda: self.open_xml_file("Productos"))
        self.bt_up_cargaMasivaActividades.clicked.connect(lambda: self.open_xml_file("Actividades"))
        
        #Conectando los botones para los reportes 
        self.bt_reporte_usuarios.clicked.connect(lambda: self.mostrar_reporte("Usuarios"))
        self.bt_reporte_productos.clicked.connect(lambda: self.mostrar_reporte("Productos"))
        self.bt_reporte_actividades.clicked.connect(lambda: self.mostrar_reporte("Actividades"))
        self.bt_reporte_compras.clicked.connect(lambda: self.mostrar_reporte("Compras"))
        self.bt_reporte_vendedores.clicked.connect(lambda: self.mostrar_reporte("Vendedores"))
        self.bt_reportes_COLA.clicked.connect(lambda: self.mostrar_reporte("Cola"))
        
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def mostrar_reporte(self, tipo_reporte):
        if tipo_reporte == "Usuarios":
                print("Mostrando reporte de usuarios.")
                self.carga_masiva_usuarios = cargaMasivaUsuarios()
                self.carga_masiva_usuarios.lista_usuarios.graficar()
        elif tipo_reporte == "Productos":
                print("Mostrando reporte de productos.")
                self.carga_masiva_producto = CargaMasivaProducto()
                self.carga_masiva_producto.lista_productos.graficar()
        elif tipo_reporte == "Actividades":
                print("Mostrando reporte de actividades.")
        elif tipo_reporte == "Compras":
                print("Mostrando reporte de compras.")
        elif tipo_reporte == "Vendedores":
                print("Mostrando reporte de vendedores.")
                self.carga_masiva_empleados = cargaMasivaEmpleados()
                self.carga_masiva_empleados.lista_empleados.graficar()
        elif tipo_reporte == "Cola":
                print("Mostrando reporte de cola.")
        else:
                print("No se ha seleccionado un tipo de reporte válido.")

    def minimizar(self, MainWindow):
        MainWindow.showMinimized()

    def salir(self, MainWindow):
        MainWindow.close()

    def show_login(self, MainWindow):
        # Cerrando la ventana del administrador
        MainWindow.hide()
        #Regresando a la ventana de login
        self.ui_login.show()
    
    def mover_menu(self):
        if True: 
                width = self.frameBotones.width()
                normal = 0 
                if width == 0: 
                        extender = 300
                else: 
                        extender = normal
                self.animacion  = QPropertyAnimation(self.frameBotones, b"minimumWidth")
                self.animacion.setDuration(300)
                self.animacion.setStartValue(width)
                self.animacion.setEndValue(extender)
                self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animacion.start()

    def open_xml_file(self, tipo_archivo):
        print("Función open_xml_file llamada.")
        file_name, _ = QFileDialog.getOpenFileName(None, "Open XML File", "", "XML Files (*.xml)")
        print(f"Valor de file_name: {file_name}")
        if file_name:
                #segun el tipo de archivo que se selecciono se manda a llamar a la funcion correspondiente
                if tipo_archivo == "Usuarios":
                        #se manda a llamar a la funcion que carga los usuarios en la clase cargaMasivaUsuarios
                        self.cargaMasivaUsuarios = cargaMasivaUsuarios(file_name)
                        self.cargaMasivaUsuarios.cargar_xml()
                        #imprimir la lista de usuarios
                        print(self.cargaMasivaUsuarios.lista_usuarios.imprimir())
                elif tipo_archivo == "Empleados":
                        #se manda a llamar a la funcion que carga los empleados en la clase cargaMasivaEmpleados
                        self.cargaMasivaEmpleados = cargaMasivaEmpleados(file_name)
                        self.cargaMasivaEmpleados.cargar_xml()
                        #imprimir la lista de empleados
                        print(self.cargaMasivaEmpleados.lista_empleados.imprimir())
                elif tipo_archivo == "Productos":
                        #se manda a llamar a la funcion que carga los productos en la clase cargaMasivaProductos
                        self.cargaMasivaProducto = CargaMasivaProducto(file_name)
                        self.cargaMasivaProducto.cargar_xml()
                        print(self.cargaMasivaProducto.lista_productos.imprimir())
        else:
                print("No se seleccionó ningún archivo.")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_menu_cargar.setText(_translate("MainWindow", "Cargar"))
        self.bt_menu_reportes.setText(_translate("MainWindow", "Reportes"))
        self.bt_menu_actividades.setText(_translate("MainWindow", "Actividades"))
        self.bt_menu_compras.setText(_translate("MainWindow", "Compras"))
        self.go_login_inicio.setText(_translate("MainWindow", "Salir"))
        self.label.setText(_translate("MainWindow", "¡Bienvenido Administrador!"))
        self.bt_cargar_productos.setText(_translate("MainWindow", "Productos"))
        self.bt_cargar_usuarios.setText(_translate("MainWindow", "Usuarios"))
        self.bt_cargar_empleados.setText(_translate("MainWindow", "Empleados"))
        self.bt_cargar_actividades.setText(_translate("MainWindow", "Actividades"))
        self.go_login_cargar.setText(_translate("MainWindow", "Salir"))
        self.label_2.setText(_translate("MainWindow", "Reportes"))
        self.bt_reporte_usuarios.setText(_translate("MainWindow", "Reporte de Usuarios"))
        self.go_login_reportes.setText(_translate("MainWindow", "Salir"))
        self.bt_reporte_productos.setText(_translate("MainWindow", "Reporte de Productos"))
        self.bt_reportes_COLA.setText(_translate("MainWindow", "Reporte de Cola"))
        self.bt_reporte_compras.setText(_translate("MainWindow", "Reporte de Compras"))
        self.bt_reporte_vendedores.setText(_translate("MainWindow", "Reporte de Vendedores"))
        self.bt_reporte_actividades.setText(_translate("MainWindow", "Reporte de Actividades"))
        self.label_3.setText(_translate("MainWindow", "¡Actividades de Hoy!"))
        self.go_login_actividades.setText(_translate("MainWindow", "Salir"))
        self.label_4.setText(_translate("MainWindow", "Autoriza las Compras"))
        self.go_login_compras.setText(_translate("MainWindow", "Salir"))
        self.bt_compras_ok.setText(_translate("MainWindow", "Aprobar"))
        self.bt_compras_no.setText(_translate("MainWindow", "Denegar"))
        self.label_5.setText(_translate("MainWindow", "Cargar Usuarios"))
        self.go_login_CM_usuarios.setText(_translate("MainWindow", "Salir"))
        self.bt_up_cargaMasivaUsuarios.setText(_translate("MainWindow", "Cargar"))
        self.go_login_CM_productos.setText(_translate("MainWindow", "Salir"))
        self.bt_up_cargaMasivaProductos.setText(_translate("MainWindow", "Cargar"))
        self.label_6.setText(_translate("MainWindow", "Cargar Productos"))
        self.label_7.setText(_translate("MainWindow", "Cargar Empleados"))
        self.go_login_CM_empleados.setText(_translate("MainWindow", "Salir"))
        self.bt_up_cargaMasivaEmpleados.setText(_translate("MainWindow", "Cargar"))
        self.bt_up_cargaMasivaActividades.setText(_translate("MainWindow", "Cargar"))
        self.label_8.setText(_translate("MainWindow", "Cargar Actividades"))
        self.go_login_CM_Actividades.setText(_translate("MainWindow", "Salir"))
        self.label_9.setText(_translate("MainWindow", "Reporte Creado"))
        self.go_login_CM_Actividades_2.setText(_translate("MainWindow", "Salir"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
