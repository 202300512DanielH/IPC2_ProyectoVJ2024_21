class Compras: 
    
    # Constructor
    def __init__(self, id_usuario, nombre, productos, total):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre
        self.productos = cantidad_productos
        self.total = total
        
    # Método para imprimir la información de la compra
    def __str__(self):
        return f"ID Usuario: {self.id_usuario}\nNombre Usuario: {self.nombre_usuario}\nProductos: {self.productos}\nTotal: {self.total}"