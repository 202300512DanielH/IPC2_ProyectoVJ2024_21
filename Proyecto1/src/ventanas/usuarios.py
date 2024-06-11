from PyQt5 import QtCore, QtGui, QtWidgets
import res
import sys, os
from tkinter import messagebox

# agregando la carpeta ventanas al path de python
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, 'ventanas'))

from login import Ui_Form as ui_login_Form #importando la clase Ui_Form de login.py en la carpeta ventanas

# subiendo dos niveles para acceder a la carpeta que contiene la carpeta controller
parent_dir = os.path.dirname(os.path.dirname(script_dir))

# Navega a la carpeta controller y agrega la ruta al path de python
sys.path.append(os.path.join(parent_dir, 'controller'))

from cargaMasivaUsuarios import cargaMasivaUsuarios
from cargaMasivaProducto import CargaMasivaProducto

sys.path.append(os.path.join(parent_dir, 'models'))

from pila import pila
from carrito_compras import carrito_compras
from compras import Compras
from cola import cola

class Ui_Form(QtCore.QObject):
        
    #Creando pila para el carrito 
    lista_carrito = pila()
    
    cola_compras = cola()
    
    #constructor de la clase para que acepte la instancia de la clase login
    def __init__(self, login_window, ui_login):
        super().__init__()  # Llamada al constructor de la superclase
        self.login_window = login_window
        self.ui_login = ui_login
        #conectando la señal id_user de la clase login a la funcion comprar
        self.ui_login.id_user.connect(self.aux_id_user)           
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(984, 613)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.Form = Form
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 9, 961, 591))
        self.widget.setStyleSheet("QPushButton{\n"
" background-color: rgb(236, 253, 212);\n"
"    color: rgb(0,0,0); \n"
"    border: 2px solid rgb(199, 255, 193);\n"
"    border-bottom-width: 4px; \n"
"    border-bottom-color: rgb(150, 204, 144); \n"
"    border-radius: 15px; \n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: rgb(150, 204, 144); \n"
" border: 2px solid rgb(236, 253, 212);\n"
"    color: white; \n"
"}\n"
"QPushButton#regresar_button{\n"
" background-color: rgb(255, 189, 189);\n"
"    color: rgb(0,0,0); \n"
"    border: 2px solid rgb(255, 155, 155);\n"
"    border-bottom-width: 4px; \n"
"    border-bottom-color: rgb(255, 85, 85); \n"
"    border-radius: 15px; \n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton#regresar_button:hover{\n"
"  background-color: rgb(255, 85, 85); \n"
" border: 2px solid rgb(255, 189, 189);\n"
"    color: white; \n"
"}\n"
"\n"
"QComboBox#productos_combobox {\n"
"   width: 100%;\n"
"    height: 150px;\n"
"    padding: 12px 20px;\n"
"    border: 2px solid rgb(253, 229, 212);\n"
"    border-bottom-width: 4px; \n"
"    border-bottom-color: rgb(255, 165, 0);\n"
"    border-radius: 15px;\n"
"    background-color: rgb(253, 236, 224);\n"
"    font-size: 16px;\n"
"    color: rgb(156, 156, 156)\n"
"}\n"
"\n"
"    QComboBox::down-arrow {\n"
"        image:url(:/images/down-arrow.png);\n"
"        width: 28px; \n"
"        height: 20px;  \n"
"    }\n"
"    QComboBox::drop-down {\n"
"        border:none;\n"
"        width: 35px;  \n"
"        padding: 5px; \n"
"    \n"
"    }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border:none;\n"
"    border-radius: 10px;\n"
"    margin-left: 10px;\n"
"    background-color: rgb(253, 236, 224);\n"
"    selection-background-color: rgb(254, 206, 142);\n"
"    selection-border:none;\n"
"    selection-color: rgb(127, 127, 127);\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button {\n"
"            image: url(:/images/up-arrow (1).png);\n"
"            width: 20px;\n"
"            height: 20px;\n"
"            padding-right:2px;\n"
"        }\n"
"        QSpinBox::down-button {\n"
"            image: url(:/images/down-arrow.png);\n"
"            width: 20px;\n"
"            height: 20px;\n"
"            padding-right:2px;\n"
"            backgound-color:black;\n"
"        }")
        self.widget.setObjectName("widget")
        self.tittle = QtWidgets.QLabel(self.widget)
        self.tittle.setGeometry(QtCore.QRect(0, 10, 951, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(37)
        font.setBold(True)
        font.setWeight(75)
        self.tittle.setFont(font)
        self.tittle.setStyleSheet("")
        self.tittle.setAlignment(QtCore.Qt.AlignCenter)
        self.tittle.setObjectName("tittle")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(410, 110, 121, 6))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-radius:10%;\n"
"background-color:rgb(255, 170, 0)")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.ver_producto_button = QtWidgets.QPushButton(self.widget)
        self.ver_producto_button.setGeometry(QtCore.QRect(430, 168, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.ver_producto_button.setFont(font)
        self.ver_producto_button.setStyleSheet("color:black")
        self.ver_producto_button.setObjectName("ver_producto_button")
        self.actualizar_button = QtWidgets.QPushButton(self.widget)
        self.actualizar_button.setGeometry(QtCore.QRect(550, 168, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.actualizar_button.setFont(font)
        self.actualizar_button.setStyleSheet("color:black")
        self.actualizar_button.setObjectName("actualizar_button")
        self.productos_combobox = QtWidgets.QComboBox(self.widget)
        self.productos_combobox.setGeometry(QtCore.QRect(30, 160, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.productos_combobox.setFont(font)
        self.productos_combobox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.productos_combobox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.productos_combobox.setStyleSheet("color:black")
        self.productos_combobox.setObjectName("productos_combobox")
        self.productos_combobox.addItem("")
        self.productos_combobox.setItemText(0, "Seleccionar Producto")
        self.cantidad_producto = QtWidgets.QSpinBox(self.widget)
        self.cantidad_producto.setGeometry(QtCore.QRect(670, 440, 91, 44))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cantidad_producto.setFont(font)
        self.cantidad_producto.setStyleSheet("\n"
"padding: 12px 20px;\n"
"    border: 2px solid rgb(253, 229, 212);\n"
"    border-bottom-width: 4px; \n"
"    border-bottom-color: rgb(255, 165, 0);\n"
"    border-radius: 15px;\n"
"    background-color: rgb(253, 236, 224);\n"
"    font-size: 12px;")
        
        #Agregando PushButton para regresar al login
        self.regresar_button = QtWidgets.QPushButton(self.widget)
        self.regresar_button.setGeometry(QtCore.QRect(740, 50, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.regresar_button.setFont(font)
        self.regresar_button.setStyleSheet("color:black")
        self.regresar_button.setObjectName("regresar_button")
        
        self.cantidad_producto.setObjectName("cantidad_producto")
        self.agregar_button = QtWidgets.QPushButton(self.widget)
        self.agregar_button.setEnabled(True)
        self.agregar_button.setGeometry(QtCore.QRect(780, 430, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.agregar_button.setFont(font)
        self.agregar_button.setAcceptDrops(False)
        self.agregar_button.setStyleSheet("color:black")
        self.agregar_button.setObjectName("agregar_button")
        self.label_cantidad = QtWidgets.QLabel(self.widget)
        self.label_cantidad.setGeometry(QtCore.QRect(420, 440, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_cantidad.setFont(font)
        self.label_cantidad.setStyleSheet("")
        self.label_cantidad.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_cantidad.setObjectName("label_cantidad")
        self.label_nombre = QtWidgets.QLabel(self.widget)
        self.label_nombre.setGeometry(QtCore.QRect(420, 230, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_nombre.setFont(font)
        self.label_nombre.setStyleSheet("")
        self.label_nombre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_nombre.setObjectName("label_nombre")
        self.label_precio = QtWidgets.QLabel(self.widget)
        self.label_precio.setGeometry(QtCore.QRect(420, 270, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_precio.setFont(font)
        self.label_precio.setStyleSheet("")
        self.label_precio.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_precio.setObjectName("label_precio")
        self.label_descripcion = QtWidgets.QLabel(self.widget)
        self.label_descripcion.setGeometry(QtCore.QRect(420, 310, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_descripcion.setFont(font)
        self.label_descripcion.setStyleSheet("")
        self.label_descripcion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_descripcion.setObjectName("label_descripcion")
        self.label_categoria = QtWidgets.QLabel(self.widget)
        self.label_categoria.setGeometry(QtCore.QRect(420, 350, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_categoria.setFont(font)
        self.label_categoria.setStyleSheet("")
        self.label_categoria.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_categoria.setObjectName("label_categoria")
        self.label_categoria_2 = QtWidgets.QLabel(self.widget)
        self.label_categoria_2.setGeometry(QtCore.QRect(420, 390, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_categoria_2.setFont(font)
        self.label_categoria_2.setStyleSheet("")
        self.label_categoria_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_categoria_2.setObjectName("label_categoria_2")
        self.ver_carrito_button = QtWidgets.QPushButton(self.widget)
        self.ver_carrito_button.setGeometry(QtCore.QRect(530, 520, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.ver_carrito_button.setFont(font)
        self.ver_carrito_button.setStyleSheet("color:black")
        self.ver_carrito_button.setObjectName("ver_carrito_button")
        self.comprar_button = QtWidgets.QPushButton(self.widget)
        self.comprar_button.setGeometry(QtCore.QRect(740, 520, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.comprar_button.setFont(font)
        self.comprar_button.setStyleSheet("color:black")
        self.comprar_button.setObjectName("comprar_button")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 230, 361, 311))
        self.label.setStyleSheet("image:url(:/images/error-image.png);\n"
"background-color:rgb(198, 198, 198);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(270, 40, 81, 51))
        self.label_2.setStyleSheet("image: url(:/images/carretilla.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.nombre = QtWidgets.QLabel(self.widget)
        self.nombre.setGeometry(QtCore.QRect(610, 230, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.nombre.setFont(font)
        self.nombre.setStyleSheet("")
        self.nombre.setText("")
        self.nombre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nombre.setObjectName("nombre")
        self.precio = QtWidgets.QLabel(self.widget)
        self.precio.setGeometry(QtCore.QRect(590, 270, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.precio.setFont(font)
        self.precio.setStyleSheet("")
        self.precio.setText("")
        self.precio.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.precio.setObjectName("precio")
        self.descripcion = QtWidgets.QLabel(self.widget)
        self.descripcion.setGeometry(QtCore.QRect(530, 310, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.descripcion.setFont(font)
        self.descripcion.setStyleSheet("")
        self.descripcion.setText("")
        self.descripcion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.descripcion.setObjectName("descripcion")
        self.categoria = QtWidgets.QLabel(self.widget)
        self.categoria.setGeometry(QtCore.QRect(510, 350, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.categoria.setFont(font)
        self.categoria.setStyleSheet("")
        self.categoria.setText("")
        self.categoria.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.categoria.setObjectName("categoria")
        self.cantidad = QtWidgets.QLabel(self.widget)
        self.cantidad.setGeometry(QtCore.QRect(500, 390, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cantidad.setFont(font)
        self.cantidad.setStyleSheet("")
        self.cantidad.setText("")
        self.cantidad.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cantidad.setObjectName("cantidad")
        
        #conectando el boton de regresar al login
        self.regresar_button.clicked.connect(lambda: self.show_login(Form))
        
        #conectando el boton de actualizar el combobox
        self.actualizar_button.clicked.connect(lambda: self.actualizar_combobox())
        
        #conectando el boton de ver producto para mostrar la informacion del producto seleccionado
        self.ver_producto_button.clicked.connect(lambda: self.mostrar_producto())
        
        #conectando el boton de agregar al carrito
        self.agregar_button.clicked.connect(lambda: self.agregar_carrito())
        
        #conectando el boton de ver carrito para graficar el carrito
        self.ver_carrito_button.clicked.connect(lambda: self.graficar_carrito())
        
        #conectando el boton de comprar
        self.comprar_button.clicked.connect(lambda: self.comprar())
        
        #haciendo una instancia de la clase login 
        self.ui_login_Form = ui_login_Form()
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    #funcion para obtener el id del usuario que ha iniciado sesion
    def aux_id_user(self, id_user):
        self.id_user = id_user

    # Definir la señal que emitirá la cola de compras
    cola_compras_signal = QtCore.pyqtSignal(cola)
    
    #funcion para comprar los productos del carrito
    def comprar(self) :
        
        global lista_carrito
        
        global cola_compras
        
        #obteniendo la lista de la carga masiva de usuarios
        self.carga_masiva_usuarios = cargaMasivaUsuarios()
        #llamando a la lista de usuarios en la carga masiva 
        self.lista_usuarios = self.carga_masiva_usuarios.lista_usuarios
       
        #obteniendo el id del usuario que ha iniciado sesion
        nombre_usuario = self.lista_usuarios.buscar(self.id_user).nombre
        
        # Haciendo una copia de la lista del carrito
        self.lista_carrito_copia = pila() 
        self.lista_auxiliar = pila()
        for i in range(self.lista_carrito.get_size()):
                producto = self.lista_carrito.obtener()
                self.lista_carrito_copia.push(producto)
                self.lista_auxiliar.push(producto)
        
        # regresando los productos de la lista auxiliar a la lista original
        for i in range(self.lista_auxiliar.get_size()):
                producto = self.lista_auxiliar.obtener()
                self.lista_carrito.push(producto)
        
        #obteniendo el precio total de la compra tomando en cuenta que los productos se encuentran en una pila y esta no es iterable 
        nombres_productos = " "
        total = 0 
        for i in range(self.lista_carrito_copia.get_size()):
                producto = self.lista_carrito_copia.obtener()
                total += float(producto.producto.precio) * producto.cantidad
                nombres_productos += producto.producto.nombre + ", "
                
        try: 
                #creando una nueva compra 
                self.compra = Compras(self.id_user, nombre_usuario, nombres_productos, total)
        
                # colocando la compra en la cola
                self.cola_compras.push(self.compra)
                
                #imprimiendo la cola 
                self.cola_compras.imprimir()
        except:
                messagebox("Error", "No se ha podido realizar la compra")

        self.cola_compras_signal.emit(self.cola_compras)
        
    #funcion para agregar un producto al carrito con la cantidad seleccionada
    def agregar_carrito(self):
        global lista_carrito
        
        # Obteniendo el nombre del producto seleccionado
        nombre_producto = self.productos_combobox.currentText()
        
        # Obteniendo la lista de productos 
        self.carga_masiva_productos = CargaMasivaProducto()
        self.lista_productos = self.carga_masiva_productos.lista_productos
        
        # Obteniendo el producto seleccionado de la lista de productos
        producto = self.lista_productos.buscar(nombre_producto)
        
        # Obteniendo la cantidad seleccionada
        cantidad_seleccionada = self.cantidad_producto.value()
        
        # Creando un nuevo carrito 
        carrito_item = carrito_compras(producto, cantidad_seleccionada)
        
        # Si no se ha seleccionado ningún producto se muestra un mensaje de error
        if nombre_producto == "Seleccionar Producto":
                messagebox.showerror("Error", "No se ha seleccionado ningun producto")
                return
        
        # Mostrando un mensaje de máximo alcanzado si la cantidad seleccionada es mayor a la cantidad del producto
        if cantidad_seleccionada > int(producto.cantidad):
                messagebox.showinfo("Maximo alcanzado", "La cantidad seleccionada es mayor a la cantidad disponible del producto")
                return
        
        # Si la cantidad seleccionada es mayor a 0 se agrega el producto al carrito
        if cantidad_seleccionada > 0:
                # Agregando el producto al carrito
                self.lista_carrito.push(carrito_item)
                messagebox.showinfo("Producto agregado", "El producto ha sido agregado al carrito")

    
    #funcion para graficar el carrito
    def graficar_carrito(self):
        global lista_carrito
        self.lista_carrito.graficar()
    
    #funcion para mostrar la informacion del producto seleccionado
    def mostrar_producto(self):
        #Obteniendo el nombre del producto seleccionado
        nombre_producto = self.productos_combobox.currentText()
        
        #Obteniendo la lista de productos 
        self.carga_masiva_productos = CargaMasivaProducto()
        self.lista_productos = self.carga_masiva_productos.lista_productos
        
        #obteniendo el producto seleccionado de la lista de productos
        producto = self.lista_productos.buscar(nombre_producto)
        
        #insertando la informacion del producto en los labels correspondientes
        self.nombre.setText(producto.nombre)
        self.precio.setText(producto.precio)
        self.descripcion.setText(producto.descripcion)
        self.categoria.setText(producto.categoria)
        self.cantidad.setText(producto.cantidad)
        
        #mostrando la imagen del producto en el label de la imagen
        self.label.setStyleSheet(f"image:url(:/images/{producto.imagen});\n"
"background-color:rgb(198, 198, 198);")
        
        #si no se ha seleccionado ningun producto se muestra un mensaje de error
        if nombre_producto == "Seleccionar Producto":
                messagebox.showerror("Error", "No se ha seleccionado ningun producto")
        
        #modificando el spinbox para que tenga un maximo de la cantidad del producto
        self.cantidad_producto.setMaximum(int(producto.cantidad))
        
        # mostrando un mensaje de maximo alcanzado si la cantidad seleccionada es igual a la cantidad del producto
        if self.cantidad_producto.value() > int(producto.cantidad):
                messagebox.showinfo("Maximo alcanzado", "La cantidad seleccionada es mayor a la cantidad disponible del producto")
    
    #funcion para actualizar el combobox
    def actualizar_combobox(self):
        #Eliminando items innecesarios del combobox
        self.productos_combobox.clear()
        
        #Obteniendo la lista de productos 
        self.carga_masiva_productos = CargaMasivaProducto()
        self.lista_productos = self.carga_masiva_productos.lista_productos
        
        #Agregando los productos al combobox teniendo en cuenta que la lista de productos no es iterable y que al inicio del programa no se ha cargado ningun producto
        self.productos_combobox.addItem("Seleccionar Producto")
        for producto in self.lista_productos:
                self.productos_combobox.addItem(producto.nombre)
    
    #funcion para regresar al login
    def show_login(self, Form):
        print("Regresando al login")
        # Cerrando la ventana del usuario
        self.Form.close()
        #Regresando a la ventana de login
        self.login_window.show()
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tittle.setText(_translate("Form", "Comprar"))
        self.ver_producto_button.setText(_translate("Form", "V E R"))
        self.actualizar_button.setText(_translate("Form", "A C T U A L I Z A R"))
        self.productos_combobox.setCurrentText(_translate("Form", "Seleccionar Producto"))
        self.agregar_button.setText(_translate("Form", "A G R E G A R   A L    \n"
"C A R R I T O  "))
        self.label_cantidad.setText(_translate("Form", "Cantidad a agregar al carrito:"))
        self.label_nombre.setText(_translate("Form", "Nombre del producto:"))
        self.label_precio.setText(_translate("Form", "Precio del producto:"))
        self.label_descripcion.setText(_translate("Form", "Descripcion:"))
        self.label_categoria.setText(_translate("Form", "Categoria:"))
        self.label_categoria_2.setText(_translate("Form", "Cantidad:"))
        self.ver_carrito_button.setText(_translate("Form", "V E R   C A R R I T O"))
        self.comprar_button.setText(_translate("Form", "C O M P R A R"))
        self.regresar_button.setText(_translate("Form", "S A L I R"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
