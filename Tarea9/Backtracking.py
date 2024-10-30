def cargar_laberinto(nombre_archivo='Tarea9\laberinto.csv'):
    laberinto = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                laberinto.append(linea.strip().split(','))
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se encontró.")
        return []
    return laberinto

def mostrar_laberinto(laberinto, solucion_encontrada=False):
    simbolos = {
        'E': '🚀',  # Entrada
        'S': '🏁',  # Salida
        'C': '⬜',  # Corredor
        'P': '🧱',  # Pared
        '-': '👣',  # Visitado
        '*': '🏆',  # Salida encontrada
        'X': '🔙',  # Camino descartado
        'A': '🌲'   # Línea de entrada
    }
    for fila in laberinto:
        print("".join(simbolos.get(celda, celda) for celda in fila))
    if solucion_encontrada:
        print("\n¡Solución encontrada!")
    else:
        print("\nNo se encontró ninguna solución.")

def movimiento_valido(laberinto, fila, columna):
    if fila < 0 or fila >= len(laberinto) or columna < 0 or columna >= len(laberinto[0]):
        return False
    return laberinto[fila][columna] != 'P'

def mover(laberinto, fila, columna, direccion):
    movimientos = { "arb": (-1, 0), "abj": (1, 0), "izq": (0, -1), "der": (0, 1) }
    cambio_fila, cambio_columna = movimientos[direccion]
    nueva_fila, nueva_columna = fila + cambio_fila, columna + cambio_columna
    if movimiento_valido(laberinto, nueva_fila, nueva_columna):
        return nueva_fila, nueva_columna
    return fila, columna

def buscar_inicio(laberinto, inicio):
    for fila in range(len(laberinto)):
        if inicio in laberinto[fila]:
            columna = laberinto[fila].index(inicio)
            return fila, columna
    return -1, -1

def principal():
    ruta = []
    nombre_archivo = 'laberinto.csv'
    laberinto = cargar_laberinto(nombre_archivo)
    if not laberinto:
        return
    print("Labertinto inicial:")
    mostrar_laberinto(laberinto)
    fila_inicio, columna_inicio = buscar_inicio(laberinto, 'E')
    if fila_inicio == -1:
        print("El laberinto no tiene un punto de inicio.")
        return
    ruta.append((fila_inicio, columna_inicio))
    laberinto[fila_inicio][columna_inicio] = '-'
    solucion_encontrada = False
    while ruta and not solucion_encontrada:
        fila, columna = ruta[-1]
        for direccion in ["izq", "arb", "der", "abj"]:
            nueva_fila, nueva_columna = mover(laberinto, fila, columna, direccion)
            if (nueva_fila, nueva_columna) != (fila, columna):
                if laberinto[nueva_fila][nueva_columna] == 'S':
                    laberinto[nueva_fila][nueva_columna] = '*'
                    solucion_encontrada = True
                    break
                elif laberinto[nueva_fila][nueva_columna] == 'C':
                    laberinto[nueva_fila][nueva_columna] = '-'
                    ruta.append((nueva_fila, nueva_columna))
                    break
        else:
            laberinto[fila][columna] = 'X'
            ruta.pop()
    print("\nLabertinto después de la búsqueda:")
    mostrar_laberinto(laberinto, solucion_encontrada)
    if solucion_encontrada:
        print(f"La solución cuenta con {len(ruta)} pasos.")
    else:
        print("No se encontró ninguna solución.")

if __name__ == "__main__":
    principal()