from modeloClientes import Cliente

cliente1 = Cliente("Lionel Messi", 35, "leomessi@barcelona.com", "Casteldefelds 123")
cliente2 = Cliente("Julian Alvarez", 23, "julian@carp.com.ar", "Figueroa Alcorta 7597")

print(cliente1)
print(cliente2)

cliente1.guardar_fechaCompra("18-12-2022")
cliente1.guardar_productosComprados("Botines")

print(cliente1.fechaCompra)
print(cliente1.productosComprados)
