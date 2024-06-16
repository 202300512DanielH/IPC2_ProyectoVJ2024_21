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
    
    #Funcion para obtener el tamaño de la lista
    def tamanio(self):
        contador = 0
        if self.primero is None:
            return contador
        actual = self.primero
        contador += 1
        actual = actual.siguiente
        while actual != self.primero:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def graficar(self):
        if self.primero is None:
            print("La lista está vacía, no hay nada que graficar.")
            return

        codigo_dot = '''digraph G {
        rankdir=LR;
        node [shape = record, style=filled, fillcolor=lightblue, fontname="Arial"];
        edge [fontname="Arial"];'''

        contador_nodos = 0
        actual = self.primero
        nodo_anterior = None

        while True:
            empleado = actual.empleado
            codigo_dot += f'node{contador_nodos} [label = "{{<f1> Código: {empleado.codigo}\\nNombre: {empleado.nombre}\\nPuesto: {empleado.puesto}|<f2>}}"];\n'
            if nodo_anterior is not None:
                codigo_dot += f'{nodo_anterior}:f2 -> node{contador_nodos}:f1;\n'
            nodo_anterior = f'node{contador_nodos}'
            contador_nodos += 1
            actual = actual.siguiente
            if actual == self.primero:
                break

        # Conectar el último nodo con el primero
        codigo_dot += f'{nodo_anterior}:f2 -> node0:f1;\n'
        codigo_dot += '}'

        carpeta_reportes = 'Reportes'
        if not os.path.exists(carpeta_reportes):
            os.makedirs(carpeta_reportes)

        archivo = open(os.path.join(carpeta_reportes, 'ListaVendedores.dot'), 'w')
        archivo.write(codigo_dot)
        archivo.close()

        print("Contenido del archivo .dot:")
        print(codigo_dot)

        ruta_dot = os.path.join(carpeta_reportes, 'ListaVendedores.dot')
        ruta_imagen = os.path.join(carpeta_reportes, 'ListaVendedores.png')
        comando = f'dot -Tpng {ruta_dot} -o {ruta_imagen}'
        os.system(comando)

        ruta_abrir_reporte = os.path.abspath(ruta_imagen)
        os.startfile(ruta_abrir_reporte)
        print('Reporte generado con éxito')