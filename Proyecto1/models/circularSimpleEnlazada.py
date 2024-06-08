from nodoCircularSimple import Nodo
class ListaCircularSimpleEnlazada:
    def __init__(self):
        self.primero = None

    def insertar(self, empleado):
        nuevo_nodo = Nodo(empleado)
        if self.primero is None:
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero

    def eliminar(self, codigo):
        if self.primero is None:
            return False
        if self.primero.empleado.codigo == codigo:
            if self.primero.siguiente == self.primero:
                self.primero = None
            else:
                actual = self.primero
                while actual.siguiente != self.primero:
                    actual = actual.siguiente
                actual.siguiente = self.primero.siguiente
                self.primero = self.primero.siguiente
            return True
        actual = self.primero
        while actual.siguiente != self.primero:
            if actual.siguiente.empleado.codigo == codigo:
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
        return False

    def buscar(self, codigo):
        if self.primero is None:
            return None
        actual = self.primero
        if actual.empleado.codigo == codigo:
            return actual.empleado
        actual = actual.siguiente
        while actual != self.primero:
            if actual.empleado.codigo == codigo:
                return actual.empleado
            actual = actual.siguiente
        return None