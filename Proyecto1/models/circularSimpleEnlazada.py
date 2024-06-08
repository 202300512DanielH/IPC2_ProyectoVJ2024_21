from nodoCircularSimple import Nodo
class ListaCircularSimpleEnlazada:
    def __init__(self):
        self.primero = None

    # Metodo para insertar un empleado
    def insertar(self, empleado):
        nuevo_nodo = Nodo(empleado)
        # Si la lista esta vacia se inserta el empleado como el primero
        if self.primero is None:
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
        # Si la lista no esta vacia se inserta el empleado al final de la lista
        else:
            actual = self.primero
            # Se recorre la lista para llegar al final
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero

    # Metodo para eliminar un empleado
    def eliminar(self, codigo):
        # Si la lista esta vacia no se puede eliminar
        if self.primero is None:
            return False
        # Si el empleado a eliminar es el primero se elimina y se actualiza el primero
        if self.primero.empleado.codigo == codigo:
            # Si el empleado a eliminar es el unico en la lista se elimina y se limpia la lista 
            if self.primero.siguiente == self.primero:
                self.primero = None
            # Si el empleado a eliminar es el primero se elimina y se actualiza el primero
            else:
                actual = self.primero
                # Se recorre la lista para encontrar el ultimo empleado
                while actual.siguiente != self.primero:
                    actual = actual.siguiente
                actual.siguiente = self.primero.siguiente
                self.primero = self.primero.siguiente
            return True
        # Si el empleado a eliminar no es el primero se recorre la lista para encontrarlo
        actual = self.primero
        # Se recorre la lista para encontrar el empleado a eliminar
        while actual.siguiente != self.primero:
            # Si se encuentra el empleado se procede a eliminarlo
            if actual.siguiente.empleado.codigo == codigo:
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
        return False

    # Metodo para buscar un empleado
    def buscar(self, codigo):
        # Si la lista esta vacia no se puede buscar
        if self.primero is None:
            return None
        # Si el empleado a buscar es el primero se retorna el empleado
        actual = self.primero
        if actual.empleado.codigo == codigo:
            return actual.empleado
        actual = actual.siguiente
        # Si el empleado a buscar no es el primero se recorre la lista para encontrarlo
        while actual != self.primero:
            # Si se encuentra el empleado se retorna el empleado
            if actual.empleado.codigo == codigo:
                return actual.empleado
            actual = actual.siguiente
        return None # Si no se encuentra el empleado se retorna None porque no esta en la lista
    
    # Metodo para imprimir los empleados de la lista
    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.empleado.__str__())
            print("____________________________________________________")
            actual = actual.siguiente
        print()