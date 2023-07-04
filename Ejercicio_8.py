def calcular_total(articulos):
    total_articulos = 0
    total_cobrar = 0
    
    for articulo in articulos:
        cantidad = articulo["cantidad"]
        precio = articulo["precio"]
        total_articulos += cantidad
        total_cobrar += cantidad * precio
    
    return total_articulos, total_cobrar

articulos = []

while True:
    nombre = input("Ingrese el nombre del artículo (o 'salir' para terminar): ")
    
    if nombre.lower() == "salir":
        break
    
    cantidad = int(input("Ingrese la cantidad de este artículo: "))
    precio = float(input("Ingrese el precio unitario de este artículo: "))
    
    articulo = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    articulos.append(articulo)

total_articulos, total_cobrar = calcular_total(articulos)

print("\nResumen de la compra:")
print("Cantidad de artículos:", total_articulos)
print("Cantidad a cobrar:", total_cobrar)
