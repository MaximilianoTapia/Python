def seleccion_sort(lista):
    n = len(lista)

    for i in range(n):
        # Encuentra el índice del elemento más pequeño en el resto de la lista.
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        # Intercambia el elemento más pequeño con el elemento en la posición actual.
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Ejemplo de uso:
numbers = [6, 2, 4, 8, 5, 1, 7]
seleccion_sort(numbers)
print(numbers)  # Mostrará la lista ordenada.
