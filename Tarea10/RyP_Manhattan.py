import heapq

def cargar_laberinto(nombre_archivo='Tarea10/laberinto.csv'):
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
        'Y': '👣',  # Visitado temporalmente
        '*': '🏆',  # Camino final
        'X': '🔙'   # Camino descartado
    }
    for fila in laberinto:
        print("".join(simbolos.get(celda, celda) for celda in fila))
    if solucion_encontrada:
        print("\n¡Solución encontrada!")
    else:
        print()

def verificar_movimiento(laberinto, x, y):
    filas = len(laberinto)
    columnas = len(laberinto[0]) if filas > 0 else 0
    return 0 <= x < filas and 0 <= y < columnas and laberinto[x][y] not in {'P', 'Y', 'X'}

def buscar_entrada(laberinto, entrada, salida):
    entrada_x_y = None
    salida_x_y = None
    for x in range(len(laberinto)):
        for y in range(len(laberinto[x])):
            if laberinto[x][y] == entrada:
                entrada_x_y = [x, y]
            if laberinto[x][y] == salida:
                salida_x_y = [x, y]
    return entrada_x_y, salida_x_y

def distancia_manhattan(actual, objetivo):
    return abs(actual[0] - objetivo[0]) + abs(actual[1] - objetivo[1])

def principal():
    laberinto = cargar_laberinto()
    if not laberinto:
        return
    entrada, salida = buscar_entrada(laberinto, 'E', 'S')
    if entrada is None or salida is None:
        print("El laberinto no tiene una entrada o salida válidas.")
        return
    print("Laberinto original:")
    mostrar_laberinto(laberinto)
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, entrada[0], entrada[1], []))
    visitados = set()
    visitados.add((entrada[0], entrada[1]))
    laberinto[entrada[0]][entrada[1]] = 'Y'
    solucion_encontrada = False
    while cola_prioridad and not solucion_encontrada:
        _, x, y, ruta = heapq.heappop(cola_prioridad)
        laberinto[x][y] = 'Y'
        ruta.append((x, y))
        if [x, y] == salida:
            for rx, ry in ruta:
                laberinto[rx][ry] = '*'
            solucion_encontrada = True
            break
        movimientos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        movimiento_valido = False
        for nx, ny in movimientos:
            if verificar_movimiento(laberinto, nx, ny) and (nx, ny) not in visitados:
                prioridad = distancia_manhattan((nx, ny), salida)
                heapq.heappush(cola_prioridad, (prioridad, nx, ny, ruta[:]))
                visitados.add((nx, ny))
                movimiento_valido = True
        if not movimiento_valido:
            laberinto[x][y] = 'X'
    if solucion_encontrada:
        mostrar_laberinto(laberinto, solucion_encontrada=True)
        print(f"El camino tiene {len(ruta)} pasos.")
    else:
        print("No se encontró solución.")

if __name__ == '__main__':
    principal()