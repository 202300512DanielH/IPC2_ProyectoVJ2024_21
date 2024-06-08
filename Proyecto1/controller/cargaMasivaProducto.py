import xml.etree.ElementTree as ET
from Proyecto1.models.nodoCircularDoble import Nodo
from Proyecto1.models.circularDoblementeEnlazada import ListaCircularDoblementeEnlazada
from Proyecto1.models.producto import Producto

def cargar_productos_desde_xml(archivo_xml):
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