import random
from funcionesReps import validar_opcion, validar_string_no_vacio, validar_numero_positivo, validar_precio, buscar_pelicula_por_titulo, mostrar_lista_opciones
def altaDePelicula(peliculas):
    '''Autor princiapl: Felipe Antelo
    Función que permite registrar una película en el sistema, solicitando al usuario los datos necesarios.'''
    
    generosDisponibles = ["Accion","Aventura","Comedia","Drama","Ciencia Ficcion","Terror","Animacion","Documental"]

    estadosDisponibles = ["En cartelera","Proximo estreno","Funcion especial","Finalizada"]

    print("\n" + "=" * 70)
    print("ALTA DE PELÍCULA".center(70))
    print("=" * 70)

    # Ingresar Título con validación de título único
    titulo = validar_string_no_vacio("Ingresar el titulo de la película: ")
    while buscar_pelicula_por_titulo(peliculas, titulo) != -1:  # ← Usamos while sin return
        titulo = input("El título ya existe. Ingrese un título diferente: ")

    # Ingresar Género
    mostrar_lista_opciones(generosDisponibles, "Géneros disponibles")
    opGenero = validar_opcion(1, len(generosDisponibles), "Seleccione un genero: ")
    genero = generosDisponibles[opGenero - 1]

    # Ingresar Duración
    duracion = validar_numero_positivo("Ingrese la duracion en minutos: ")

    # Ingresar Estado
    mostrar_lista_opciones(estadosDisponibles, "Estados disponibles")
    opEstado = validar_opcion(1, len(estadosDisponibles), "Seleccione estado: ")
    estado = estadosDisponibles[opEstado - 1]
    
    # Ingresar Sala
    sala = validar_numero_positivo("Ingrese numero de sala: ")

    # Ingresar Precio
    precio = validar_precio()
    
    # Entradas vendidas aleatorias 
    entradas = random.randint(0,500)
    print(f"Entradas vendidas: {entradas}")

    pelicula = [titulo, genero, duracion, sala, entradas, precio, estado]
    peliculas.append(pelicula)
    
    print("\nPelícula registrada correctamente")