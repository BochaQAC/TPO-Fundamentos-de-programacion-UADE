'''Funciones de respaldo y reutilizadas'''

def validar_opcion(minimo, maximo, mensaje="Seleccione una opción: "):
    
    '''Valida que la opción ingresada esté dentro del rango permitido'''
    opcion = input(mensaje)
    
    # Validar que sea un número
    while not opcion.isdigit():
        print(f"Opción inválida. Seleccione una opción válida entre {minimo} y {maximo}.")
        opcion = input(mensaje)
    
    opcion = int(opcion)
    
    # Validar que esté en el rango
    while opcion < minimo or opcion > maximo:
        print(f"Error. Seleccione una opción entre {minimo} y {maximo}.")
        opcion = input(mensaje)
        
        # Validar nuevamente que sea número
        while not opcion.isdigit():
            print(f"Opción inválida. Seleccione una opción válida entre {minimo} y {maximo}.")
            opcion = input(mensaje)
        
        opcion = int(opcion)
    
    return opcion


def validar_string_no_vacio(mensaje, mensaje_error="El campo no puede estar vacío."):
    '''Valida que el string ingresado no esté vacío'''
    valor = input(mensaje)
    while valor == "":
        print(mensaje_error)
        valor = input(mensaje)
    return valor

def validar_numero_positivo(mensaje, mensaje_error="Error. Ingrese un valor positivo: "):
    '''Valida que el número ingresado sea positivo'''
    valor = input(mensaje)
    
    while not valor.isdigit() or int(valor) <= 0:
        print(mensaje_error)
        valor = input(mensaje)

    valor = int(valor)
    return valor

def validar_precio(mensaje="Ingrese valor promedio de la entrada: "):
    '''Valida que el precio ingresado no sea negativo'''
    precio = float(input(mensaje))
    while precio <= 0:
        precio = float(input("Error. Ingrese un precio válido: "))
    return precio

def buscar_pelicula_por_titulo(peliculas, titulo):
    '''Busca una película por su título (ignorando mayúsculas/minúsculas)'''
    for i in range(len(peliculas)):
        if peliculas[i][0].lower() == titulo.lower():
            return i   
    return -1

def hay_peliculas_registradas(peliculas):
    '''Verifica si hay películas registradas'''
    return len(peliculas) > 0

def mostrar_lista_opciones(lista, mensaje_titulo):
    '''Muestra una lista de opciones numeradas'''
    print(f"\n{mensaje_titulo}:")
    for i in range(len(lista)):
        print(f"{i + 1} - {lista[i]}")                 
