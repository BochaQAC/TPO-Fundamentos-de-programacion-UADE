from funcionesReps import hay_peliculas_registradas 
def informeGeneral(peliculas):
    '''Autor princiapl: Bautista Miano Gaibisso
    Función que muestra un informe general de las películas registradas en el sistema, ordenadas por cantidad de entradas vendidas de forma descendente. En caso de empate, se ordenan alfabéticamente por título.'''

    if hay_peliculas_registradas(peliculas):
        print("\n" + "=" * 70)
        print("INFORME GENERAL DE PELÍCULAS".center(70))
        print("=" * 70)

        ordenar_peliculas_por_seleccion(peliculas)
        
        mostrar_informe(peliculas)

    else:
        print("No hay películas registradas.")    

def ordenar_peliculas_por_seleccion(peliculas):
    '''Ordena las películas usando el MÉTODO DE SELECCIÓN'''

    n = len(peliculas)

    # Metodo Selección
    for i in range(n - 1):
        pos_max = i
        for j in range(i + 1, n):
            # Si la película en j tiene MÁS entradas que la que está en pos_max
            if peliculas[j][4] > peliculas[pos_max][4]:
                pos_max = j
                # Si tienen igual cantidad de entradas, ordenar alfabéticamente
            elif peliculas[j][4] == peliculas[pos_max][4]:
                # Orden ascendente (A-Z) por título
                if peliculas[j][0] < peliculas[pos_max][0]:
                    pos_max = j
        # Intercambiar la película en pos_max con la película en i
        if pos_max != i:
            peliculas[i], peliculas[pos_max] = peliculas[pos_max], peliculas[i]    

def mostrar_informe(peliculas):
    '''Muestra el informe con todos los datos de las películas en reporte matricial.'''   
    print("\n" + "=" * 130)
    print(f"{'TITULO':20}{'GENERO':20}{'DURACION':12}{'SALA':8}{'ENTRADAS':12}{'PRECIO':12}{'ESTADO':20}")
    print("=" * 130)

    for pelicula in peliculas:
        print(f"{pelicula[0]:20}{pelicula[1]:20}{pelicula[2]:5}{pelicula[3]:8}{pelicula[4]:12}{pelicula[5]:12}\t{pelicula[6]:25}")