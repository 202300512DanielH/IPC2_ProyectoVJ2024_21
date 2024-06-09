from PyQt5 import QtCore, QtGui, QtWidgets
import res


class Ui_Form(QtCore.QObject):
        
    verificador = QtCore.pyqtSignal(str)  # inicializando la señal verificador como una señal de tipo str
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(984, 613)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
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
        self.productos_combobox.addItem("")
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tittle.setText(_translate("Form", "Comprar"))
        self.ver_producto_button.setText(_translate("Form", "V E R"))
        self.productos_combobox.setCurrentText(_translate("Form", "Seleccionar Producto"))
        self.productos_combobox.setItemText(1, _translate("Form", "New Item"))
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
