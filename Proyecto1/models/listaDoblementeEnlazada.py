from nodo import Nodo
from usuario import Usuario

# Definición de la clase ListaDoblementeEnlazada
class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.ids = set() # Conjunto para almacenar los IDs de los usuarios

    # Metodo para insertar un usuario en la lista
    def insertar(self, nodo):
        usuario = nodo.usuario
        # Validar que el ID no exista en la lista
        if usuario.id in self.ids:
            raise ValueError("El ID ya existe en la lista")
        # Validar que el email y el teléfono sean válidos
        if not usuario.validar_email():
            raise ValueError("El email no es válido")
        if not usuario.validar_telefono():
            raise ValueError("El teléfono no es válido")

        # Agregar el ID al conjunto de IDs
        self.ids.add(usuario.id)

        # Si la lista está vacía, se inserta el usuario como el primero y último
        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        # Si la lista no está vacía, se inserta el usuario al final de la lista
        else:
            self.ultimo.siguiente = nodo
            nodo.anterior = self.ultimo
            self.ultimo = nodo

    # Metodo para buscar un usuario en la lista
    def buscar(self, id):
        actual = self.primero
        # Se recorre la lista para encontrar el usuario a buscar
        while actual:
            # Si se encuentra el usuario se retorna el usuario
            if actual.usuario.id == id:
                return actual.usuario
            actual = actual.siguiente
        return None
    
    # Metodo para mostrar en consola los usuarios de la lista
    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.usuario.__str__())
            print("____________________________________________________")
            actual = actual.siguiente
        print()