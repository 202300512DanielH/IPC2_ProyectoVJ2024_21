from nodoCircularDoble import Nodo

class ListaCircularDoblementeEnlazada:
    #constructor de la clase
    def __init__(self):
        self.primero = None
        self.ultimo = None

    
    def insertar(self, producto):
        nuevo_nodo = Nodo(producto)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            nuevo_nodo.siguiente = self.primero
            self.ultimo.siguiente = nuevo_nodo
            self.primero.anterior = nuevo_nodo
            self.ultimo = nuevo_nodo

    def eliminar(self, producto):
        actual = self.primero
        while actual:
            if actual.producto == producto:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior
                return True
            actual = actual.siguiente
            if actual == self.primero:
                break
        return False

    def imprimir(self):
        actual = self.primero
        while actual:
            print(f"ID: {actual.producto.id},\n Precio: {actual.producto.precio},\n Descripción: {actual.producto.descripcion},\n Categoría: {actual.producto.categoria},\n Cantidad: {actual.producto.cantidad},\n Imagen: {actual.producto.imagen}")
            print("____________________________________________________")
            if actual.siguiente == self.primero:
                break
            actual = actual.siguiente
        print()