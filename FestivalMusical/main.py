from cantante import Cantante
from dj import DJ
from banda import Banda
from festival import iniciar_festival


def solicitar_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El dato no puede quedar vacío. Intenta nuevamente.")


def solicitar_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Ingresa un número igual o mayor que {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Ingresa un número igual o menor que {maximo}.")
                continue
            return valor
        except ValueError:
            print("Por favor, ingresa un número entero válido.")


def main():
    print("===== REGISTRO DEL FESTIVAL MUSICAL =====")
    cantidad = solicitar_entero("¿Cuántos artistas se presentarán?: ", 1)
    lista_artistas = []

    for numero in range(cantidad):
        print(f"\n--- Registro del artista {numero + 1} ---")
        print("1. Cantante")
        print("2. DJ")
        print("3. Banda")

        while True:
            tipo = input("Selecciona el tipo de artista (1-3): ").strip()
            if tipo in ("1", "2", "3"):
                break
            print("Opción no válida. Selecciona 1, 2 o 3.")

        nombre = solicitar_texto("Nombre: ")
        genero = solicitar_texto("Género musical: ")
        popularidad = solicitar_entero("Popularidad (1-100): ", 1, 100)

        if tipo == "1":
            cancion = solicitar_texto("Canción más popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)
        elif tipo == "2":
            estilo = solicitar_texto("Estilo del DJ: ")
            artista = DJ(nombre, genero, popularidad, estilo)
        else:
            integrantes = solicitar_entero("Número de integrantes: ", 1)
            artista = Banda(nombre, genero, popularidad, integrantes)

        lista_artistas.append(artista)
        print("Artista registrado correctamente.")

    iniciar_festival(lista_artistas)


if __name__ == "__main__":
    main()
