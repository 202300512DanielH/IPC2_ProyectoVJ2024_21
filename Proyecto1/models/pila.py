from nodo_simple import Nodo
import os, sys

class pila: 
    # Constructor de la clase
    def __init__(self):
        self.head = None # Puntero al primer nodo de la lista, inicialmente None porque la lista está vacía
        self.size = 0 # Tamaño de la pila, inicialmente 0
    
    # Método para agregar un nodo al final de la pila
    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.head
            self.head = nuevo_nodo
        self.size += 1
    
    # Método para eliminar el nodo que está en la cima de la pila
    def pop(self):
        if self.head is None:
            return None
        if self.head.siguiente is None:
            dato = self.head.dato
            self.head = None
        else:
            actual = self.head
            anterior = None
            while actual.siguiente:
                anterior = actual
                actual = actual.siguiente
            dato = actual.dato
            anterior.siguiente = None
        self.size -= 1
        return dato
        
    # Método para retornar el valor que está en la cima de la pila y eliminarlo para posteriormente extraer el siguiente valor
    def obtener(self):
        actual = self.head
        anterior = None
        while actual.siguiente:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            return False
        elif anterior is None:
            self.head = actual.siguiente
            self.size -= 1
            return actual.dato
        else:
            anterior.siguiente = actual.siguiente
            self.size -= 1
            return actual.dato
    
    # Método para obtener el tamaño de la pila 
    def get_size(self):
        return self.size
    
    # Método para graficar la pila con Graphviz
    def graficar(self, user_id):
        codigo_dot = 'digraph G {\n'
        actual = self.head
        contador_nodos = 0
        while actual:
            codigo_dot += f'nodo{contador_nodos} [label="ID del producto: {actual.dato.producto.id}: \nNombre de producto: {actual.dato.producto.nombre}: \nCantidad seleccionada: {actual.dato.cantidad}"];\n'
            if actual.siguiente:
                codigo_dot += f'nodo{contador_nodos} -> nodo{contador_nodos + 1};\n'
            actual = actual.siguiente
            contador_nodos += 1
        codigo_dot += '}'

        filename = f"Pila#{user_id}.dot"
        with open(filename, "w") as file:
            file.write(codigo_dot)

        output_filename = f"Pila{user_id}Usuario.png"
        os.system(f"dot -Tpng {filename} -o {output_filename}")
        os.system(f"{output_filename}")