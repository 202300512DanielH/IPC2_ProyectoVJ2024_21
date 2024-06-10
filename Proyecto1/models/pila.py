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
            self.size += 1
            return
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            self.size += 1
    
    # Método para eliminar un nodo de la pila
    def pop(self):
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
            return True
        else:
            anterior.siguiente = actual.siguiente
            self.size -= 1
            return True
    
    # Método para graficar la pila con Graphviz
    def graficar(self):
        codigo_dot = ''
        contador_nodos = 0
        actual = self.head
        while actual:
            codigo_dot += f"nodo{contador_nodos} [label=\"{actual.dato}\"];\n"
            if actual.siguiente:
                codigo_dot += f"nodo{contador_nodos} -> nodo{contador_nodos+1};\n"
            actual = actual.siguiente
            contador_nodos += 1
        codigo_dot = f"digraph G {{\n{codigo_dot}}}"
        with open("pila.dot", "w") as file:
            file.write(codigo_dot)
        os.system("dot -Tpng pila.dot -o pila.png")
        os.system("pila.png")