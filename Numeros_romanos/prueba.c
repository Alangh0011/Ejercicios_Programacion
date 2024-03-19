#include <conio.h>
#include <ctype.h>
#include <stdio.h>

int numero_romano (char numero[]){

    int numero_letras = strlen(numero);
    int numero_romano[numero_letras];
    printf("El numero de letras es: %d\n",numero_letras);
    for (int i = 0; i < numero_letras; i++)
    {
        numero[i] = toupper(numero[i]);
        if(numero[i] == 'I'){
            numero_romano[i] = 1;
        } else if(numero[i] == 'V'){
            numero_romano[i] = 5;
        } else if(numero[i] == 'X'){
            numero_romano[i] = 10;
        } else if(numero[i] == 'L'){
            numero_romano[i] = 50;
        } else if(numero[i] == 'C'){
            numero_romano[i] = 100;
        } else if(numero[i] == 'D'){
            numero_romano[i] = 500;
        } else if(numero[i] == 'M'){
            numero_romano[i] = 1000;
        } else {
            printf("El numero ingresado no es valido");
            return 0;
        }
    }

    int total = 0;
    for (int i = 0; i < numero_letras; i++)
    {
        if(i == numero_letras - 1){
            total+=numero_romano[i];
            printf("\nEl total es:%d y entro con %c",total, numero[i]);
            return total;
        }
        if (numero_romano[i] < numero_romano[i + 1])
        {
            total-=numero_romano[i];
            printf("\nEl total es:%d y entro con %c",total, numero[i]);
    
        } else {
            total+=numero_romano[i];
            printf("\nEl total es:%d y entro con %c",total, numero[i]);
        }
    }
    return total;
}

int main(int argc, char const *argv[])
{
    char palabra[10];
    printf("Ingrese un numero romano: ");
    scanf("%s",palabra);
    numero_romano(palabra);
    return 0;
}