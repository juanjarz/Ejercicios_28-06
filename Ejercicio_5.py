def palindromo(word):
    word = word.replace(" ","").lower()
    if word == word[::-1]:
        return "Es palindromo"
    else:
        return "No es palindromo"

word = input("Ingrese la palabra a analizar: ")
resultado = palindromo(word)
print(resultado)