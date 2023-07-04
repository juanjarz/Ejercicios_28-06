def numero_mayor(*numeros):
    if len(numeros) == 0:
        return "No se ingresaron numeros"
    
    mayor = numeros[0]

    for num in numeros:
        if num > mayor:
            mayor = num
    return mayor

numeros_usuario = input("Ingrese los numeros que desea sumar separados por ',': ")
if not numeros_usuario:
    resultado = numero_mayor()
else:
    numeros_usuario = tuple(map(int, numeros_usuario.split(',')))
    resultado = numero_mayor(*numeros_usuario)
print(resultado)