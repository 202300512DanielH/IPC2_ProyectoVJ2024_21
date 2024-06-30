import re

class Usuario:
    def __init__(self, id, password, nombre, edad, email, telefono):
        self.id = id
        self.password = password
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.telefono = telefono
    
    # Función para validar el formato del correo electrónico
    @staticmethod
    def validar_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None


    # Función para validar el formato del número de teléfono
    @staticmethod
    def validar_telefono(telefono):
        return telefono.isdigit() and len(telefono) == 8
    
    def to_json(self):
        return {
            "id": self.id,
            "password": self.password,
            "nombre": self.nombre,
            "edad": self.edad,
            "email": self.email,
            "telefono": self.telefono
        }