class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.ids = set()

    def insertar(self, usuario):
        if usuario.id in self.ids:
            raise ValueError("El ID ya existe en la lista")
        if not usuario.validar_email():
            raise ValueError("El email no es válido")
        if not usuario.validar_telefono():
            raise ValueError("El teléfono no es válido")

        nuevo_nodo = Nodo(usuario)
        self.ids.add(usuario.id)

        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo

    def mostrar_usuarios(self):
        actual = self.primero
        while actual:
            print(f"ID: {actual.usuario.id}, Nombre: {actual.usuario.nombre}, Edad: {actual.usuario.edad}, Email: {actual.usuario.email}, Teléfono: {actual.usuario.telefono}")
            actual = actual.siguiente