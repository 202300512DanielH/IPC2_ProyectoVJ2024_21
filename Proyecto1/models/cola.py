from nodo_simple import Nodo
import os, sys
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
    
    # Método para eliminar un nodo de la cola
    def pop(self):
        if self.head is None:
            return None
        else:
            aux = self.head
            self.head = self.head.siguiente
            self.size -= 1
            return aux.dato
    
    # Método para saber si la cola esta vacia 
    def esta_vacia(self):
        return self.head is None
    
    # Método para obtener el primer nodo de la cola sin eliminarlo
    def primero(self):
        if self.head is None:
            return None
        else:
            return self.head.dato
    
    # Método para imprimir la cola
    def imprimir(self):
        actual = self.head
        while actual:
            print(actual.dato.__str__())
            print("____________________________________________________")
            actual = actual.siguiente
        print()

    def graficar(self):
        codigodot = ''
        carpeta_reportes = 'Reportes'
        if not os.path.exists(carpeta_reportes):
            os.makedirs(carpeta_reportes)

        archivo = open(os.path.join(carpeta_reportes, 'reporteCola.dot'), 'w')
        codigodot += '''digraph G {
    rankdir="RL";
    label="Cola";
    node[shape=box];\n'''

        contador = 0
        actual = self.head  # Call the method here
        conexiones = ''
        nodos = ''
        while actual is not None:
            nodos += f'Nodo{contador} [label="ID Usuario: {actual.dato.id_usuario}\\nNombre Usuario: {actual.dato.nombre_usuario}\\nProductos: {actual.dato.productos}\\nTotal: {actual.dato.total}"];\n'
            if actual.siguiente is not None:
                conexiones += 'Nodo'+str(contador+1) + ' -> Nodo'+str(contador)+';\n'
            contador += 1
            actual = actual.siguiente
            
        codigodot += nodos +"\n"+ conexiones + '\n}'

        archivo.write(codigodot)
        archivo.close()

        ruta_dot = 'Reportes/reporteCola.dot'
        ruta_salida = 'Reportes/reporteCola.png'
        comando = 'dot -Tpng ' + ruta_dot + ' -o ' + ruta_salida
        os.system(comando)

        ruta_salida2 = os.path.abspath(ruta_salida)
        os.startfile(ruta_salida2)