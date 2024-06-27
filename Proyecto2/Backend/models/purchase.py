class Compra: 
    
    # Constructor
    def __init__(self, num_compra, id_usuario, nombre, productos_carrito, productos_stock):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre
        self.productos_carrito = productos_carrito
        self.productos_stock = productos_stock
        self.num_compra = num_compra
        #calculando el total de la compra si productos_carrito y productos_stock son diccionarios con la misma estructura
        self.total = 0
        for producto in productos_carrito:
            #buscando el producto en el stock para obtener el precio
            for producto_stock in productos_stock:
                if producto['producto'] == producto_stock['producto']:
                    self.total += float(producto['cantidad']) * float(producto_stock['precio'])
                    break
    
    def to_json(self):
        return {
            "num_compra": self.num_compra,
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "productos_carrito": self.productos_carrito,
            "productos_stock": self.productos_stock,
            "total": self.total
        }