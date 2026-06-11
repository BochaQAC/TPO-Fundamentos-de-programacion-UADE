def eliminarPelicula(peliculas):
    '''Autor princiapl: Gennaro Nicolas Pocetti
    Función que permite eliminar una película 'finalizada' del sistema, solicitando al usuario el título de la película a eliminar.'''
    
    if len(peliculas) == 0:
        print("No hay películas registradas.")
        return
    
    titulo = input("Ingrese el título de la película finalizada a eliminar: ")

    indice = -1

    for i in range(len(peliculas)):
        if peliculas[i][0].lower() == titulo.lower():
            indice = i
            
    if indice == -1:
        print("La película no existe.")
   
    elif peliculas[indice][6] != "Finalizada":
        print("La película no se encuentra finalizada, no se puede eliminar.")
        
    elif peliculas[indice][6] == "Finalizada":    
        peliculas.pop(indice)
        print("Película eliminada correctamente.")