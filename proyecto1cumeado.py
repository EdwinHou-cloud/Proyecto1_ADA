from colorama import init, Fore, Back, Style

init()

def Presentacion():
    print("\n{:^70}".format("UNIVERSIDAD TECNOLÓGICA DE PANAMÁ"))
    print("{:^70}".format("FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES"))
    print("{:^70}".format("DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS"))
    print("{:^70}".format("PROYECTO #1"))
    print("{:^70}".format("Integrantes: Miguel Arosemana 8-1016-2330"))
    print("{:^78}".format("Edward Camaño 8-1010-515"))
    print("{:^80}".format("Diego Corrales 8-1001-1890"))
    print("{:^76}".format("Edwin Hou 8-1021-1916"))
    print("{:^76}".format("Josue Pino 8-1012-688\n\n"))

def mostrar_asientos(asientos):
    print("\nAsientos disponibles:")
    for i, fila in enumerate(asientos):
        print(f"{8 - i} | {' '.join(fila)}")

def Reserva():
    asientos = [[Back.GREEN + "[ ]" + Style.RESET_ALL for _ in range(9)] for _ in range(8)]
    total_asientos = 8 * 9  # Total de asientos disponibles
    entradas_reservadas = 0  # Contador de entradas reservadas

    while True:
        try:
            cantEntradas = int(input("\nIngrese la cantidad de entradas: "))
            if entradas_reservadas + cantEntradas > total_asientos:
                print(f"No se pueden reservar más de {total_asientos - entradas_reservadas} asientos.")
                continue
            
            cantAdultos = int(input("Ingrese la cantidad de adultos (18 años o más): "))
            cantNinos = int(input("Ingrese la cantidad de niños (14 años o menos): "))
            cantViejos = int(input("Ingrese la cantidad de adultos mayores (60 años o más): "))

            # Verificar que la cantidad de entradas sea igual a la suma de la cantidad de adultos, niños y adultos mayores
            if cantEntradas != (cantAdultos + cantNinos + cantViejos):
                print("La cantidad de entradas no coincide con la cantidad de adultos, niños y adultos mayores.")
                continue
            
            entradas_reservadas += cantEntradas  # Actualizar el contador de entradas reservadas
            break  # Salir del bucle si las entradas son correctas

        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

    print("\nELIJA UNA PELÍCULA\n")
    print("Películas\t\t\tHorarios\n1. Película1\t\t\t[13:00, 16:00, 19:00]\n2. Película2\t\t\t[13:00, 16:00, 19:00]\n3. Película3\t\t\t[13:00, 16:00, 19:00]")
    
    while True:
        try:
            codigoPelicula = int(input("\nIngrese el código de la película que desea ver: "))
            if codigoPelicula < 1 or codigoPelicula > 3:
                raise ValueError("Código de película no válido.")
            break  # Salir si el código es válido

        except ValueError as e:
            print(e)

    horaPelicula = input("Ingrese la hora en la que desea ver la película (formato HH:MM): ")

    # Crear una instancia de la clase Pelicula
    pelicula_seleccionada = None  # Inicializamos la variable con None
    if codigoPelicula == 1:
        pelicula_seleccionada = Pelicula("Interestellar", 169, 14, "Christopher Nolan")
    elif codigoPelicula == 2:
        pelicula_seleccionada = Pelicula("Película 2", 90, 18, "Director 2")
    elif codigoPelicula == 3:
        pelicula_seleccionada = Pelicula("Película 3", 135, 14, "Director 3")
    else:
        print("Código de película no válido")
        return

    # Crear una instancia de la clase Cine
    cine = Cine(pelicula_seleccionada, 10.0, horaPelicula)

    # Crear instancias de la clase Espectador
    espectadores = []
    for i in range(cantAdultos):
        espectadores.append(Espectador("Adulto {}".format(i + 1), 18, 100))
    for i in range(cantNinos):
        espectadores.append(Espectador("Niño {}".format(i + 1), 14, 50))
    for i in range(cantViejos):
        espectadores.append(Espectador("Adulto mayor {}".format(i + 1), 60, 80))

    for espectador in espectadores:
        if espectador.edad < pelicula_seleccionada.edad_minima:
            print("El espectador {} no tiene la edad mínima requerida para ver la película.".format(espectador.nombre))
            return

    while True:
        mostrar_asientos(asientos)
        while True:
            try:
                fila = int(input("Ingrese la fila del asiento (1-8): "))
                break
            except ValueError:
                print("Fila incorrecta, por favor ingrese un número válido.")
                mostrar_asientos(asientos)

        while True:
            columna = input("Ingrese la columna del asiento (A-I): ")
            if len(columna) != 1 or not columna.isalpha():
                print("Columna incorrecta, por favor ingrese una letra válida.")
                mostrar_asientos(asientos)
            else:
                break

        fila -= 1
        columna = ord(columna.upper()) - 65
        if fila < 0 or fila >= 8 or columna < 0 or columna >= 9:
            print("Fila o columna incorrecta, por favor ingrese un valor válido.")
            mostrar_asientos(asientos)
            continue
        if asientos[fila][columna] == Back.GREEN + "[ ]" + Style.RESET_ALL:
            asientos[fila][columna] = Back.RED + "[ ]" + Style.RESET_ALL
            print("Asiento seleccionado con éxito!")
        else:
            print("Asiento ocupado, seleccione otro.")
            continue
        
        while True:
            respuesta = input("¿Desea seleccionar otro asiento? (S/N): ")
            if respuesta.upper() == "S":
                break
            elif respuesta.upper() == "N":
                break
            else:
                print("Letra incorrecta, intente nuevamente")

        if respuesta.upper() == "N":
            break

    # Mostrar la reserva
    print("\nReserva realizada con éxito!")
    print("Película: {}".format(cine.pelicula.titulo))
    print("Hora: {}".format(cine.hora))
    print("Espectadores:")
    for espectador in espectadores:
        print("  - {}".format(espectador.nombre))
    print("Asientos seleccionados:")
    for i, fila in enumerate(asientos):
        print(f"{8 - i} | {' '.join(fila)}")
    print("Subtotal: ${}".format(cantEntradas * 10.0))
    print("Descuento: ${}".format(cantNinos * 5.0 + cantViejos * 2.0))
    print("Total: ${}".format(cantEntradas * 10.0 - (cantNinos * 5.0 + cantViejos * 2.0)))

class Pelicula:
    def __init__(self, titulo, duracion, edad_minima, director):
        self.titulo = titulo
        self.duracion = duracion
        self.edad_minima = edad_minima
        self.director = director

class Cine:
    def __init__(self, pelicula, precio, hora):
        self.pelicula = pelicula
        self.precio = precio
        self.hora = hora

class Espectador:
    def __init__(self, nombre, edad, cantidad_dinero):
        self.nombre = nombre
        self.edad = edad
        self.cantidad_dinero = cantidad_dinero

def menu():
    while True:
        print("\nBIENVENIDO USUARIO\nReservación de Boletos de Cine\n")
        print("0. Presentacion\n\n1. Reservar\n\n2. Confirmar Reserva\n\n3. Cancelar Reserva\n\n4. Salir\n")
        try:
            opcion = int(input("Seleccione una opción del menú: "))

            if opcion == 0:
                Presentacion()
            elif opcion == 1:
                Reserva()
            elif opcion == 2:
                print()
            elif opcion == 3:
                print()
            elif opcion == 4:
                print("Gracias por utilizar nuestro programa.")
                break
            else:
                # Mensaje de error si la opción seleccionada es inválida
                print("Opción no válida, por favor ingrese un número válido (1-4).")
        except ValueError:
            # Maneja errores si el usuario ingresa un valor no numérico
            print("Error: Por favor, ingrese un número válido.")

menu()