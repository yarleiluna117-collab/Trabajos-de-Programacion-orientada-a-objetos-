# Festival Musical

**Alumno:** Yarlei Aldahir Luna Dimas  
**Materia:** Fundamentos de Programación  
**Actividad:** Herencia y polimorfismo - Festival musical  
**Institución:** Instituto Tecnológico de Aguascalientes

## Descripción
Programa en Python que simula un festival musical con tres tipos de artistas: cantante, DJ y banda. Se aplican clases, constructores, herencia y polimorfismo.

## Archivos
- `artista.py`: clase base.
- `cantante.py`: subclase Cantante.
- `dj.py`: subclase DJ.
- `banda.py`: subclase Banda.
- `festival.py`: función que recorre la lista y ejecuta los métodos de cada artista.
- `main.py`: captura los datos y crea los objetos.

## Requisitos
Python 3.10 o superior. No requiere instalar librerías externas.

## Ejecución
Abre la carpeta del proyecto en PyCharm o VS Code y ejecuta:

```bash
python main.py
```

## Conceptos aplicados
- **Constructores:** inicializan los atributos de cada objeto.
- **Herencia:** `Cantante`, `DJ` y `Banda` heredan de `Artista`.
- **Sobrescritura:** cada subclase redefine `actuar()`.
- **Polimorfismo:** `iniciar_festival()` llama a `actuar()` sin preguntar qué tipo de artista recibe.
