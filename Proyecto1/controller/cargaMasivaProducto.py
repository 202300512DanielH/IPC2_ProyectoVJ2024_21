import xml.etree.ElementTree as ET
import os
import sys

# Agregando la carpeta models al path de Python
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_proyecto = os.path.dirname(script_dir)
sys.path.append(os.path.join(ruta_proyecto, 'models'))

from nodoCircularDoble import Nodo
from circularDoblementeEnlazada import ListaCircularDoblementeEnlazada
from producto import Producto

class CargaMasivaProducto:
    
    # Crear una nueva lista circular doblemente enlazada 
    lista_productos = ListaCircularDoblementeEnlazada()
    
    def __init__(self, archivo_xml):
        self.archivo_xml = archivo_xml

    def cargar_xml(self):
        arbol = ET.parse(self.archivo_xml)
        raiz = arbol.getroot()
        for elemento_producto in raiz.findall('producto'):
            id = elemento_producto.get('id')
            precio = float(elemento_producto.find('precio').text)
            descripcion = elemento_producto.find('descripcion').text
            categoria = elemento_producto.find('categoria').text
            cantidad = int(elemento_producto.find('cantidad').text)
            imagen = elemento_producto.find('imagen').text
            producto = Producto(id, precio, descripcion, categoria, cantidad, imagen)
            self.lista_productos.insertar(producto)
        return self.lista_productos