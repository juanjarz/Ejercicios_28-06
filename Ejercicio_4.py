def num_primo(num):
    if num <= 1:
        return "No es primo"
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "No es primo"
    
    return "El numero es primo"

num = int(input("Ingrese el numero a analizar: "))
resultado = num_primo(num)
print(resultado)