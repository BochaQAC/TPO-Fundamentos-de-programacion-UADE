from funcionesReps import hay_peliculas_registradas, buscar_pelicula_por_titulo, validar_opcion, validar_numero_positivo, validar_precio, mostrar_lista_opciones, validar_string_no_vacio
def modificarPelicula(peliculas):
    '''Autor princiapl: Alan Roberto Bernard
    Función que permite modificar los datos de una película registrada en el sistema, solicitando al usuario el título de la película a modificar y los nuevos datos.'''

    if hay_peliculas_registradas(peliculas):
        print(f"\nPelículas registradas: {len(peliculas)}")
        
        titulo = validar_string_no_vacio("Ingrese el título de la película a modificar: ")
        indice = buscar_pelicula_por_titulo(peliculas, titulo)
        
        if indice != -1:
            # Mostrar opciones de modificación
            print("\n¿Qué desea modificar?")
            print("1. Género")
            print("2. Duración")
            print("3. Sala")
            print("4. Precio")
            print("5. Estado")

            opcion = validar_opcion(1, 5)
            
            if opcion == 1:
                modificar_genero(peliculas, indice)
            elif opcion == 2:
                modificar_duracion(peliculas, indice)
            elif opcion == 3:
                modificar_sala(peliculas, indice)
            elif opcion == 4:
                modificar_precio(peliculas, indice)
            elif opcion == 5:
                modificar_estado(peliculas, indice)
        else:
            print("La película no existe.")
    else:
        print("No hay películas registradas.")

def modificar_genero(peliculas, indice):
    generosDisponibles = ["Accion","Aventura","Comedia","Drama","Ciencia Ficcion","Terror","Animacion","Documental"]
    mostrar_lista_opciones(generosDisponibles, "Géneros disponibles")
    opGenero = validar_opcion(1, len(generosDisponibles), "Seleccione un genero: ")
    peliculas[indice][1] = generosDisponibles[opGenero - 1]
    print("Género modificado correctamente.")

def modificar_duracion(peliculas, indice):
    duracion = validar_numero_positivo("Ingrese la nueva duración en minutos: ")
    peliculas[indice][2] = duracion
    print("Duración modificada correctamente.")

def modificar_sala(peliculas, indice):
    sala = validar_numero_positivo("Ingrese el nuevo numero de sala: ")
    peliculas[indice][3] = sala
    print("Sala modificada correctamente.")

def modificar_precio(peliculas, indice):
    precio = validar_precio("Ingrese el nuevo valor promedio de la entrada: ")
    peliculas[indice][5] = precio
    print("Precio modificado correctamente.")

def modificar_estado(peliculas, indice):
    estadosDisponibles = ["En cartelera","Proximo estreno","Funcion especial","Finalizada"]
    mostrar_lista_opciones(estadosDisponibles, "Estados disponibles")
    opEstado = validar_opcion(1, len(estadosDisponibles), "Seleccione estado: ")
    peliculas[indice][6] = estadosDisponibles[opEstado - 1]
    print("Estado modificado correctamente.")