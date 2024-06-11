from nodo_simple import Nodo

class cola: 
    # Constructor
    def __init__(self):
        self.head = None # Puntero al primer nodo de la lista, inicialmente None porque la lista está vacía 
        self.tail = None # Puntero al último nodo de la lista, inicialmente None porque la lista está vacía
        self.size = 0 # Tamaño de la lista, inicialmente 0 porque la lista está vacía
        
    # Método para agregar un nodo a la cola (al final de la lista)
    def push (self, dato): 
        nuevo_nodo = Nodo(dato) 
        #si la cola esta vacia
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
            self.size += 1
            return
        else: 
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo
            self.size += 1
            return
    
    # Método para eliminar un nodo de la cola y retornar su valor
    def pop(self):
        if self.head is None:
            return None
        else:
            aux = self.head
            self.head = self.head.siguiente
            self.size -= 1
            return aux.dato
    
    # Método para imprimir la cola
    def imprimir(self):
        actual = self.head
        while actual:
            print(actual.dato.__str__())
            print("____________________________________________________")
            actual = actual.siguiente
        print()    