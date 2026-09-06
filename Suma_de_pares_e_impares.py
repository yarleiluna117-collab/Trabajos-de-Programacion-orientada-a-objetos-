n = int(input("Ingresa un número: "))

suma_pares = 0
suma_impares = 0

for numero in range(1, n + 1):

    if numero % 2 == 0:
        suma_pares += numero

    else:
        suma_impares += numero

print("Suma de pares:", suma_pares)
print("Suma de impares:", suma_impares)