from nodo_simple import Nodo
import os, sys

class Lista_simplemente_enlazada: 
    # Constructor
    def __init__(self):
        self.head = None # Puntero al primer nodo de la lista, inicialmente None porque la lista está vacía
    
    # Método para agregar un nodo al final de la lista
    def append(self, dato): 
        nuevo_nodo = Nodo(dato) 
        if self.head is None:
            self.head = nuevo_nodo
            return
        else: 
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            
    # Método para eliminar un nodo de la lista
    def remove(self, dato):
        actual = self.head 
        anterior = None 
        while actual.dato.id_usuario != dato:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            return False
        elif anterior is None:
            self.head = actual.siguiente
            return True
        else:
            anterior.siguiente = actual.siguiente
            return True
            

    # Método para imprimir la lista
    def imprimir(self):
        actual = self.head 
        while actual:
            print(actual.dato.__str__(), end=' ')
            print("\n____________________________________________________")
            actual = actual.siguiente
        print()
    
    # Método para buscar un nodo en la lista
    def buscar(self, dato ):
        actual = self.head
        while actual.dato.id_usuario != dato:
            actual = actual.siguiente
        if actual is None:
            return False
        else:
            return actual.dato

    def graficar(self):
        codigodot = ''
        contador_nodos = 0
        
        #Creando la carpeta de reportes si no existe
        carpeta_reportes = 'Reportes'
        if not os.path.exists(carpeta_reportes):
            os.makedirs(carpeta_reportes)
        
        # Crear el archivo .dot
        archivo = open(os.path.join(carpeta_reportes, 'ListaCompras.dot'), 'w')
        codigodot += '''digraph G {
        rankdir=LR;
        node [shape = record, height = .1]'''
    
        #PRIMERO CREAMOS LOS NODOS
        actual = self.head
        while actual != None:
            codigodot += f'node{contador_nodos} [label="{{ID Usuario: {actual.dato.id_usuario}\\nNombre Usuario: {actual.dato.nombre_usuario}\\nProductos: {actual.dato.productos}\\nTotal: {actual.dato.total}|<f1>}}"];\n'
            contador_nodos += 1
            actual = actual.siguiente

        #AHORA CREAMOS LAS RELACIONES
        actual = self.head
        contador_nodos = 0
        while actual.siguiente != None:
            codigodot += 'node'+str(contador_nodos)+'-> node'+str(contador_nodos+1)+';\n'
            contador_nodos += 1
            actual = actual.siguiente

        codigodot += '}'

        #Lo escribimos en el archivo dot
        archivo.write(codigodot)
        archivo.close()

        #Generamos la imagen
        ruta_dot = 'Reportes/ListaCompras.dot'
        ruta_reporte = 'Reportes/ListaCompras.png'
        comando = 'dot -Tpng '+ruta_dot+' -o '+ruta_reporte
        os.system(comando)
        
        #Abrir la imagen
        #CONVERTIR DE RUTA RELATIVA A RUTA ABSOLUTA
        ruta_abrir_reporte = os.path.abspath(ruta_reporte)
        os.startfile(ruta_abrir_reporte)
        print('Reporte generado con éxito')