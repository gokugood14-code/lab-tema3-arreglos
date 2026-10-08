lista = []

while True:
    print("\n--- MENÚ ---")
    print("1. Insertar elemento al final")
    print("2. Eliminar elemento por posición")
    print("3. Buscar valor y mostrar su posición")
    print("4. Mostrar lista actualizada")
    print("5. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        valor = int(input("Valor a insertar: "))
        lista.append(valor)
        print("Elemento insertado.")

    elif opcion == "2":
        pos = int(input("Posición a eliminar (empieza en 0): "))
        if 0 <= pos < len(lista):
            eliminado = lista.pop(pos)
            print(f"Se eliminó el valor {eliminado}.")
        else:
            print("Posición inválida.")

    elif opcion == "3":
        valor = int(input("Valor a buscar: "))
        if valor in lista:
            print(f"El valor {valor} está en la posición {lista.index(valor)}.")
        else:
            print("El valor no se encuentra en la lista.")

    elif opcion == "4":
        print("Lista actual:", lista)

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")