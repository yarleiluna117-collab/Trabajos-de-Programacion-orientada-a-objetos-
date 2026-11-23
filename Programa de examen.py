print("=== SISTEMA DE CALIFICACIONES ===")


estudiantes = int(input("¿Cuántos estudiantes hay? "))
materias = int(input("¿Cuántas materias hay? "))


calificaciones = []

for i in range(estudiantes):
    fila = []
    print(f"\nEstudiante {i + 1}")

    for j in range(materias):
        while True:
            calificacion = float(input(f"Calificación de la materia {j + 1}: "))

            if 0 <= calificacion <= 100:
                fila.append(calificacion)
                break
            else:
                print("Error: la calificación debe estar entre 0 y 100.")

    calificaciones.append(fila)

# Mostrar matriz
print("\n=== MATRIZ DE CALIFICACIONES ===")

for fila in calificaciones:
    print(fila)

print("\n=== PROMEDIO POR ESTUDIANTE ===")

for i in range(estudiantes):
    promedio = sum(calificaciones[i]) / materias
    print(f"Estudiante {i + 1}: {promedio:.2f}")

print("\n=== PROMEDIO POR MATERIA ===")

for j in range(materias):
    suma = 0

    for i in range(estudiantes):
        suma += calificaciones[i][j]

    promedio = suma / estudiantes
    print(f"Materia {j + 1}: {promedio:.2f}")

calificacion_maxima = max(max(fila) for fila in calificaciones)
calificacion_minima = min(min(fila) for fila in calificaciones)

print("\n=== RESULTADOS GENERALES ===")
print(f"Calificación más alta: {calificacion_maxima}")
print(f"Calificación más baja: {calificacion_minima}")

print("\nPrograma finalizado.")