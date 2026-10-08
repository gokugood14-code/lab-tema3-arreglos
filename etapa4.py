def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

original = [64, 25, 12, 22, 11, 90, 5, 38]

copia1 = original.copy()
print("Lista original:        ", original)
print("Ordenada con burbuja:  ", burbuja(copia1))

copia2 = original.copy()
print("Ordenada con selección:", seleccion(copia2))

print("\n¿Ambos resultados son iguales?", copia1 == copia2)