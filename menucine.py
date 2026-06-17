from funcionesReps import validar_opcion
def menuCine():
    '''Autor princiapl: Baltasar Silvera
    Función que muestra el menú principal del sistema y solicita al usuario que seleccione una opción.'''

    print("\n" + "=" * 70)
    print("Menú CINEVERSE".center(70))
    print("=" * 70)

    

    
    print("1. Alta de pelicula")
    print("2. Eliminar película")
    print("3. Modificar película")
    print("4. Informe general")
    print("5. Salir")

    return validar_opcion(1, 5, "Seleccione una opcion: ")