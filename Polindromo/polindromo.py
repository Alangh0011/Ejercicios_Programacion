def polindromo(list):
    print(list)
    numero_volteado = list[::-1]

    if(numero_volteado == list):
        print("Es polindromo")
    else:
        print("No es polindromo")





# Llamada a la función con un ejemplo
if __name__ == '__main__':
    polindromo("head = [1,2,3,4,5]")
