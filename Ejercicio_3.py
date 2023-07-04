def encontrar_num():
    num_usuario = float(input("Ingrese el numero a buscar: "))
    num_menor = float(input("Ingrese el rango minimo: "))
    num_mayor = float(input("Ingrese el rango mayor: "))

    return num_usuario >= num_menor and num_usuario <= num_mayor
    
resultado = encontrar_num()
print(f"El resultado de su busqueda es: {resultado}")
