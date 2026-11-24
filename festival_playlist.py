# FESTIVAL DE MUSICA - PLAYLIST INTELIGENTE


nombres = []
artistas = []
duraciones = []
popularidades = []


def agregar_canciones():
    cantidad = int(input("¿Cuantas canciones deseas agregar? "))

    for i in range(cantidad):
        print(f"\\nCancion {i + 1}")

        nombre = input("Nombre de la cancion: ")
        artista = input("Nombre del artista: ")
        duracion = float(input("Duracion en minutos: "))

        while True:
            popularidad = int(input("Popularidad (1-100): "))

            if 1 <= popularidad <= 100:
                break
            else:
                print("La popularidad debe estar entre 1 y 100.")

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("\\nCanciones agregadas correctamente.")


def ver_reportes():
    if len(nombres) == 0:
        print("No hay canciones registradas.")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    promedio = sum(popularidades) / total_canciones

    indice_mayor = popularidades.index(max(popularidades))
    indice_menor = popularidades.index(min(popularidades))

    print("\\n===== REPORTES =====")
    print(f"Total de canciones: {total_canciones}")
    print(f"Duracion total: {duracion_total:.2f} minutos")
    print(f"Cancion mas popular: {nombres[indice_mayor]}")
    print(f"Popularidad: {popularidades[indice_mayor]}")
    print(f"Cancion menos popular: {nombres[indice_menor]}")
    print(f"Popularidad: {popularidades[indice_menor]}")
    print(f"Promedio de popularidad: {promedio:.2f}")


def buscar_canciones():
    if len(nombres) == 0:
        print("No hay canciones registradas.")
        return

    print("\\n===== BUSCAR CANCIONES =====")
    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        artista_buscar = input("Nombre del artista: ").lower()
        encontrados = 0

        for i in range(len(nombres)):
            if artista_buscar in artistas[i].lower():
                print(f"{nombres[i]} - {artistas[i]} - "
                      f"{duraciones[i]} min - Popularidad: {popularidades[i]}")
                encontrados += 1

        if encontrados == 0:
            print("No se encontraron canciones de ese artista.")

    elif opcion == "2":
        minimo = int(input("Popularidad minima: "))
        maximo = int(input("Popularidad maxima: "))
        encontrados = 0

        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                print(f"{nombres[i]} - {artistas[i]} - "
                      f"Popularidad: {popularidades[i]}")
                encontrados += 1

        if encontrados == 0:
            print("No se encontraron canciones en ese rango.")

    else:
        print("Opcion no valida.")


def playlist_recomendada():
    if len(nombres) == 0:
        print("No hay canciones registradas.")
        return

    promedio = sum(popularidades) / len(popularidades)

    print("\\n===== PLAYLIST RECOMENDADA =====")
    print(f"Popularidad promedio: {promedio:.2f}")
    print("Canciones por encima del promedio:\\n")

    encontrados = 0

    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print(f"{nombres[i]} - {artistas[i]} "
                  f"({popularidades[i]} puntos)")
            encontrados += 1

    if encontrados == 0:
        print("No hay canciones por encima del promedio.")


# Menu principal
while True:
    print("\\n===== FESTIVAL DE MUSICA =====")
    print("1. Agregar canciones")
    print("2. Ver reportes")
    print("3. Buscar canciones")
    print("4. Playlist recomendada")
    print("5. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        agregar_canciones()

    elif opcion == "2":
        ver_reportes()

    elif opcion == "3":
        buscar_canciones()

    elif opcion == "4":
        playlist_recomendada()

    elif opcion == "5":
        print("Gracias por utilizar la playlist del festival.")
        break

    else:
        print("Opcion no valida. Intenta de nuevo.")
