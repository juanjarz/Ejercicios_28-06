def calcular(operacion, numero):
    if operacion == "+":
        return resultado + numero
    elif operacion == "-":
        return resultado - numero
    elif operacion == "*":
        return resultado * numero
    elif operacion == "/":
        return resultado / numero
    else:
        return numero

resultado = None

while True:
    entrada = input("$ ")
    
    if entrada == "":
        continue
    
    if entrada[-1] == "=":
        entrada = entrada[:-1]
        resultado = calcular(operacion, float(entrada))
        print("Resultado final:", resultado)
        break
    
    if resultado is None:
        resultado = float(entrada)
    else:
        operacion = entrada[0]
        numero = float(entrada[1:])
        resultado = calcular(operacion, numero)
    
    print(resultado)
