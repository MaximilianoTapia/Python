def insercion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1

        # Mueve los elementos mayores hacia la derecha para hacer espacio para el elemento actual.
        while j >= 0 and actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        # Inserta el elemento actual en la posición correcta.
        lista[j + 1] = actual

# Ejemplo de uso:
numbers = [6, 2, 4, 8, 5, 1, 7]
insercion_sort(numbers)
print(numbers)  # Mostrará la lista ordenada.
