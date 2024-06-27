class Producto:
    def __init__(self, id, nombre, precio, descripcion, categoria, cantidad, imagen):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.categoria = categoria
        self.cantidad = cantidad
        self.imagen = imagen
    
    # Función para validar el formato del precio (debe contener decimales)
    @staticmethod
    def validar_precio(precio):
        try:
            float(precio)
            return '.' in precio
        except ValueError:
            return False

    # Función para validar el formato de la cantidad (debe ser un entero)
    @staticmethod
    def validar_cantidad(cantidad):
        return cantidad.isdigit()
    
    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "descripcion": self.descripcion,
            "categoria": self.categoria,
            "cantidad": self.cantidad,
            "imagen": self.imagen
        }