import re
class Usuario:
    def __init__(self, id, password, nombre, edad, email, telefono):
        self.id = id
        self.password = password
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.telefono = telefono


    def validar_email(self):
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(patron, self.email) is not None

    def validar_telefono(self):
        return self.telefono.isdigit() and len(self.telefono) == 8

    def __str__(self):
        return f"ID: {self.id},\n Password: {self.password},\n Nombre: {self.nombre},\n Edad: {self.edad},\n Email: {self.email},\n Teléfono: {self.telefono}"