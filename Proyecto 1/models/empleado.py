
class Empleado:
    def __init__(self, codigo, nombre, puesto):
        self.codigo = codigo
        self.nombre = nombre
        self.puesto = puesto

    def __str__(self):
        return f"Empleado({self.codigo}, {self.nombre}, {self.puesto})"
