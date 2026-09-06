n = int(input("Ingresa la altura de la pirámide: "))

for fila in range(1, n + 1):

    espacios = " " * (n - fila)
    asteriscos = "*" * (2 * fila - 1)

    print(espacios + asteriscos)