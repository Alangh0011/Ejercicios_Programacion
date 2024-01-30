# Función para convertir números romanos a arábigos
def numeroromano(romano):
    # Diccionario que asigna valores numéricos a cada letra romana
    letras = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Inicializar el total en 0
    total = 0

    # Convertir la cadena de entrada a mayúsculas para evitar problemas de mayúsculas/minúsculas
    romano = romano.upper()

    # Inicializar el índice para iterar a través de la cadena
    j = 0

    # Iterar a través de la cadena de entrada
    while j < len(romano) - 1:
        print(f"ciclo:{j + 1}")

        # Comprobar si el valor de la letra actual es menor que el valor de la siguiente letra
        if letras[romano[j]] < letras[romano[j + 1]]:
            print(f"{romano[j]} < {romano[j + 1]}")
            # Restar el valor de la letra actual al total
            total -= letras[romano[j]]
            print(f"Entro en {romano[j]}{romano[j+1]} El total:{total}")
        else:
            # Sumar el valor de la letra actual al total
            total += letras[romano[j]]
            print(f"Entro en {romano[j]} El total:{total}")

        # Incrementar el índice para pasar a la siguiente letra
        j += 1

    # Sumar el valor de la última letra, ya que no se procesó en el bucle
    total += letras[romano[j]]

    # Imprimir el resultado final
    print(f"El total es: {total}")


# Llamada a la función con un ejemplo
if __name__ == '__main__':
    numeroromano("xiv")



