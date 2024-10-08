
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

def mostrar_asientos(asientos):
    print("Asientos disponibles:")
    for i, fila in enumerate(asientos):
        print(f"{8 - i} | {' '.join(fila)}")

def Reservar():
    peliculas = [
        Pelicula("Pelicula 1", 120, 18, "Director 1"),
        Pelicula("Pelicula 2", 90, 16, "Director 2"),
        # Agrega más películas aquí
    ]

    cines = [
        Cine(peliculas[0], 6.25, "19:00"),
        Cine(peliculas[1], 6.25, "21:00"),
        # Agrega más cines aquí
    ]

    print("Seleccione una película:")
    for i, pelicula in enumerate(peliculas):
        print(f"{i+1}. {pelicula.titulo} ({pelicula.duracion} minutos, Edad mínima: {pelicula.edad_minima})")

    opcion_pelicula = int(input("Ingrese el número de la película: "))
    selected_pelicula = peliculas[opcion_pelicula - 1]
    print(f"Película seleccionada: {selected_pelicula.titulo}")
    print(f"Duración: {selected_pelicula.duracion} minutos")
    print(f"Edad mínima: {selected_pelicula.edad_minima}")
    print(f"Director: {selected_pelicula.director}")
    print(f"Precio: {cines[0].precio}")
    print(f"Hora: {cines[0].hora}")

    asientos = [["0" for _ in range(9)] for _ in range(8)]

    while True:
        mostrar_asientos(asientos)
        fila = int(input("Ingrese la fila del asiento (1-8): "))
        columna = input("Ingrese la columna del asiento (A-I): ")
        fila -= 1
        columna = ord(columna) - 65

        if asientos[fila][columna] == "0":
            asientos[fila][columna] = "X"
            print("Asiento seleccionado con éxito!")
        else:
            print("Asiento ocupado, seleccione otro.")

        respuesta = input("¿Desea seleccionar otro asiento? (S/N): ")
        if respuesta.upper() != "S":
            break

    return selected_pelicula, fila, columna, asientos

def ConfirmarReserva(selected_pelicula, fila, columna, asientos):
    print("Ingrese sus datos:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    cantidad_dinero = float(input("Cantidad de dinero: "))

    print("\nDatos de la reserva:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Película seleccionada: {selected_pelicula.titulo}")
    print(f"Asientos asignados: Fila {8 - fila}, Columna {chr(columna + 65)}")

    # Calcular el total a pagar
    total_a_pagar = 6.25

    # Aplicar descuentos
    if total_a_pagar > 30.00:
        total_a_pagar *= 0.9
        print("Se aplicó un descuento del 10% por compra superior a 30.00")
    elif total_a_pagar >= 25.00 and total_a_pagar <= 30.00:
        total_a_pagar *= 0.95
        print("Se aplicó un descuento del 5% por compra entre 25.00 y 30.00")

    # Verificar si la tanda es después de las 9:00 de la noche

    print(f"Total a pagar: {total_a_pagar:.2f}")

    # Verificar si el usuario tiene suficiente dinero
    if cantidad_dinero >= total_a_pagar:
        print("La reserva se ha confirmado con éxito.")
        print ("Gracias por su compra.")
    else:
        print("No tiene suficiente dinero para realizar la reserva.")

def CancelarReserva(selected_pelicula, fila, columna, asientos):
    print("¿Qué desea hacer?")
    print("1. Agregar otro asiento")
    print("2. Eliminar reserva y comenzar de nuevo")

    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        print("Asientos disponibles:")
        for i, fila in enumerate(asientos):
            print(f"{8 - i} | {' '.join(fila)}")

        fila_nueva = int(input("Ingrese la fila del asiento (1-8): "))
        columna_nueva = input("Ingrese la columna del asiento (A-I): ")
       
        
print("BIENVENIDO USUARIO\nReservación de Boletos de Cine\n")
print("1. Reservar\n\n2. Confirmar Reserva\n\n3. Cancelar Reserva\n")

opcion = int(input("Seleccione una opcion del menu:"))

if opcion == 1:
     Reservar()
elif opcion==2:
    ConfirmarReserva()
elif opcion==3:
    CancelarReserva()
