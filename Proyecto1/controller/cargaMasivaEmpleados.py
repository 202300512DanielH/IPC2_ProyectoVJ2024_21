import xml.etree.ElementTree as ET
import os, sys
from tkinter import messagebox

#agregando la carpeta models al path de python
script_dir = os.path.dirname(os.path.abspath(__file__))#obteniendo la ruta del directorio actual
#subiendo un nivel en la jerarquia de directorios
ruta_proyecto = os.path.dirname(script_dir)
#accediendo a la carpeta models
sys.path.append(os.path.join(ruta_proyecto, 'models'))

from nodoCircularSimple import Nodo
from circularSimpleEnlazada import ListaCircularSimpleEnlazada
from empleado import Empleado

class cargaMasivaEmpleados:

    lista_empleados = ListaCircularSimpleEnlazada()

    def __init__(self, archivo_xml=None):
        self.archivo_xml = archivo_xml


    # Método para cargar empleados desde un archivo XML
    def cargar_xml(self):
        # Leer el archivo XML y obtener la raíz
        arbol = ET.parse(self.archivo_xml)
        raiz = arbol.getroot()
        codigos_existentes = set()

        # Iterar sobre cada elemento 'empleado' en la raíz
        for elemento_empleado in raiz.findall('empleado'):
            # Crear un nuevo objeto Empleado con los datos del elemento
            codigo = elemento_empleado.get('codigo')
            nombre = elemento_empleado.find('nombre').text
            puesto = elemento_empleado.find('puesto').text
            empleado = Empleado(codigo, nombre, puesto)
            
            # Verificar si el código ya existe
            if codigo in codigos_existentes:
                print(f"Error: El código {codigo} ya existe. No se puede agregar el empleado {nombre}.")
                messagebox.showerror("Error de código", f"El código {codigo} ya existe. No se puede agregar el empleado {nombre}.")
            else:
                codigos_existentes.add(codigo)   
                self.lista_empleados.insertar(empleado)

        return self.lista_empleados