#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

// Definición de la estructura ListNode
struct ListNode {
    char val;
    struct ListNode *next;
};

// Función para determinar si una lista enlazada de caracteres es un palíndromo
bool polindromo(struct ListNode* head) {
    // Si la lista está vacía o solo tiene un nodo, es un palíndromo
    if (head == NULL || head->next == NULL) {
        return true;
    }
    
    // Definir dos punteros para recorrer la lista enlazada
    struct ListNode *slow = head;
    struct ListNode *fast = head;
    
    // Usar el algoritmo de tortuga y liebre para encontrar el nodo medio de la lista
    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // Invertir la segunda mitad de la lista
    struct ListNode *prev = NULL;
    struct ListNode *curr = slow->next;
    struct ListNode *next = NULL;
    
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    
    // Comparar los valores de los nodos en la primera mitad y la segunda mitad
    struct ListNode *p1 = head;
    struct ListNode *p2 = prev;
    
    while (p2 != NULL) {
        if (p1->val != p2->val) {
            return false;
        }
        p1 = p1->next;
        p2 = p2->next;
    }
    
    return true;
}

// Función principal
int main() {
    // Crear una lista enlazada para probar la función polindromo
    struct ListNode *head = NULL;
    struct ListNode *prev = NULL;
    struct ListNode *current = NULL;

    // Añadir nodos a la lista enlazada
    char input[] = "abcdedcba"; // Cambia este valor según la cadena que quieras verificar
    for (int i = 0; input[i] != '\0'; i++) {
        current = malloc(sizeof(struct ListNode));
        current->val = input[i];
        current->next = NULL;
        if (head == NULL) {
            head = current;
        } else {
            prev->next = current;
        }
        prev = current;
    }
    
    // Llama a la función polindromo para verificar si la lista enlazada es un palíndromo
    if (polindromo(head)) {
        printf("La lista enlazada es un palíndromo.\n");
    } else {
        printf("La lista enlazada no es un palíndromo.\n");
    }
    
    // Liberar la memoria asignada para los nodos de la lista enlazada
    current = head;
    while (current != NULL) {
        prev = current;
        current = current->next;
        free(prev);
    }
    
    return 0;
}
