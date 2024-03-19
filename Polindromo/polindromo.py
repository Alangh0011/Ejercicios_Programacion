def polindromo(list):
    numeros = []
    for numero in list:
        print(numero)
        if (numero == "1" or numero == "2" or numero == "3" or numero == "4" or numero == "5" or numero == "6" or numero == "7" or numero == "8" or numero == "9" or numero == "0"):
            numeros.append(numero)
            print("es numero:",numeros)

    numero_volteado = numeros[::-1]
    print(numero_volteado)

    if(numero_volteado == numeros):
        print("Es polindromo")
    else:
        print("No es polindromo")





# Llamada a la función con un ejemplo
if __name__ == '__main__':
    polindromo("head = [1,2,3,2,1]")
