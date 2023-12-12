# Ajedrez
https://github.com/vdiazqui/Ajedrez.git

Este programa en Python simula un juego de ajedrez en la consola, permitiendo a los usuarios realizar movimientos y guardar el estado de la partida en un archivo.
## Cómo Usar:

### Inicio del Juego:
Elige un nombre para el archivo de la partida.
Visualiza el tablero inicial de ajedrez.
### Realizar Movimientos:
Decide si deseas hacer un movimiento (sí/no).
Si eliges "sí", introduce detalles sobre el movimiento.

## Estructura del Código:

### Funciones:
imprimir_tablero(tablero): Muestra el estado del tablero en la consola.
guardar_tablero_en_archivo(nombre_archivo, tablero): Guarda el tablero en un archivo.
realizar_movimiento(tablero, fila_origen, col_origen, fila_destino, col_destino): Realiza un movimiento.
### Flujo Principal:
Se pide el nombre del archivo para guardar la partida.
Inicia un bucle para realizar movimientos hasta que el usuario decide no hacer más.
