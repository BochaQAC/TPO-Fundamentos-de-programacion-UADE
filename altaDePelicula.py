import random
def altaDePelicula(peliculas):
    #aaaa
    generosDisponibles = ["Accion","Aventura","Comedia","Drama","Ciencia Ficcion","Terror","Animacion","Documental"]

    estadosDisponibles = ["En cartelera","Proximo estreno","Funcion especial","Finalizada"]

    print("\n" + "=" * 70)
    print("ALTA DE PELÍCULA".center(70))
    print("=" * 70)

    # Ingresar Titulo

    titulo = input("Ingresar el titulo de la película: ")

    
    while titulo == "" :
        print("El título no puede estar vacío.")
        titulo = input("Ingresar el titulo de la película: ")
    
    existe = True
    
    while existe:
        existe = False
    
        for i in range(len(peliculas)):
            if peliculas[i][0].lower() == titulo.lower():
                existe = True
    
        if existe:
            titulo = input("El título ya existe. Ingrese un título diferente: ")


    # Ingresar Genero
    print("\nGéneros disponibles:")
    for i in range(len(generosDisponibles)):
        print(i + 1, "-", generosDisponibles[i])

    opGenero = int(input("Seleccione un genero: "))
    while opGenero < 1 or opGenero > 8:
        opGenero = int(input("Error. Seleccione un genero válido: "))
    genero = generosDisponibles[opGenero - 1]

    # Ingresar Duración
    duracion = int(input("Ingrese la duracion en minutos: "))
    while duracion <= 0:
        duracion = int(input("Error. Ingrese la duración nuevamente: "))
    
    # Ingresar Estado
    print("\nEstados:")
    for i in range(len(estadosDisponibles)):
        print(i + 1, "-", estadosDisponibles[i])

    opEstado = int(input("Seleccione estado: "))
    estado = estadosDisponibles[opEstado - 1]
    
    #if estado == "Finalizada":
       # print("La película se encuentra finalizada, no se registrará en el sistema.")
        #return peliculas 
    #la idea seria que si la pelicula esta finalizada, no se registre directamente, siendo ya eliminada. Como la consigna no indica eso, lo dejo comentado.
    
    # Ingresar Sala
    sala = int(input("Ingrese numero de sala: "))
    while sala <= 0:
        sala = int(input("Error. Ingrese un numero de sala: "))

    # Ingresar Precio promedio
    precio = float(input("Ingrese valor promedio de la entrada: "))
    while precio < 0:
        precio = float(input("Error. Ingrese valor promedio de la entrada: "))
    
    # Entradas vendidas aleatorias 
    entradas = random.randint(0,500)
    print("Entradas vendidas: ",entradas)
    
    

    

    pelicula = [titulo, genero, duracion, sala, entradas, precio, estado]

   
    peliculas.append(pelicula)
    
    print("\nPelícula registrada correctamente")