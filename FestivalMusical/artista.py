class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}. Mi género musical es {self.genero} "
              f"y mi popularidad es {self.popularidad}/100.")

    def actuar(self):
        print(f"{self.nombre} está realizando su presentación.")

    def despedirse(self):
        print(f"Gracias por acompañarnos. ¡Hasta pronto! Atentamente, {self.nombre}.")
