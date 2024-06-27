class Empleado:
    def __init__(self, codigo, nombre, puesto):
        self.codigo = codigo
        self.nombre = nombre
        self.puesto = puesto
    
    def to_json(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "puesto": self.puesto
        }