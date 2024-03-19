#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

bool polindromo(char *head) {
    int len = strlen(head);
    char palabra_volteada[len + 1];
    char palabra[len + 1];
    
    int j = 0;
    for (int i = 0; i < len; i++) {
        if (isdigit(head[i])) {
            printf("\ncaracter en head:%c", head[i]);
            palabra[j] = head[i];
            j++;
        }
    }
    for (int i = 0; i < j; i++) {
        palabra_volteada[i] = palabra[j - i - 1];
    }
    
    palabra[j] = '\0';
    palabra_volteada[j] = '\0';

    printf("\nPalabra volteda:%s y palabra ingresada:%s", palabra_volteada, palabra);
    if (strcmp(palabra, palabra_volteada) == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main(int argc, char const *argv[]) {
    char head[100];
    printf("Ingresa palindromo head: {}: ");
    fgets(head, sizeof(head), stdin); // Lee la entrada completa, incluidos los espacios en blanco
    if (polindromo(head)) {
        printf("\nEs palindromo\n");
    } else {
        printf("\nNo es palindromo\n");
    }
    return 0;
}
