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
from usuario import Usuario

class cargaMasivaUsuarios:
    
    # Crear una nueva lista doblemente enlazada
    lista_usuarios = ListaDoblementeEnlazada()
    
    # Constructor de la clase
    def __init__(self, archivo_xml):
        self.archivo_xml = archivo_xml
    
    # Metodo para cargar usuarios desde un archivo xml
    def cargar_xml(self):
        # Leer el archivo XML y obtener la raíz
        arbol = ET.parse(self.archivo_xml)
        raiz = arbol.getroot()

        # Iterar sobre cada elemento 'usuario' en la raíz
        for elemento_usuario in raiz.findall('usuario'):
            # Crear un nuevo objeto Usuario con los datos del elemento
            id = elemento_usuario.get('id')
            nombre = elemento_usuario.find('nombre').text
            edad = elemento_usuario.find('edad').text
            email = elemento_usuario.find('email').text
            telefono = elemento_usuario.find('telefono').text
            usuario = Usuario(id, nombre, edad, email, telefono)

            # Agregar el objeto Usuario a la lista doblemente enlazada
            nodo_usuario = Nodo(usuario)
            self.lista_usuarios.insertar(nodo_usuario)

        return self.lista_usuarios