class Carrito(): 
    
    # Constructor de la clase
    def __init__(self):
        self.productos = []

    def agregar_producto(self, id, producto, cantidad):
        #si el producto ya está en el carrito, se suma la cantidad
        for prod in self.productos:
            if prod['producto'] == producto:
                nueva_cantidad = int(prod['cantidad']) + int(cantidad)
                (prod['cantidad']) = str(nueva_cantidad)
                return
        #si no está, se agrega
        self.productos.append({'producto': producto, 'cantidad': cantidad, 'id': id})

    def vaciar_carrito(self):
        self.productos = []