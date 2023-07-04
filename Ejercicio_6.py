def fibonacci(num):
    fibonacci_list = []

    if num >= 1:
        fibonacci_list.append(0)
    if num >= 2:
        fibonacci_list.append(1)
    for i in range (2,num):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    
    return fibonacci_list

num = int(input("Ingrese la cantidad de numeros de fibonacci que desea: "))
resultado = fibonacci(num)
print(resultado)