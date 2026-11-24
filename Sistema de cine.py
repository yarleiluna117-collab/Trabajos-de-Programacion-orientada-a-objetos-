
def mostrar_sala(matriz):
    print("\n===== SALA DE CINE =====")
    print("     ", end="")

    for columna in range(len(matriz[0])):
        print(f"{columna + 1:3}", end="")

    print()

    for i in range(len(matriz)):
        print(f"Fila {i + 1:2} ", end="")

        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:3}", end="")

        print()


def reservar_asiento(matriz):
    fila = int(input("Ingresa la fila: "))
    columna = int(input("Ingresa la columna: "))

    if 1 <= fila <= len(matriz) and 1 <= columna <= len(matriz[0]):
        if matriz[fila - 1][columna - 1] == "L":
            matriz[fila - 1][columna - 1] = "X"
            print("Asiento reservado correctamente.")
        else:
            print("Ese asiento ya está ocupado.")
    else:
        print("Error: el asiento no existe.")


def liberar_asiento(matriz):
    fila = int(input("Ingresa la fila: "))
    columna = int(input("Ingresa la columna: "))

    if 1 <= fila <= len(matriz) and 1 <= columna <= len(matriz[0]):
        if matriz[fila - 1][columna - 1] == "X":
            matriz[fila - 1][columna - 1] = "L"
            print("Asiento liberado correctamente.")
        else:
            print("Ese asiento ya está libre.")
    else:
        print("Error: el asiento no existe.")


def mostrar_estadisticas(matriz):
    ocupados = 0
    libres = 0

    for fila in matriz:
        for asiento in fila:
            if asiento == "X":
                ocupados += 1
            else:
                libres += 1

    print("\n===== ESTADISTICAS =====")
    print(f"Asientos ocupados: {ocupados}")
    print(f"Asientos libres: {libres}")


print("===== SISTEMA DE CINE =====")

filas = int(input("Numero de filas: "))
columnas = int(input("Numero de columnas: "))

# Crear matriz con todos los asientos libres
sala = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append("L")
    sala.append(fila)

# Menu principal
while True:
    print("\n===== MENU =====")
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        mostrar_sala(sala)

    elif opcion == "2":
        reservar_asiento(sala)

    elif opcion == "3":
        liberar_asiento(sala)

    elif opcion == "4":
        mostrar_estadisticas(sala)

    elif opcion == "5":
        print("Gracias por utilizar el sistema de cine.")
        break

    else:
        print("Opcion no valida. Intenta de nuevo.")
