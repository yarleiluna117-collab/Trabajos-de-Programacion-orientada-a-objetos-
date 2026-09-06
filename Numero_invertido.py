numero = int(input("Ingresa un número entero: "))

signo = -1 if numero < 0 else 1
numero = abs(numero)

invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

invertido *= signo

print("Número invertido:", invertido)