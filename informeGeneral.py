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

    for i in range(len(peliculas)):
        for j in range(i+1,len(peliculas)):
            if peliculas[i][4] < peliculas[j][4]:
                aux = peliculas[i]
                peliculas[i] = peliculas[j]
                peliculas[j] = aux
                
            elif peliculas[i][4] == peliculas [j][4]:
                if peliculas[i][0] > peliculas[j][0]:
                    aux = peliculas[i]
                    peliculas[i] = peliculas[j]
                    peliculas[j] = aux
    return peliculas

def mostrar_informe(peliculas):
    '''Muestra el informe con todos los datos de las películas en reporte matricial.'''   
    print("\n" + "=" * 130)
    print(f"{'TITULO':20}{'GENERO':20}{'DURACION':12}{'SALA':8}{'ENTRADAS':12}{'PRECIO':12}{'ESTADO':20}")
    print("=" * 130)

    for pelicula in peliculas:
        print(f"{pelicula[0]:20}{pelicula[1]:20}{pelicula[2]:5}{pelicula[3]:8}{pelicula[4]:12}{pelicula[5]:12}\t{pelicula[6]:25}")