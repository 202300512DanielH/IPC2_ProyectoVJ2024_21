import xml.etree.ElementTree as ET
from Proyecto1.models.nodo import Nodo
from Proyecto1.models.listaDoblementeEnlzada import ListaDoblementeEnlazada
from Proyecto1.models.usuario import Usuario
def cargar_usuarios_desde_xml(archivo_xml):
    # Crear una nueva lista doblemente enlazada
    lista_usuarios = ListaDoblementeEnlazada()

    # Leer el archivo XML y obtener la raíz
    arbol = ET.parse(archivo_xml)
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
        lista_usuarios.insertar_al_final(nodo_usuario)

    return lista_usuarios