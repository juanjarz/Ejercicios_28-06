def mult_numeros(*numeros):
    if len(numeros) == 0:
        return "No se ingresaron numeros"
    
    resultado = 1

    for num in numeros:
        resultado *= num
    return resultado

numeros_usuario = input("Ingrese los numeros que desea multiplicar separados por ',': ")
if not numeros_usuario:
    resultado = mult_numeros()
else:
    numeros_usuario = tuple(map(int, numeros_usuario.split(',')))
    resultado = mult_numeros(*numeros_usuario)
print(resultado)