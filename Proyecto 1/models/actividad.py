

class Actividad:
    def __init__(self, id, nombre, descripcion, empleado, dia, hora):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleado = empleado
        self.dia = dia
        self.hora = hora

    def __str__(self):
        return f"Actividad({self.id}, {self.nombre}, {self.descripcion}, {self.empleado}, {self.dia}, {self.hora})"
