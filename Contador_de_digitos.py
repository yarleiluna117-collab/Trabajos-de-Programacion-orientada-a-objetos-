numero = int(input("Ingresa un número entero: "))

numero = abs(numero)

if numero == 0:
    contador = 1
else:
    contador = 0

    while numero > 0:
        contador += 1
        numero //= 10

print("El número tiene", contador, "dígitos.")