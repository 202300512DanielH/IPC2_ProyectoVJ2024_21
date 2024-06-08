from nodoCircularDoble import Nodo

class ListaCircularDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    # Metodo para insertar un producto en la lista
    def insertar(self, producto):
        nuevo_nodo = Nodo(producto)
        # Si la lista esta vacia se inserta el producto como el primero y ultimo
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
        # Si la lista no esta vacia se inserta el producto al final de la lista
        else:
            nuevo_nodo.anterior = self.ultimo
            nuevo_nodo.siguiente = self.primero
            self.ultimo.siguiente = nuevo_nodo
            self.primero.anterior = nuevo_nodo
            self.ultimo = nuevo_nodo

    # Metodo para eliminar un producto de la lista
    def eliminar(self, producto):
        actual = self.primero
        # Se recorre la lista para encontrar el producto a eliminar
        while actual:
            # Si se encuentra el producto se procede a eliminarlo
            if actual.producto == producto:
                # Si el producto a eliminar es el unico en la lista se elimina y se limpia la lista
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                # Si el producto a eliminar es el primero se elimina y se actualiza el primero
                else:
                    self.primero = actual.siguiente
                # Si el producto a eliminar es el ultimo se elimina y se actualiza el ultimo
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                # Si el producto a eliminar es el ultimo se elimina y se actualiza el ultimo
                else:
                    self.ultimo = actual.anterior
                return True
            # Se continua recorriendo la lista hasta encontrar el producto a eliminar o llegar al final de la lista 
            actual = actual.siguiente
            if actual == self.primero:
                break
        return False