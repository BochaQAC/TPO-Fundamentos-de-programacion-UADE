def menuCine():
    print("\n" + "=" * 70)
    print("Menú CINEVERSE".center(70))
    print("=" * 70)

    

    
    print("1. Alta de pelicula")
    print("2. Eliminar película")
    print("3. Modificar película")
    print("4. Informe general")
    print("5. Salir")

    opcion = int(input("Seleccione una opcion: "))
    #if opcion != int:
        #print("Error. Ingrese un número válido.")
        #opcion = int(input("Seleccione una opcion: "))

    while opcion < 1 or opcion > 5:
        opcion = int(input("Opción inválida. Seleccione una opción válida: "))
    
    return opcion