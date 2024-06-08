import xml.etree.ElementTree as etree
import os, sys

#agregando la carpeta models al path de python
script_dir = os.path.dirname(os.path.abspath(__file__))#obteniendo la ruta del directorio actual
#subiendo un nivel en la jerarquia de directorios
ruta_proyecto = os.path.dirname(script_dir)
#accediendo a la carpeta models
sys.path.append(os.path.join(ruta_proyecto, 'models'))

from nodo import Nodo
from listaDoblementeEnlazada import ListaDoblementeEnlazada
from producto import Producto

class cargaMasivaProducto:
    
    def cargar_xml(archivo_xml):
        # Crear una nueva lista circular doblemente enlazada
        lista_productos = ListaCircularDoblementeEnlazada()

        # Leer el archivo XML y obtener la raíz
        arbol = ET.parse(archivo_xml)
        raiz = arbol.getroot()

        # Iterar sobre cada elemento 'producto' en la raíz
        for elemento_producto in raiz.findall('producto'):
            # Crear un nuevo objeto Producto con los datos del elemento
            id = elemento_producto.get('id')
            precio = float(elemento_producto.find('precio').text)
            descripcion = elemento_producto.find('descripcion').text
            categoria = elemento_producto.find('categoria').text
            cantidad = int(elemento_producto.find('cantidad').text)
            imagen = elemento_producto.find('imagen').text
            producto = Producto(id, precio, descripcion, categoria, cantidad, imagen)

            # Agregar el objeto Producto a la lista circular doblemente enlazada
            nodo_producto = Nodo(producto)
            lista_productos.insertar(nodo_producto)

        return lista_productos