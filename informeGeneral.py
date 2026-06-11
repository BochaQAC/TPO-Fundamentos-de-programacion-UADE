def informeGeneral(peliculas):
    '''Autor princiapl: Bautista Miano Gaibisso
    Función que muestra un informe general de las películas registradas en el sistema, ordenadas por cantidad de entradas vendidas de forma descendente. En caso de empate, se ordenan alfabéticamente por título.'''

    if len(peliculas) == 0:
        print("No hay películas registradas.")
        return

    print("\n" + "=" * 70)
    print("INFORME GENERAL DE PELÍCULAS".center(70))
    print("=" * 70)

    n = len(peliculas)

    # Metodo Selección
    for i in range(0,len(peliculas)-1):
        for j in range( i + 1, len(peliculas)):
            if peliculas[i][4] < peliculas [j][4] or ( peliculas [i][4] == peliculas [j][4] and peliculas[i][0] > peliculas[j][0]):
                aux = peliculas [i]
                peliculas [i] = peliculas [j]
                peliculas[j] = aux

    print("\n" + "=" * 130)
    print(f"{'TITULO':20}{'GENERO':20}{'DURACION':12}{'SALA':8}{'ENTRADAS':12}{'PRECIO':12}{'ESTADO':20}")
    print("=" * 130)

    for i in range(len(peliculas)):
        print(f"{peliculas[i][0]:20}{peliculas[i][1]:20}{peliculas[i][2]:5}{peliculas[i][3]:8}{peliculas[i][4]:12}{peliculas[i][5]:12}{peliculas[i][6]:25}")
            