###
# Ejercicio 2: Contador de Caracteres
# Escribe una función en Python llamada contador_caracteres que tome una
# cadena de texto como entrada y devuelva un diccionario que contenga
# la cantidad de veces que aparece cada carácter en la cadena.
# Si la entrada es "abracadabra", la salida debería ser {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}.
# Si la entrada es "python", la salida debería ser {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}.
###

def Contador(cadena):

    #len sirve para saber la longitud de la cadena
    longitud = len(cadena)
    print(f"La longitud de la cadena es: {longitud}")

    #index sirve para buscar la posicion de un caracter
    index = cadena.index("=")
    print(f"La posicion de = es: {index}")

    #count sirve para contar cuantas veces aparece un caracter
    conteo = cadena.count("1")
    print(f"Hay {conteo} 1 en la cadena: ")

    #split sirve para separar la cadena en una lista
    palabras = cadena.split()
    print(f"Lista de palabras con split:{palabras}")

    #join sirve para unir una lista en una cadena
    cadena = " ".join(palabras)
    print(f"Lista de palabras con join:{cadena}")


    dicconario = {}
    for i in cadena:
        print(f"El caracter {i} aparece {cadena.count(i)} veces en la cadena")
        if i in dicconario:
            #diccionadio[1] es la clave y se le suma 1
            dicconario[i] += 1
            print(f"entro al primer if{dicconario}")
        else:
            #diccionadio[1] es la clave y se le asigna 1
            dicconario[i] = 1
            print(f"entro al else{dicconario}")

    print(dicconario)



if __name__ == '__main__':
    #cadena = input("ingresa una cadena de texto")

    Contador("head = [1,2,3,2,1]")