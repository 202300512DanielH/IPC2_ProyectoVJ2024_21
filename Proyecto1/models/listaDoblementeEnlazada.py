from nodo import Nodo
from usuario import Usuario

import os

# Definición de la clase ListaDoblementeEnlazada
class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.ids = set() # Conjunto para almacenar los IDs de los usuarios

    # Metodo para insertar un usuario en la lista
    def insertar(self, nodo):
        usuario = nodo.usuario
        # Validar que el ID no exista en la lista
        if usuario.id in self.ids:
            raise ValueError("El ID ya existe en la lista")
        # Validar que el email y el teléfono sean válidos
        if not usuario.validar_email():
            raise ValueError("El email no es válido")
        if not usuario.validar_telefono():
            raise ValueError("El teléfono no es válido")

        # Agregar el ID al conjunto de IDs
        self.ids.add(usuario.id)

        # Si la lista está vacía, se inserta el usuario como el primero y último
        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        # Si la lista no está vacía, se inserta el usuario al final de la lista
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
        # Verificar si la carpeta "Reportes" existe, y crearla si no
        carpeta_reportes = 'Reportes'
        if not os.path.exists(carpeta_reportes):
            os.makedirs(carpeta_reportes)

        # Abrir el archivo para escribir
        archivo = open(os.path.join(carpeta_reportes, 'Listas_doblemente_enlazadas.dot'), 'w')
        codigo_dot += '''digraph G {
        rankdir=LR;
        node [shape = record, height = .1]'''
        contador_nodos = 0

        # PRIMERO CREAMOS LOS NODOS
        actual = self.primero
        while actual is not None:
            codigo_dot += f'node{contador_nodos} [label="{{ID: {actual.usuario.id}\\nNombre: {actual.usuario.nombre}\\nEdad: {actual.usuario.edad}\\nEmail: {actual.usuario.email}\\nTeléfono: {actual.usuario.telefono}|<f1>|<f2>}}"];\n'
            contador_nodos += 1
            actual = actual.siguiente

        # AHORA CREAMOS LAS RELACIONES DE IZQUIERDA A DERECHA
        actual = self.primero
        contador_nodos = 0
        while actual.siguiente is not None:
            codigo_dot += f'node{contador_nodos}:f2 -> node{contador_nodos+1}:f1;\n'
            contador_nodos += 1
            actual = actual.siguiente

        # AHORA CREAMOS LAS RELACIONES DE DERECHA A IZQUIERDA
        actual = self.ultimo
        contador_nodos -= 1  # Ajustamos el contador para apuntar al nodo actual
        while actual.anterior is not None:
            codigo_dot += f'node{contador_nodos}:f1 -> node{contador_nodos-1}:f2;\n'
            contador_nodos -= 1
            actual = actual.anterior

        codigo_dot += '}'

        # Escribimos el código DOT en el archivo
        archivo.write(codigo_dot)
        archivo.close()

        # Generamos la imagen
        ruta_dot = 'Reportes/Listas_doblemente_enlazadas.dot'
        ruta_imagen = 'Reportes/Listas_doblemente_enlazadas.png'
        comando = 'dot -Tpng ' + ruta_dot + ' -o ' + ruta_imagen
        os.system(comando)

        # Abrimos la imagen
        ruta_abrir_reporte = os.path.abspath(ruta_imagen)
        os.startfile(ruta_abrir_reporte)
        print('Reporte generado con éxito')