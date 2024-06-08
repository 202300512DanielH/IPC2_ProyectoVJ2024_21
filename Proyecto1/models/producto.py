class Producto:
    def __init__(self, id, precio, descripcion, categoria, cantidad, imagen):
        self.id = id
        self.precio = precio
        self.descripcion = descripcion
        self.categoria = categoria
        self.cantidad = cantidad
        self.imagen = imagen

    def __str__(self):
        return (f"ID: {self.id},\n Precio: {self.precio},\n Descripción: {self.descripcion},"
                f"\n Categoría: {self.categoria},\n Cantidad: {self.cantidad},\n Imagen: {self.imagen}")