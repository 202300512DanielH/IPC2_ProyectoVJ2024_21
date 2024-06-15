import xml.etree.ElementTree as ET
import os
import sys
from tkinter import messagebox

# Agregando la carpeta models al path de Python
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_proyecto = os.path.dirname(script_dir)
sys.path.append(os.path.join(ruta_proyecto, 'models'))

from nodoCircularDoble import Nodo
from circularDoblementeEnlazada import ListaCircularDoblementeEnlazada
from producto import Producto

class CargaMasivaProducto:
    lista_productos = ListaCircularDoblementeEnlazada()
    
    def __init__(self, archivo_xml=None):
        self.archivo_xml = archivo_xml

    def cargar_xml(self):
        try:
            arbol = ET.parse(self.archivo_xml)
            raiz = arbol.getroot()
            for elemento_producto in raiz.findall('producto'):
                id = elemento_producto.get('id')
                nombre = elemento_producto.find('nombre').text
                precio = elemento_producto.find('precio').text
                descripcion = elemento_producto.find('descripcion').text
                categoria = elemento_producto.find('categoria').text
                cantidad = elemento_producto.find('cantidad').text
                imagen = elemento_producto.find('imagen').text
                producto = Producto(id, nombre, precio, descripcion, categoria, cantidad, imagen)
                
                if self.lista_productos.buscar(id) is not None:
                    print(f"Error: El ID {id} ya existe. El producto no se agregará.")
                    messagebox.showerror("Error de ID", f"El ID {id} ya existe. El producto no se agregará.")
                elif producto.validar_precio() and producto.validar_cantidad():
                    self.lista_productos.insertar(producto)  # Insert the 'producto' object
                else:
                    print(f"El producto {producto.id} no pasó la validación.")
                    messagebox.showerror("Error", "Producto(s) no válidos en el archivo XML. Los productos que sí son válidos se han cargado.")

        except Exception as e:
            print(f"Error durante la carga del XML o la creación del producto {e}")

        return self.lista_productos