def modificarPelicula(peliculas):
    if len(peliculas) == 0:
        print("No hay películas registradas.")
        return
    
    print(f"\nPelículas registradas: {len(peliculas)}")
    
    titulo = input("Ingrese el título de la película a modificar: ")
    indice = -1
    
    for i in range(len(peliculas)):
        if peliculas[i][0].lower() == titulo.lower():
            indice = i
    
    if indice == -1:
        print("La película no existe.")
        return
    
    print("\n¿Qué desea modificar?")
    print("1. Género")
    print("2. Duración")
    print("3. Sala")
    print("4. Precio")
    print("5. Estado")

    opcion = int(input("Seleccione una opción: "))
   
    while opcion < 1 or opcion > 5:
        opcion = int(input("Opción inválida. Seleccione una opción válida: "))
        
    if opcion == 1:
        generosDisponibles = ["Accion","Aventura","Comedia","Drama","Ciencia Ficcion","Terror","Animacion","Documental"]
        #print(f"\nGéneros disponibles: {generosDisponibles}") 

        for i in range(len(generosDisponibles)):
            print(i + 1, "-", generosDisponibles[i])
        
        opGenero = int(input("Seleccione un genero del 1 al 8: "))
        while opGenero < 1 or opGenero > len(generosDisponibles):
            opGenero = int(input("Error. Seleccione un genero válido: "))
        peliculas[indice][1] = generosDisponibles[opGenero - 1]

        print("Género modificado correctamente.")
        
    elif opcion == 2:
        duracion = int(input("Ingrese la nueva duración en minutos: "))

        while duracion <= 0:
            duracion = int(input("Error. Ingrese la duración nuevamente: "))
        peliculas[indice][2] = duracion
        
        print("Duración modificada correctamente.")
        
    elif opcion == 3:
        sala = int(input("Ingrese el nuevo numero de sala: "))

        while sala <= 0:
            sala = int(input("Error. Ingrese un numero de sala: "))
        peliculas[indice][3] = sala
        
        print("Sala modificada correctamente.")
        
    elif opcion == 4:
        precio = float(input("Ingrese el nuevo valor promedio de la entrada: "))
    
        while precio < 0:
            precio = float(input("Error. Ingrese valor promedio de la entrada: "))

        peliculas[indice][5] = precio

        print("Precio modificado correctamente.")

    elif opcion == 5:
        estadosDisponibles = ["En cartelera","Proximo estreno","Funcion especial","Finalizada"]
            
        #print(f"\nEstados disponibles: {estadosDisponibles}") 

        for i in range(len(estadosDisponibles)):
            print(i + 1, "-", estadosDisponibles[i])
        
        opEstado = int(input("Seleccione estado del 1 al 4: "))
            
        while opEstado < 1 or opEstado > len(estadosDisponibles):
            opEstado = int(input("Error. Seleccione un estado válido: "))



        peliculas[indice][6] = estadosDisponibles[opEstado - 1]    

        print("Estado modificado correctamente.")