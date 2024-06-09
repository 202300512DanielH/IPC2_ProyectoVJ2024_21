class Producto:
    def __init__(self, id, nombre, precio, descripcion, categoria, cantidad, imagen):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.categoria = categoria
        self.cantidad = cantidad
        self.imagen = imagen

    def validar_precio(self):
        try:
            float(self.precio)
            return True
        except:
            return False

    def validar_cantidad(self):
        try:
            int(self.cantidad)
            return True
        except:
            return False


    def __str__(self):
        return (f"ID: {self.id},\n Precio: {self.precio},\n Nombre: {self.nombre},\n Descripción: {self.descripcion},"
                f"\n Categoría: {self.categoria},\n Cantidad: {self.cantidad},\n Imagen: {self.imagen}")