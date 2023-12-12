# Definir una función para imprimir el tablero de ajedrez
def imprimir_tablero(tablero):
    # Iterar sobre cada fila en el tablero de ajedrez
    for fila in tablero:
        # Utilizar join para concatenar cada elemento de la fila con un tabulador ('\t') como separador
        print("\t".join(fila))
    # Imprimir una línea nueva para un mejor formato
    print()

# Definir una función para guardar el estado del tablero de ajedrez en un archivo
def guardar_tablero_en_archivo(nombre_archivo, tablero):
    # Abrir el archivo en modo de añadir ('a')
    with open(nombre_archivo, "a") as archivo:
        # Iterar sobre cada fila en el tablero
        for fila in tablero:
            # Escribir en el archivo cada elemento de la fila con un tabulador ('\t') como separador y agregar una nueva línea al final
            archivo.write("\t".join(fila) + "\n")
        # Agregar una línea en blanco para un mejor formato
        archivo.write("\n")

# Definir una función para realizar un movimiento en el tablero de ajedrez
def realizar_movimiento(tablero, fila_origen, col_origen, fila_destino, col_destino):
    # Obtener la pieza en la posición de origen
    pieza = tablero[fila_origen][col_origen]
    # Limpiar la posición de origen en el tablero
    tablero[fila_origen][col_origen] = "  "
    # Colocar la pieza en la posición de destino
    tablero[fila_destino][col_destino] = pieza

# Solicitar al usuario que introduzca el nombre del archivo para guardar la partida
nombre_archivo = input("Introduce el nombre del archivo para guardar la partida: ")

# Función principal del programa
def main():

    # Tablero inicial de ajedrez
    tablero = [
        ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
        ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
        ["  "] * 8,
        ["  "] * 8,
        ["  "] * 8,
        ["  "] * 8,
        ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
        ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
    ]

    # Guardar el tablero inicial en el archivo y imprimirlo
    guardar_tablero_en_archivo(nombre_archivo, tablero)
    imprimir_tablero(tablero)

    # Inicializar el contador de turnos
    turno = 1

    # Bucle principal del juego
    while True:
        # Imprimir el número del turno
        print(f"Turno {turno}")

        # Preguntar al usuario si quiere hacer un movimiento
        opcion = input("¿Quieres hacer un movimiento? (s/n): ")

        # Salir del bucle si la respuesta no es 's'
        if opcion.lower() != 's':
            break
        
        # Solicitar información sobre el movimiento al usuario
        fila_origen = int(input("Fila de la pieza que quieres mover: "))
        col_origen = int(input("Columna de la pieza que quieres mover: "))
        fila_destino = int(input("Fila a la que quieres mover la pieza: "))
        col_destino = int(input("Columna a la que quieres mover la pieza: "))

        # Realizar el movimiento en el tablero y guardarlo en el archivo
        realizar_movimiento(tablero, fila_origen, col_origen, fila_destino, col_destino)
        guardar_tablero_en_archivo(nombre_archivo, tablero)

        # Imprimir el tablero actualizado
        imprimir_tablero(tablero)

        # Incrementar el contador de turnos
        turno += 1

# Verificar si el script está siendo ejecutado directamente
if __name__ == "__main__":
    # Llamar a la función principal del programa
    main()
