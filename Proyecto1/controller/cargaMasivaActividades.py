import xml.etree.ElementTree as ET
import os, sys
from tkinter import messagebox

#agregando la carpeta models al path de python  
script_dir = os.path.dirname(os.path.abspath(__file__))#obteniendo la ruta del directorio actual
#subiendo un nivel en la jerarquia de directorios  
ruta_proyecto = os.path.dirname(script_dir)
#accediendo a la carpeta models
sys.path.append(os.path.join(ruta_proyecto, 'models'))

from nodo_celda import NodoCelda
from lista_cabecera import ListaCabecera
from nodo_cabecera import NodoCabecera
from lista_ortogonal import ListaOrtogonal
from actividad import Actividad

class CargaMasivaActividades:
    # Crear una nueva lista ortogonal
    lista_actividades = ListaOrtogonal()
    
    # Constructor de la clase
    def __init__(self, archivo_xml = None):
        self.archivo_xml = archivo_xml
    
    # Metodo para cargar actividades desde un archivo xml
    def cargar_xml(self):
        try:
            # Leer el archivo XML y obtener la raíz
            arbol = ET.parse(self.archivo_xml)
            raiz = arbol.getroot()

            # Iterar sobre cada elemento 'actividad' en la raíz
            for elemento_actividad in raiz.findall('actividad'):
                # Crear un nuevo objeto Actividad con los datos del elemento
                id = elemento_actividad.get('id')
                nombre = elemento_actividad.find('nombre').text
                descripcion = elemento_actividad.find('descripcion').text
                empleado = elemento_actividad.find('empleado').text
                dia = elemento_actividad.find('dia').text
                hora = elemento_actividad.find('dia').get('hora')
                actividad = Actividad(id, nombre, descripcion, empleado, dia, hora)

                # Obtener las coordenadas x (fila) e y (columna)
                x = int(dia)
                y = int(hora)
                
                # Insertar la actividad en la lista ortogonal
                self.lista_actividades.insertar(x, y, actividad)
                
        except Exception as e:
            print(f"Error durante la carga del XML o la creación de la actividad: {e}")

        return self.lista_actividades