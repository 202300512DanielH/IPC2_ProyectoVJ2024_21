from nodoCircularDoble import Nodo
import os 

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
        if self.primero is None:
            print("La lista está vacía")
            return

        actual = self.primero
        while True:
            producto = actual.producto  # Accede al atributo 'producto' del nodo actual
            print(f"ID: {producto.id},\n Nombre: {producto.nombre},\n Precio: {producto.precio},\n Descripción: {producto.descripcion},\n Categoría: {producto.categoria},\n Cantidad: {producto.cantidad},\n Imagen: {producto.imagen}")
            actual = actual.siguiente
            if actual == self.primero:  # Si hemos vuelto al principio, termina el bucle
                break
    
    #Metodo para verificar si la lista esta vacia
    def esta_vacia(self):
        return self.primero is None
    
    # Método para buscar un producto en la lisat circular doblemente enlazada, recibe el nombre del producto a buscar
    def buscar(self, nombre):
        # Si la lista está vacía
        if self.esta_vacia():
            return None
        else: 
            actual = self.primero
            while True:
                if actual.producto.nombre == nombre:
                    return actual.producto
                actual = actual.siguiente
                if actual == self.primero:
                    break

    # Método para iterar sobre la lista circular doblemente enlazada
    def __iter__(self):
        #si la lista esta vacia
        if self.esta_vacia():
            return
        else: 
            actual = self.primero
            while True:
                yield actual.producto
                actual = actual.siguiente
                if actual == self.primero:
                    break
    
    def graficar(self):
        codigo_dot = ''
        carpeta_reportes = 'Reportes'
        if not os.path.exists(carpeta_reportes):
            os.makedirs(carpeta_reportes)

        archivo = open(os.path.join(carpeta_reportes, 'ListaCircularDoblementeEnlazada.dot'), 'w')
        codigo_dot += '''digraph G {
        rankdir=LR;
        node [shape = record, height = .1];'''

        # Crear los nodos
        contador_nodos = 0
        actual = self.primero
        nodos = []
        if actual is not None:
            while True:
                producto = actual.producto
                codigo_dot += f'node{contador_nodos} [label = "{{<f1>| ID: {producto.id}\\nNombre: {producto.nombre}\\nPrecio: {producto.precio}\\nDescripción: {producto.descripcion}\\nCategoría: {producto.categoria}\\nCantidad: {producto.cantidad}\\nImagen: {producto.imagen}|<f2>}}"];\n'
                nodos.append(f'node{contador_nodos}')
                contador_nodos += 1
                actual = actual.siguiente
                if actual == self.primero:
                    break

            # Hacer las relaciones
            for i in range(contador_nodos):
                siguiente = (i + 1) % contador_nodos
                codigo_dot += f'{nodos[i]}:f2 -> {nodos[siguiente]}:f1;\n'
                codigo_dot += f'{nodos[siguiente]}:f1 -> {nodos[i]}:f2;\n'

        codigo_dot += '}'

        archivo.write(codigo_dot)
        archivo.close()

        # Generar la imagen y abrir el reporte
        ruta_dot = os.path.join(carpeta_reportes, 'ListaCircularDoblementeEnlazada.dot')
        ruta_imagen = os.path.join(carpeta_reportes, 'ListaCircularDoblementeEnlazada.png')
        comando = f'dot -Tpng {ruta_dot} -o {ruta_imagen}'
        os.system(comando)

        ruta_abrir_reporte = os.path.abspath(ruta_imagen)
        os.startfile(ruta_abrir_reporte)
        print('Reporte generado con éxito')

