

class Usuario:
    def __init__(self, id, nombre, edad, email, telefono):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"Usuario({self.id}, {self.nombre}, {self.edad}, {self.email}, {self.telefono})"
