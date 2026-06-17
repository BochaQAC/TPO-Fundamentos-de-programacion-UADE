from funcionesReps import hay_peliculas_registradas, buscar_pelicula_por_titulo

def eliminarPelicula(peliculas):
    '''Autor princiapl: Gennaro Nicolas Pocetti
    Función que permite eliminar una película 'finalizada' del sistema, solicitando al usuario el título de la película a eliminar.'''
    
    if hay_peliculas_registradas(peliculas):
        titulo = input("Ingrese el título de la película finalizada a eliminar: ")
        indice = buscar_pelicula_por_titulo(peliculas, titulo)

        if indice == -1:
            print("La película no existe.")
        elif peliculas[indice][6] != "Finalizada":
            print("La película no se encuentra finalizada, no se puede eliminar.")
        else:
            peliculas.pop(indice)
            print("Película eliminada correctamente.")
    else:
        print("No hay películas registradas.")