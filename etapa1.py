lista = [12, 45, 7, 23, 89, 34, 56, 11, 78, 3]

print("Elementos de la lista:")
for elemento in lista:
    print(elemento)

nuevo = int(input("Ingrese el nuevo valor para el tercer elemento: "))
lista[2] = nuevo
print("Lista modificada:", lista)

buscar = int(input("Ingrese el número a buscar: "))
if buscar in lista:
    print(f"El número {buscar} SÍ existe en la lista.")
else:
    print(f"El número {buscar} NO existe en la lista.")