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
        print(f"{i+1} | {' '.join(fila)}")
    print("     A   B   C   D   E   F   G   H   I")  # Agregar encabezado de columnas

def calcular_precio(edad):
    if edad >= 60:  # Tercera edad
        return 2.25
    elif edad <= 12:  # Niños
        return 3.50
    else:  # Adultos
        return 6.25

def Reserva():
    try:
        while True:
            cantEntradas = int(input("\nIngrese la cantidad de entradas: "))
            cantAdultos = int(input("Ingrese la cantidad de adultos (18 años o mas): "))
            cantNinos = int(input("Ingrese la cantidad de niños (14 años o menos): "))
            cantViejos = int(input("Ingrese la cantidad de Adultos mayores (60 años o mas): "))
                    # Verificar que la cantidad de entradas sea igual a la suma de la cantidad de adultos, niños y adultos mayores
            if cantEntradas != cantAdultos + cantNinos + cantViejos:
                print("La cantidad de entradas no coincide con la cantidad de adultos, niños y adultos mayores. Por favor, ingrese la cantidad correcta.")
            else:
                break
        
        print("\nELIJA UNA PELICULA\n")
        print("Peliculas\t\t\tHorarios\n1. Interestellar\t\t[13:00, 16:00, 19:00, 11:00]\n2. Avatar\t\t\t[13:00, 16:00, 19:00, 11:00]\n3. SAW\t\t\t\t[13:00, 16:00, 19:00, 11:00]")
        codigoPelicula = int(input("\nIngrese la pelicula que desea ver (1-3): "))
        horaPelicula = input("Ingrese la hora en la que desea ver la pelicula: ")

        # Crear una instancia de la clase Pelicula
        pelicula_seleccionada = None #Inicializamos la variable con None
        if codigoPelicula == 1:
            pelicula_seleccionada = Pelicula("Interestellar", 169, 14, "Christopher Nolan")
        elif codigoPelicula == 2:
            pelicula_seleccionada = Pelicula("Avatar", 90, 14, "James Cameron")
        elif codigoPelicula == 3:
            pelicula_seleccionada = Pelicula("SAW", 135, 18, "Darren Lynn Bousman")
        else:
            print("Código de película no válido")
            return

        # Crear una instancia de la clase Cine
        cine = Cine(pelicula_seleccionada, 10.0, horaPelicula)

        # Crear instancias de la clase Espectador
        espectadores = []
        for i in range(cantAdultos):
            espectadores.append(Espectador("Adulto {}".format(i+1), 18, 100))  
        for i in range(cantNinos):
            espectadores.append(Espectador("Niño {}".format(i+1), 14, 50))  
        for i in range(cantViejos):
            espectadores.append(Espectador("Adulto mayor {}".format(i+1), 60, 80))  

        for espectador in espectadores:
            if espectador.edad < pelicula_seleccionada.edad_minima:
                print("El espectador {} no tiene la edad mínima requerida para ver la película.".format(espectador.nombre))
                return
            
        asientos = [[Back.GREEN+"[ ]"+ Style.RESET_ALL for _ in range(9)] for _ in range(8)]
        while True:
            mostrar_asientos(asientos)
            for i in range(cantEntradas):
                while True:
                    try:
                        while True:
                            print(f"Reservacion para asiento de la entrada N°{i+1}")
                            fila = int(input("Ingrese la fila del asiento (1-8): "))
                            if fila < 1 or fila > 8:  # Validamos que esté entre 1 y 8
                                print("Fila incorrecta, por favor ingrese un número válido.")
                                mostrar_asientos(asientos)
                                continue
                            break
                    except ValueError:
                        print("Fila incorrecta, por favor ingrese un número válido.")
                        mostrar_asientos(asientos)
                        continue
                    while True:
                        columna = input("Ingrese la columna del asiento (A-I): ").upper()
                        if not 'A' <= columna <= 'I':
                            print("Columna incorrecta, por favor ingrese una letra válida.")
                            mostrar_asientos(asientos)
                            continue
                        else:
                            break
                    fila -= 1
                    columna = ord(columna.upper()) - 65
                    if fila < 0 or fila >= 8 or columna < 0 or columna >= 9:
                        print("Fila o columna incorrecta, por favor ingrese un valor válido.")
                        mostrar_asientos(asientos)
                        continue
                    if asientos[fila][columna] == Back.GREEN+"[ ]"+ Style.RESET_ALL:
                        asientos[fila][columna] = Back.RED+"[ ]"+ Style.RESET_ALL
                        print("Asiento seleccionado con éxito!\n")
                        mostrar_asientos(asientos)
                        break
                    else:
                        print("Asiento ocupado, seleccione otro.")
                        mostrar_asientos(asientos)
            break
                    
        # Mostrar la reserva
        print("\n!Su Reserva se ha realizado con éxito!\n")
        print("Película: {}".format(cine.pelicula.titulo))
        print("Hora: {}".format(cine.hora))
        print("Espectadores:")
        for espectador in espectadores:
            print("  - {}".format(espectador.nombre))
        print("Sus asientos seleccionados:")
        for i, fila in enumerate(asientos):
            print(f"{1 + i} | {' '.join(fila)}")
        print("     A   B   C   D   E   F   G   H   I")  # Agregar encabezado de columnas    
        # Calcular el total a pagar
        total = 0
        tipo_descuento = []  
        for espectador in espectadores:
            precio = calcular_precio(espectador.edad)
            total += precio
            

        # Mostrar el resumen
        print(f"Total: ${total:.2f}")

        
        #CONFIRMAR RESERVA
        """
         # Aplicar descuentos
        descuento = 0

        if total > 30:
            descuento = total * 0.10
            tipo_descuento.append("10% por gastar más de $30")
        elif 25 <= total <= 30:
            descuento = total * 0.05
            tipo_descuento.append("5% por gastar entre $25 y $30")

        if int(cine.hora.split(":")[0]) >= 21:  # Si la película es después de las 9 PM
            descuento += total * 0.15
            tipo_descuento.append("15% por función después de las 9 PM")

        total_final = total - descuento
        mostrar_asientos(asientos)
        print(f"Subtotal: ${total:.2f}")
        print(f"Descuento: ${descuento:.2f}") 
        if tipo_descuento:
            print("Tipos de descuentos aplicados:")
            for tipo in tipo_descuento:
                print(f" - {tipo}")
            print(f"Total: ${total_final:.2f}")
        """
        
    except ValueError:
        print("Ha ocurrido un error, intente nuevamente")

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
    
        def __str__(self):
            return f"{self.nombre}, Edad: {self.edad}, Dinero: ${self.cantidad_dinero:.2f}"
        
def menu():
    while True:
        print("\nBIENVENIDO USUARIO\nReservación de Boletos de Cine\n")
        print("0. Presentacion\n\n1. Reservar\n\n2. Confirmar Reserva\n\n3. Cancelar Reserva\n\n4. Salir\n")
        try:
            opcion = int(input("Seleccione una opcion del menu: "))

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

#validacion de edad
#validar hora
#validar cantidad de entradas (if cantidad de entradas)