class Nodo:
    def __init__(self, empleado):
        self.empleado = empleado
        self.siguiente = None

    def __str__(self):
        return str(self.empleado)