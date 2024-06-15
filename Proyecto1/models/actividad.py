

class Actividad:
    def __init__(self, id, nombre, descripcion, empleado, dia, hora):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleado = empleado
        self.dia = dia
        self.hora = hora

    def __str__(self):
        return f"Actividad: {self.id}, \n{self.nombre}, \n{self.descripcion}, \nID empleado: {self.empleado}, \nDía: {self.dia}, \nHora: {self.hora}"
