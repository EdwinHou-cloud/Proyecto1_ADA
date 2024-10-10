from colorama import init, Fore, Back, Style
init()

# Diccionario para almacenar las reservas previas
reservas_previas = {}

def Presentacion():
    print("\n{:^70}".format("UNIVERSIDAD TECNOLÓGICA DE PANAMÁ"))
    print("{:^70}".format("FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES"))
    print("{:^70}".format("DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS"))
    print("{:^70}".format("PROYECTO #1"))
    print("{:^70}".format("Integrantes: Miguel Arosemana 8-1016-2330"))
    print("{:^78}".format("Edward Camaño 8-1010-515"))
    print("{:^80}".format("Diego Corrales 8-1001-1890"))
    print("{:^76}".format("Edwin Hou 8-1021-1916"))
    print("{:^76}".format(" Josue Pino 8-1012-688\n\n"))

def mostrar_asientos(asientos):
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
class Reserva:
    def __init__(self, pelicula, hora, asientos, espectadores, total, confirmada=False):
        self.pelicula = pelicula
        self.hora = hora
        self.asientos = asientos
        self.espectadores = espectadores
        self.total = total
        self.confirmada = confirmada

    def __str__(self):
        return f"Reserva de {self.pelicula.titulo} a las {self.hora} con {len(self.asientos)} asientos y un total de ${self.total:.2f}"
def ConfirmarReserva(reserva):
    reserva.confirmada = True
    print("\n¡Reserva confirmada con éxito!\n")
    print(reserva)

def CancelarReserva(reserva):
    reserva.confirmada = False
    print("\n¡Reserva cancelada con éxito!\n")
    print(reserva)
    
reservas_realizadas = []
def Realizar_reserva():
    global pelicula_seleccionada, espectadores, asientos, total, cine, horaPelicula, reserva_confirmada
    reserva_confirmada = False
    pelicula_seleccionada = None
    espectadores = []
    asientos = [[Back.GREEN + "[ ]" + Style.RESET_ALL for _ in range(9)] for _ in range(8)]
    total = 0
    cine = None
    horaPelicula = None
    
    while True:
        try:
            cantEntradas = int(input("\nIngrese la cantidad de entradas: "))
            if cantEntradas <= 0:
                print("La cantidad de entradas debe ser mayor que 0.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

    while True:
        try:
            cantAdultos = int(input("Ingrese la cantidad de adultos (12 años o más): "))
            if cantAdultos < 0:
                print("La cantidad de adultos no puede ser negativa.")
                continue
            elif cantAdultos > cantEntradas:
                print("La cantidad de adultos no puede ser mayor que la cantidad de entradas.")
                continue
            cantNinos = int(input("Ingrese la cantidad de niños (12 años o menos): "))
            if cantNinos < 0:
                print("La cantidad de niños no puede ser negativa.")
                continue
            elif cantNinos + cantAdultos > cantEntradas:
                print("La cantidad de niños y adultos no puede ser mayor que la cantidad de entradas.")
                continue
            cantViejos = int(input("Ingrese la cantidad de adultos mayores (60 años o más): "))
            if cantViejos < 0:
                print("La cantidad de adultos mayores no puede ser negativa.")
                continue
            elif cantViejos + cantAdultos + cantNinos != cantEntradas:
                if cantViejos + cantAdultos + cantNinos > cantEntradas:
                    print("La cantidad de adultos mayores, adultos y niños no puede ser mayor que la cantidad de entradas.")
                else:
                    print("La cantidad de adultos mayores, adultos y niños debe ser igual a la cantidad de entradas.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
            
    if cantAdultos + cantNinos + cantViejos == cantEntradas:
        espectadores = []
        for i in range(cantAdultos):
            espectadores.append(Espectador(f"Adulto {i + 1}", 18, 100))
        for i in range(cantNinos):
            espectadores.append(Espectador(f"Niño {i + 1}", 12, 50))
        for i in range(cantViejos):
            espectadores.append(Espectador(f"Adulto mayor {i + 1}", 60, 80))

        while True:
            print("ELIJA UNA PELICULA")
            print("Películas                       Horarios")
            print("1. Interestellar                [13:00, 16:00, 19:00, 22:00]")
            print("2. Avatar                       [13:00, 16:00, 19:00, 22:00]")
            print("3. SAW                          [13:00, 16:00, 19:00, 22:00]")

            while True:
                try:
                    codigoPelicula = int(input("Ingrese el número de la película que desea ver (1-3): "))
                    if codigoPelicula not in [1, 2, 3]:
                        print("Selección inválida. Intente nuevamente.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

            while True:
                horaPelicula = input("Ingrese la hora en la que desea ver la película: ")
                if horaPelicula not in ["13:00", "16:00", "19:00", "22:00"]:
                    print("Hora inválida. Intente nuevamente.")
                else:
                    break

            pelicula_seleccionada = None
            if codigoPelicula == 1:
                pelicula_seleccionada = Pelicula("Interestellar", 169, 12, "Christopher Nolan")
            elif codigoPelicula == 2:
                pelicula_seleccionada = Pelicula("Avatar", 90, 12, "James Cameron")
            elif codigoPelicula == 3:
                pelicula_seleccionada = Pelicula("SAW", 135, 18, "James Wan")

            print(f"\nPelícula: {pelicula_seleccionada.titulo}")
            print(f"Duración: {pelicula_seleccionada.duracion} minutos")
            print(f"Edad mínima para ver la película: {pelicula_seleccionada.edad_minima} años")
            print(f"Director: {pelicula_seleccionada.director}")

            # Verificar si algún espectador no cumple con la edad mínima de la película seleccionada
            espectadores_invalidos = [espectador for espectador in espectadores if espectador.edad < pelicula_seleccionada.edad_minima]
            if espectadores_invalidos:
                print(f"\nAlgunos espectadores no cumplen con la edad mínima para ver {pelicula_seleccionada.titulo}:")
                for espectador in espectadores_invalidos:
                    print(f" - {espectador.nombre} (Edad: {espectador.edad})")
                print("Por favor, seleccione una película diferente.")
                continue  # Repetir la selección de la película si hay espectadores inválidos
            else:
                break  # Salir del ciclo si todos los espectadores son válidos para la película


        espectadores = []
        for i in range(cantAdultos):
            espectadores.append(Espectador(f"Adulto {i + 1}", 18, 100))
        for i in range(cantNinos):
            espectadores.append(Espectador(f"Niño {i + 1}", 12, 50))
        for i in range(cantViejos):
            espectadores.append(Espectador(f"Adulto mayor {i + 1}", 60, 80))
                
        else:
            # Verificar si ya existen reservas para esa película y esa hora
            clave_reserva = (pelicula_seleccionada.titulo, horaPelicula)
            if clave_reserva in reservas_previas:
                asientos = reservas_previas[clave_reserva]
                print("\nCargando asientos previamente reservados...")
                cine = Cine(pelicula_seleccionada, 10.0, horaPelicula)
            else:
                asientos = [[Back.GREEN + "[ ]" + Style.RESET_ALL for _ in range(9)] for _ in range(8)]
                cine = Cine(pelicula_seleccionada, 10.0, horaPelicula)

        while True:
            print("\nAsientos disponibles:")
            mostrar_asientos(asientos)
            asientos_seleccionados = []
            for i in range(cantEntradas):
                while True:
                    try:
                        while True:
                            print(f"Reservación para asiento de la entrada N°{i + 1}")
                            fila = int(input("Ingrese la fila del asiento (1-8): "))
                            if fila < 1 or fila > 8:
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
                        if len(columna) != 1:
                            print("Por favor, ingrese solo una letra.")
                            mostrar_asientos(asientos)
                            continue
                        elif not 'A' <= columna <= 'I':
                            print("Columna incorrecta, por favor ingrese una letra válida.")
                            mostrar_asientos(asientos)
                            continue
                        else:
                            break
                        
                    fila -= 1
                    columna = ord(columna.upper()) - 65
                    if asientos[fila][columna] == Back.GREEN + "[ ]" + Style.RESET_ALL:
                        asientos[fila][columna] = Back.RED + "[ ]" + Style.RESET_ALL
                        asiento_codigo = f"{fila + 1}{chr(columna + 65)}"
                        asientos_seleccionados.append(asiento_codigo)
                        print("Asiento seleccionado con éxito!\n")
                        mostrar_asientos(asientos)
                        break
                    else:
                        print("Asiento ocupado, seleccione otro.")
                        mostrar_asientos(asientos)
            break
    total = sum([calcular_precio(espectador.edad) for espectador in espectadores])
    try:
        # Guardar la nueva reserva en el diccionario
        reservas_previas[clave_reserva] = asientos
        reserva = {
            "pelicula": pelicula_seleccionada.titulo,
            "hora": horaPelicula,
            "asientos": asientos_seleccionados,
            "asientos_disponibles": asientos,  
            "espectadores": espectadores,
            "total": total,
            'duracion': pelicula_seleccionada.duracion,
            "confirmada": False
        }
        
        print("\n¡Su reserva se ha realizado con éxito!\n")
        print(f"Película: {cine.pelicula.titulo}")
        print(f"Hora: {cine.hora}")
        print("Espectadores:")
        for espectador in espectadores:
            print(f"  - {espectador.nombre}")
        print("Sus asientos seleccionados:")
        mostrar_asientos(asientos)

        for i, asiento in enumerate(asientos_seleccionados):
            print(f"Su asiento N°{i+1} es: {asiento}")

        total = sum([calcular_precio(espectador.edad) for espectador in espectadores])
        print(f"Subtotal: ${total:.2f}")
    except KeyError:
        print("Error: La clave de reserva no es válida.")
    except TypeError:
        print("Error: El tipo de dato no es correcto.")
    else:
        reservas_realizadas.append(reserva)
        print("\n¡Su reserva se ha realizado con éxito!\n")  
    reserva = Reserva(pelicula_seleccionada, horaPelicula, asientos_seleccionados, espectadores, total, reserva_confirmada)
    return reserva

def ConfirmarReserva():
    # Verificar si hay reservas realizadas
    if not reservas_realizadas:
        print("No hay reservas realizadas para confirmar. Por favor, realiza una reserva primero.")
        return
    
    # Mostrar la lista de reservas
    print("\nReservas realizadas:")
    for i, reserva in enumerate(reservas_realizadas):
        print(f"\n{i+1}. Reserva N°{i+1}:")
        print(f"Película: {reserva['pelicula']}")
        print(f"Hora: {reserva['hora']}")
        print("Asientos seleccionados:")
        for asiento in reserva['asientos']:
            print(f"  - {asiento}")
        print("Espectadores:")
        for espectador in reserva['espectadores']:
            print(f"  - {espectador.nombre}")
        print(f"Subtotal: ${reserva['total']:.2f}")

    # Pedir que se seleccione una reserva para confirmar
    while True:
        try:
            opcion = int(input("\nSeleccione la reserva que desea confirmar: "))
            if opcion < 1 or opcion > len(reservas_realizadas):
                print("Opción inválida. Por favor, ingrese un número válido.")
                continue
            break
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número válido.")

    # Seleccionar la reserva correspondiente
    reserva_seleccionada = reservas_realizadas[opcion-1]

    # Verificar si la reserva ya está confirmada
    if reserva_seleccionada["confirmada"]:
        print("Esta reserva ya está confirmada y no se puede modificar.")
        return
    
    # Pedir los datos de los usuarios
    print("\nIngrese los datos de los espectadores para la reserva.")
    for i, espectador in enumerate(reserva_seleccionada['espectadores']):
        print(f"\nEspectador {i+1}:")
        
        while True:
            try:
                nombre = input("Nombre: ")
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío.")
                break
            except ValueError as e:
                print("Por favor, ingrese un nombre válido.")

        while True:
            try:
                edad = int(input("Edad: "))
                if edad < 0:
                    raise ValueError("La edad no puede ser negativa.")
                break
            except ValueError as e:
                print("Por favor, ingrese una edad válida.")

        
        if reserva_seleccionada['pelicula'] == "SAW":
            while edad < 18:
                print("Lo siento, la película SAW es para mayores de 18 años. Por favor, ingrese una edad válida.")
                edad = int(input("Ingrese la edad del nuevo espectador: "))
        elif reserva_seleccionada['pelicula'] == "Avatar":
            while edad < 12:
                print("Lo siento, la película Avatar es para mayores de 12 años. Por favor, ingrese una edad válida.")
                edad = int(input("Ingrese la edad del nuevo espectador: "))
        elif reserva_seleccionada['pelicula'] == "Interestellar":
            while edad < 12:
                print("Lo siento, la película Interestellar es para mayores de 12 años. Por favor, ingrese una edad válida.")
                edad = int(input("Ingrese la edad del nuevo espectador: "))

        while True:
            try:
                cantidad_dinero = float(input("Cantidad de dinero disponible: $"))
                if cantidad_dinero < 0:
                    raise ValueError("La cantidad de dinero no puede ser negativa.")
                break
            except ValueError as e:
                print("Por favor, ingrese una cantidad de dinero válida.")

        espectador.nombre = nombre
        espectador.edad = edad
        espectador.cantidad_dinero = cantidad_dinero
 

    # Aplicar descuentos globales basados en la función y el gasto total
    descuento = 0
    tipo_descuento = []  
    if reserva_seleccionada['total'] > 30:
        descuento = reserva_seleccionada['total'] * 0.10
        tipo_descuento.append("10% por gastar más de $30")
    elif 25 <= reserva_seleccionada['total'] <= 30:
        descuento = reserva_seleccionada['total'] * 0.05
        tipo_descuento.append("5% por gastar entre $25 y $30")

    if reserva_seleccionada['hora'] == "22:00": 
        descuento += reserva_seleccionada['total'] * 0.15
        tipo_descuento.append("15% por función después de las 9 PM")

        total_final = reserva_seleccionada['total'] - descuento

    # Calcular el precio de cada espectador y repartir el descuento proporcionalmente
    precio_total_espectadores = sum(calcular_precio(espectador.edad) for espectador in reserva_seleccionada['espectadores'])
    factor_descuento = total_final / reserva_seleccionada['total'] if reserva_seleccionada['total'] != 0 else 1  # Factor para aplicar proporcionalmente

    # Verificar si cada espectador tiene suficiente dinero para pagar su propia entrada con el descuento aplicado
    pago_exitoso = True
    for espectador in reserva_seleccionada['espectadores']:
        precio = calcular_precio(espectador.edad)  # Obtener el precio correcto según la edad del espectador
        precio_con_descuento = precio * factor_descuento  # Aplicar el descuento proporcional al precio individual

        if espectador.cantidad_dinero < precio_con_descuento:
            print(f"\nLo siento, {espectador.nombre} no tiene suficiente dinero para pagar su entrada de ${precio_con_descuento:.2f}.")
            pago_exitoso = False
            break
        else:
            cambio = espectador.cantidad_dinero - precio_con_descuento
            print(f"\n{espectador.nombre} ha pagado ${precio_con_descuento:.2f}.")
            print(f"Su cambio es: ${cambio:.2f}")

    # Actualizar la reserva en la lista reservas_realizadas
    if pago_exitoso:
        print("\n¡Confirmación de Reserva!")
        print(f"Película: {reserva_seleccionada['pelicula']}")
        print(f"Hora de la función: {reserva_seleccionada['hora']}")
        for asiento in reserva_seleccionada['asientos']:
            print(f"  - {asiento}")
        print(f"Subtotal: ${reserva_seleccionada['total']:.2f}")
        print(f"Descuento aplicado: ${descuento:.2f}")
        if tipo_descuento:
            print("Descuentos aplicados:")
            for tipo in tipo_descuento:
                print(f" - {tipo}")
        print(f"Total a pagar después de los descuentos: ${total_final:.2f}")
        print("\nReserva confirmada con éxito.")
        reserva_seleccionada["confirmada"] = True
    else:
        print("\nReserva no confirmada debido a falta de fondos.")

    # Mostrar la lista de reservas confirmadas
    print("\nReservas confirmadas:")
    reservas_confirmadas = [reserva for reserva in reservas_realizadas if reserva["confirmada"]]
    for i, reserva in enumerate(reservas_confirmadas):
        print(f"\nReserva N°{i+1}:")
        print(f"Película: {reserva['pelicula']}")
        print(f"Hora: {reserva['hora']}")
        print("Asientos seleccionados:")
        for asiento in reserva['asientos']:
            print(f"  - {asiento}")
        print("Espectadores:")
        for espectador in reserva['espectadores']:
            print(f"  - {espectador.nombre}")
        print(f"Subtotal: ${reserva['total']:.2f}")

    # Mostrar la lista de reservas no confirmadas
    print("\nReservas no confirmadas:")
    reservas_no_confirmadas = [reserva for reserva in reservas_realizadas if not reserva["confirmada"]]# Guardar la reserva no confirmada en una lista separada
    for i, reserva in enumerate(reservas_no_confirmadas):
        print(f"\nReserva N°{i+1}:")
        print(f"Película: {reserva['pelicula']}")
        print(f"Hora: {reserva['hora']}")
        print("Asientos seleccionados:")
        for asiento in reserva['asientos']:
            print(f"  - {asiento}")
        print("Espectadores:")
        for espectador in reserva['espectadores']:
            print(f"  - {espectador.nombre}")
        print(f"Subtotal: ${reserva['total']:.2f}")

reservas_no_confirmadas = []
def CancelarReserva():
    global reservas_realizadas, reservas_no_confirmadas, reserva_confirmada, pelicula_seleccionada, espectadores, asientos, total, cine, horaPelicula
    
    # Mostrar la lista de reservas
    print("\nReservas realizadas:")
    for i, reserva in enumerate(reservas_realizadas):
        print(f"\n{i+1}. Reserva N°{i+1}:")
        print(f"Película: {reserva['pelicula']}")
        print(f"Hora: {reserva['hora']}")
        print("Asientos seleccionados:")
        for asiento in reserva['asientos']:
            print(f"  - {asiento}")
        print("Espectadores:")
        for espectador in reserva['espectadores']:
            print(f"  - {espectador.nombre}")
        print(f"Subtotal: ${reserva['total']:.2f}")
        print(f"Confirmada: {reserva['confirmada']}")

    # Pedir que se seleccione una reserva para cancelar o agregar asiento
    while True:
        try:
            opcion = int(input("\nSeleccione la reserva que desea cancelar o agregar asiento: "))
            if opcion < 1 or opcion > len(reservas_realizadas):
                print("Opción inválida. Por favor, ingrese un número válido.")
                continue
            break
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número válido.")

    # Seleccionar la reserva correspondiente
    reserva_seleccionada = reservas_realizadas[opcion-1]

    # Verificar si la reserva ya está confirmada
    if reserva_seleccionada["confirmada"]:
        print("Esta reserva ya está confirmada. Puede agregar otro asiento.")
        agregar_asiento = True
    else:
        print("Esta reserva no está confirmada. Puede cancelarla o agregar otro asiento.")
        agregar_asiento = False

    # Mostrar menú para cancelar o agregar asiento
    while True:
        print("\nOpciones para la reserva seleccionada:")
        if not agregar_asiento:
            print("1. Cancelar reserva")
        print("2. Agregar otro asiento")
        print("3. Regresar al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))

            if not agregar_asiento and opcion == 1:
                respuesta = input("¿Estás seguro de que deseas cancelar esta reserva? (s/n): ")
                if respuesta.lower() == 's':
                    reservas_realizadas.remove(reserva_seleccionada)
                    print("Reserva cancelada con éxito.")
                    break
                else:
                    print("Cancelación de la reserva cancelada.")

            elif opcion == 2:
                # Agregar otro asiento
                print("\nAsientos disponibles:")
                mostrar_asientos(reserva_seleccionada['asientos_disponibles'])
                asientos_seleccionados = []
                for i in range(1):
                    while True:
                        try:
                            while True:
                                print(f"\nReservación para el nuevo asiento:")
                                fila = int(input("Ingrese la fila del asiento (1-8): "))
                                if fila < 1 or fila > 8:
                                    print("Fila incorrecta, por favor ingrese un número válido.")
                                    mostrar_asientos(reserva_seleccionada['asientos_disponibles'])
                                    continue
                                break
                        except ValueError:
                            print("Fila incorrecta, por favor ingrese un número válido.")
                            mostrar_asientos(reserva_seleccionada['asientos_disponibles'])
                            continue

                        while True:
                            columna = input("Ingrese la columna del asiento (A-I): ").upper()
                            if not 'A' <= columna <= 'I':
                                print("Columna incorrecta, por favor ingrese una letra válida.")
                                mostrar_asientos(reserva_seleccionada['asientos_disponibles'])
                                continue
                            else:
                                break

                        fila -= 1
                        columna = ord(columna.upper()) - 65
                        if reserva_seleccionada['asientos_disponibles'][fila][columna] == Back.GREEN + "[ ]" + Style.RESET_ALL:
                            reserva_seleccionada['asientos_disponibles'][fila][columna] = Back.RED + "[ ]" + Style.RESET_ALL
                            asiento_codigo = f"{fila + 1}{chr(columna + 65)}"
                            asientos_seleccionados.append(asiento_codigo)
                            reserva_seleccionada['asientos'].append(asiento_codigo)
                            print("Asiento seleccionado con éxito!\n")
                            mostrar_asientos(reserva_seleccionada['asientos_disponibles'])

                            # Pedir nombre y cantidad de dinero del nuevo espectador
                            while True:
                                try:
                                    nombre = input("Ingrese el nombre del nuevo espectador: ")
                                    if not nombre:
                                        raise ValueError("El nombre no puede estar vacío.")
                                    break
                                except ValueError as e:
                                    print("Por favor, ingrese un nombre válido.")
                                    
                                    
                            while True:
                                try:
                                    edad = int(input("Ingrese la edad del nuevo espectador: "))
                                    if edad < 0:
                                        raise ValueError("La edad no puede ser negativa.")
                                    break
                                except ValueError as e:
                                    print("Por favor, ingrese una edad válida.")
                                    

                            if reserva_seleccionada['pelicula'] == "SAW":
                                while edad < 18:
                                    print("Lo siento, la película SAW es para mayores de 18 años. Por favor, ingrese una edad válida.")
                                    edad = int(input("Ingrese la edad del nuevo espectador: "))
                            elif reserva_seleccionada['pelicula'] == "Avatar":
                                while edad < 12:
                                    print("Lo siento, la película Avatar es para mayores de 12 años. Por favor, ingrese una edad válida.")
                                    edad = int(input("Ingrese la edad del nuevo espectador: "))
                            elif reserva_seleccionada['pelicula'] == "Interestellar":
                                while edad < 12:
                                    print("Lo siento, la película Interestellar es para mayores de 12 años. Por favor, ingrese una edad válida.")
                                    edad = int(input("Ingrese la edad del nuevo espectador: "))

                            while True:
                                try:
                                    cantidad_dinero = float(input("Ingrese la cantidad de dinero disponible del nuevo espectador: $"))
                                    if cantidad_dinero < 0:
                                        raise ValueError("La cantidad de dinero no puede ser negativa.")
                                    elif cantidad_dinero < calcular_precio(edad):
                                        print("La cantidad de dinero ingresada no es suficiente para pagar el boleto. Por favor, ingrese una cantidad de dinero válida.")
                                    else:
                                        break
                                except ValueError as e:
                                    print("Por favor, ingrese una cantidad de dinero válida.")

                            # Agregar el nuevo espectador a la lista de espectadores
                            reserva_seleccionada['espectadores'].append(Espectador(nombre, edad, cantidad_dinero))

                            # Calcular el nuevo total con descuentos aplicados
                            total = sum([calcular_precio(espectador.edad) for espectador in reserva_seleccionada['espectadores']])
                            descuento = 0
                            tipo_descuento = []  
                            if total > 30:
                                descuento = total * 0.10
                                tipo_descuento.append("10% por gastar más de $30")
                            elif 25 <= total <= 30:
                                descuento = total * 0.05
                                tipo_descuento.append("5% por gastar entre $25 y $30")

                            if reserva_seleccionada['hora'] == "22:00": 
                                descuento += total * 0.15
                                tipo_descuento.append("15% por función después de las 9 PM")

                            total_final = total - descuento

                            print(f"\nSubtotal: ${total:.2f}")
                            print(f"Descuento aplicado: ${descuento:.2f}")
                            if tipo_descuento:
                                print("Descuentos aplicados:")
                                for tipo in tipo_descuento:
                                    print(f" - {tipo}")
                            print(f"Total a pagar después de los descuentos: ${total_final:.2f}")

                            # Actualizar el total de la reserva
                            reserva_seleccionada['total'] = total_final

                            break
                        else:
                            print("Asiento ocupado, seleccione otro.")
                            mostrar_asientos(reserva_seleccionada['asientos_disponibles'])
                        
            elif opcion == 3:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción no válida, por favor ingrese un número válido.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

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

    
pelicula_seleccionada = None
espectadores = None
asientos = None
total = None
cine = None
horaPelicula = None
reserva_confirmada = False
reserva_actual = None  # Para la nueva reserva que aún no ha sido confirmada

def menu():
    global pelicula_seleccionada, espectadores, asientos, total, cine, horaPelicula
    while True:
        print("\nBIENVENIDO USUARIO\nReservación de Boletos de Cine\n")
        print("0. Presentacion\n\n1. Reservar\n\n2. Confirmar Reserva\n\n3. Cancelar Reserva\n\n4. Salir\n")
        try:
            opcion = int(input("Seleccione una opcion del menu: "))

            if opcion == 0:
                Presentacion()
            elif opcion == 1:
                reserva = Realizar_reserva()
                reserva_confirmada = False  # Reiniciar confirmación al hacer una nueva reserva
            elif opcion == 2:
                # Verificar que las variables no sean None antes de confirmar la reserva
                if pelicula_seleccionada is not None and espectadores is not None and asientos is not None:
                    ConfirmarReserva()   
                else:
                    print("No hay ninguna reserva que confirmar. Por favor, realiza una reserva primero.")

            elif opcion == 3:
                # Cancelar la reserva
                CancelarReserva()
                
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