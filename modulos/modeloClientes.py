class Cliente:
    def __init__(self, nombre, edad, email, direccion):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.direccion = direccion
        self.fechaCompra = []
        self.productosComprados = []

    def __str__(self):
        return f"Cliente: \n Nombre = {self.nombre}\n Edad = {self.edad}\n Email = {self.email}\n Direccion = {self.direccion}"
    
    def guardar_fechaCompra(self, fecha):
        self.fechaCompra.append(fecha)
        print(f"La fecha {fecha} fue agregada a las fechas de compra del cliente {self.nombre}")
    
    def guardar_productosComprados(self, producto):
        self.productosComprados.append(producto)
        print(f"El producto {producto} fue agregado a la lista de productos comprados por el cliente {self.nombre}")

