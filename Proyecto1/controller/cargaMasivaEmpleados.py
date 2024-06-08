import xml.etree.ElementTree as ET
from Proyecto1.models.nodoCircularSimple import Nodo
from Proyecto1.models.circularSimpleEnlazada import ListaCircularSimpleEnlazada
from Proyecto1.models.empleado import Empleado

def cargar_empleados_desde_xml(archivo_xml):
    # Crear una nueva lista circular simple enlazada
    lista_empleados = ListaCircularSimpleEnlazada()

    # Leer el archivo XML y obtener la raíz
    arbol = ET.parse(archivo_xml)
    raiz = arbol.getroot()

    # Iterar sobre cada elemento 'empleado' en la raíz
    for elemento_empleado in raiz.findall('empleado'):
        # Crear un nuevo objeto Empleado con los datos del elemento
        codigo = elemento_empleado.get('codigo')
        nombre = elemento_empleado.find('nombre').text
        puesto = elemento_empleado.find('puesto').text
        empleado = Empleado(codigo, nombre, puesto)

        # Agregar el objeto Empleado a la lista circular simple enlazada
        nodo_empleado = Nodo(empleado)
        lista_empleados.insertar(nodo_empleado)

    return lista_empleados