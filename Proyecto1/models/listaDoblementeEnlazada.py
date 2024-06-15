from nodo import Nodo
from usuario import Usuario

import os

# Definición de la clase ListaDoblementeEnlazada
class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    # Metodo para insertar un usuario en la lista
    def insertar(self, nodo):
        usuario = nodo.usuario
        # Validar que el ID no exista en la lista
        actual = self.primero
        while actual is not None: 
            if actual.usuario.id == usuario.id:
                raise ValueError("El ID ya existe en la lista")
            actual = actual.siguiente
        # Validar que el email y el teléfono sean válidos
        if not usuario.validar_email():
            raise ValueError("El email no es válido")
        if not usuario.validar_telefono():
            raise ValueError("El teléfono no es válido")
        # Si la lista está vacía, se inserta el usuario como el primero y último
        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        else:
            self.ultimo.siguiente = nodo
            nodo.anterior = self.ultimo
            self.ultimo = nodo

    # Metodo para buscar un usuario en la lista
    def buscar(self, id):
        actual = self.primero
        # Se recorre la lista para encontrar el usuario a buscar
        while actual:
            # Si se encuentra el usuario se retorna el usuario
            if actual.usuario.id == id:
                return actual.usuario
            actual = actual.siguiente
        return None
    
    # Metodo para mostrar en consola los usuarios de la lista
    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.usuario.__str__())
            print("____________________________________________________")
            actual = actual.siguiente
        print()
    
    # Método para graficar la lista de usuarios con Graphviz
    def graficar(self):
        codigo_dot = ''
        
        # Crear la carpeta Reportes si no existe
        carpeta_reportes = 'Reportes'
        if not os.path.exists(carpeta_reportes):
            os.makedirs(carpeta_reportes)

        # Crear el archivo .dot
        archivo = open(os.path.join(carpeta_reportes, 'Listas_doblemente_enlazadas.dot'), 'w')
        codigo_dot += '''digraph G {
        rankdir=LR;
        node [shape = record, height = .1]'''

        # Crear los nodos
        contador_nodos = 0
        actual = self.primero
        while actual is not None:
            codigo_dot += 'node'+str(contador_nodos)+' [label = \"{<f1>| ID: '+str(actual.usuario.id)+'\\nNombre: '+str(actual.usuario.nombre)+'\\nEdad: '+str(actual.usuario.edad)+'\\nEmail: '+str(actual.usuario.email)+'\\nTelefono: '+str(actual.usuario.telefono)+'|<f2>}"];\n'
            contador_nodos += 1
            actual = actual.siguiente
            
        #HACEMOS LAS RELACIONES
        actual = self.primero
        contador_nodos = 0
        while actual.siguiente != None:
            #RELACIONES DE IZQUIERDA A DERECHA
            codigo_dot += 'node'+str(contador_nodos)+':f2 -> node'+str(contador_nodos+1)+':f1;\n'
            #RELACIONES DE DERECHA A IZQUIERDA
            codigo_dot += 'node'+str(contador_nodos+1)+':f1 -> node'+str(contador_nodos)+':f2;\n'
            contador_nodos += 1
            actual = actual.siguiente

        codigo_dot += '}'

        archivo.write(codigo_dot)
        archivo.close()

        # Generar la imagen y abrir el reporte
        ruta_dot = 'Reportes/Listas_doblemente_enlazadas.dot'
        ruta_imagen = 'Reportes/Listas_doblemente_enlazadas.png'
        comando = 'dot -Tpng ' + ruta_dot + ' -o ' + ruta_imagen
        os.system(comando)

        ruta_abrir_reporte = os.path.abspath(ruta_imagen)
        os.startfile(ruta_abrir_reporte)
        print('Reporte generado con éxito')