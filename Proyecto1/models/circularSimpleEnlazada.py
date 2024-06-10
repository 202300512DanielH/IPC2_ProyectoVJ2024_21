from nodoCircularSimple import Nodo
import os 
class ListaCircularSimpleEnlazada:
    def __init__(self):
        self.primero = None

    def insertar(self, empleado):
        nuevo_nodo = Nodo(empleado)
        if self.primero is None:
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero

    def eliminar(self, codigo):
        if self.primero is None:
            return False
        if self.primero.empleado.codigo == codigo:
            if self.primero.siguiente == self.primero:
                self.primero = None
            else:
                actual = self.primero
                while actual.siguiente != self.primero:
                    actual = actual.siguiente
                actual.siguiente = self.primero.siguiente
                self.primero = self.primero.siguiente
            return True
        actual = self.primero
        while actual.siguiente != self.primero:
            if actual.siguiente.empleado.codigo == codigo:
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
        return False

    def buscar(self, codigo):
        if self.primero is None:
            return None
        actual = self.primero
        if actual.empleado.codigo == codigo:
            return actual.empleado
        actual = actual.siguiente
        while actual != self.primero:
            if actual.empleado.codigo == codigo:
                return actual.empleado
            actual = actual.siguiente
        return None

    def imprimir(self):
        if self.primero is None:
            print("La lista está vacía")
            return
        actual = self.primero
        while True:
            print(actual.empleado.__str__())
            print("____________________________________________________")
            actual = actual.siguiente
            if actual == self.primero:
                break
        print()
    
    def graficar(self):
        if self.primero is None:
            print("La lista está vacía, no hay nada que graficar.")
            return

        codigo_dot = ''
        carpeta_reportes = 'Reportes'
        if not os.path.exists(carpeta_reportes):
            os.makedirs(carpeta_reportes)

        archivo = open(os.path.join(carpeta_reportes, 'ListaCircularSimpleEnlazada.dot'), 'w')
        codigo_dot += '''digraph G {
        rankdir=LR;
        node [shape = record, style=filled, fillcolor=lightblue, fontname="Arial"];
        edge [fontname="Arial"];'''

        # Crear los nodos
        contador_nodos = 0
        actual = self.primero
        nodos = []
        while True:
            empleado = actual.empleado
            codigo_dot += f'node{contador_nodos} [label = "{{ Código: {empleado.codigo}\\nNombre: {empleado.nombre}\\nPuesto: {empleado.puesto}|<f2>}}"];\n'
            nodos.append(f'node{contador_nodos}')
            contador_nodos += 1
            actual = actual.siguiente
            if actual == self.primero:
                break

        # Hacer las relaciones
        for i in range(contador_nodos):
            siguiente = (i + 1) % contador_nodos
            codigo_dot += f'{nodos[i]} -> {nodos[siguiente]};\n'

        codigo_dot += '}'

        archivo.write(codigo_dot)
        archivo.close()

        # Imprimir el contenido del archivo .dot para depuración
        print("Contenido del archivo .dot:")
        print(codigo_dot)

        # Generar la imagen y abrir el reporte
        ruta_dot = os.path.join(carpeta_reportes, 'ListaCircularSimpleEnlazada.dot')
        ruta_imagen = os.path.join(carpeta_reportes, 'ListaCircularSimpleEnlazada.png')
        comando = f'dot -Tpng {ruta_dot} -o {ruta_imagen}'
        print(f"Ejecutando comando: {comando}")
        os.system(comando)

        ruta_abrir_reporte = os.path.abspath(ruta_imagen)
        os.startfile(ruta_abrir_reporte)
        print('Reporte generado con éxito')