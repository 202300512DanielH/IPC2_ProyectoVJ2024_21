

class Producto:
    def __init__(self, id, precio, descripcion, categoria, cantidad, imagen):
        self.id = id
        self.precio = precio
        self.descripcion = descripcion
        self.categoria = categoria
        self.cantidad = cantidad
        self.imagen = imagen

    def __str__(self):
        return f"Producto({self.id}, {self.precio}, {self.descripcion}, {self.categoria}, {self.cantidad}, {self.imagen})"
