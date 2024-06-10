class Compras: 
    
    # Constructor
    def __init__(self, id_usuario, nombre, productos, total, estado = "Pendiente"):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre
        self.productos = productos
        self.total = total
    
    # Método para cambiar el estado de la compra
    def set_estado(self, estado):
        self.estado = estado

    # Método para imprimir la información de la compra
    def __str__(self):
        return f"ID Usuario: {self.id_usuario}\nNombre Usuario: {self.nombre_usuario}\nProductos: {self.productos}\nTotal: {self.total}"