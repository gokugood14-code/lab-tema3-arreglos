matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))

print("\nMatriz ingresada:")
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end="\t")
    print()

suma = 0
for i in range(3):
    for j in range(3):
        suma += matriz[i][j]
print("Suma total de elementos:", suma)