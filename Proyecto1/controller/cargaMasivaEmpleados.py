import xml.etree.ElementTree as ET
import os, sys

#agregando la carpeta models al path de python
script_dir = os.path.dirname(os.path.abspath(__file__))#obteniendo la ruta del directorio actual
#subiendo un nivel en la jerarquia de directorios
ruta_proyecto = os.path.dirname(script_dir)
#accediendo a la carpeta models
sys.path.append(os.path.join(ruta_proyecto, 'models'))

from nodo import Nodo
from listaDoblementeEnlazada import ListaDoblementeEnlazada
from empleado import Empleado

class cargaMasivaEmpleados: 
    
    #metodo para cargar empleados desde un archivo xml
    def cargar_xml(archivo_xml):
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