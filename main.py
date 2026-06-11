import informeGeneral, altaDePelicula, eliminarPelicula, modificarPelicula, menucine, random 

opcion = 0

peliculas = [] 



while opcion != 5:

    opcion = menucine.menuCine()

    if opcion == 1:
        altaDePelicula.altaDePelicula(peliculas)
      

    elif opcion == 2:
        eliminarPelicula.eliminarPelicula(peliculas)
        

    elif opcion == 3:
        modificarPelicula.modificarPelicula(peliculas)
        

    elif opcion == 4:
        informeGeneral.informeGeneral(peliculas)
        

    else:
        print("Operación finalizada. ¡Gracias por usar CINEVERSE!")

