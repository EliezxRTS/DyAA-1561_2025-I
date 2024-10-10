def producto_mas_alto(array):
    max_producto = 0
    index_i = None
    index_j = None
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                producto = array[i] * array[j]
                if producto > max_producto:
                    index_i = i
                    index_j = j
                    max_producto = producto
    return max_producto, index_i, index_j

def buscar_patron(array, patron):
    len_array = len(array)
    len_patron = len(patron)
    contador = 0
    for i in range((len_array - len_patron) + 1):
        for j in range(len_patron):
            if array[i + j] == patron[j]:
                contador += 1
                if contador == len_patron:
                    return True
            else:
                contador = 0
                break
    return False

def combinar_objetos_mochila(array):
    if not array:
        return [[]]
    primer_elemento = array[0]
    combinar_sin_primero = combinar_objetos_mochila(array[1:])
    combinar_con_primero = [[primer_elemento] + combinaciones for combinaciones in combinar_sin_primero]
    
    return combinar_con_primero + combinar_sin_primero

def problema_mochila(objetos, capacidad_maxima):
    for o in range(len(objetos)):
        print(f"Objeto {o+1}: {objetos[o]}.")
    subconjuntos = combinar_objetos_mochila(list(enumerate(objetos)))
    mejor_valor = 0
    mejor_combinacion = []
    indices_mejor_combinacion = []
    for subconjunto in subconjuntos:
        peso_total = sum(objetos[i][0] for i, _ in subconjunto)
        valor_total = sum(objetos[i][1] for i, _ in subconjunto)
        if peso_total <= capacidad_maxima and valor_total > mejor_valor:
            mejor_valor = valor_total
            mejor_combinacion = [objeto for i, objeto in subconjunto]
            indices_mejor_combinacion = [i+1 for i, objeto in subconjunto]
    
    return mejor_valor, mejor_combinacion, indices_mejor_combinacion

def main():
    print("Producto más alto")
    A1 = [-9, 3, 5, -2, 9, -7, 4, 8, 6]
    valor, num_a, num_b = producto_mas_alto(A1)
    print(f"Dado el arreglo: {A1}")
    print(f"El producto más alto es: [{valor}] con los numeros {A1[num_a]} y {A1[num_b]}\n\n")

    print("¿Aparece el patrón P en el array A?")
    A2 = [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1]
    P = [0, 1, 1, 0, 1]
    busqueda = buscar_patron(A2, P)
    print(f"Array A: {A2}")
    print(f"Patrón P: {P}")
    print("El patrón está en el arreglo\n\n" if busqueda else "El patrón no está en el arreglo\n\n")

    print("Problema de la mochila")
    objetos = [(2, 3), (3, 4), (4, 5), (5, 8)]
    capacidad_maxima = 8
    mejor_valor, mejor_combinacion, indices_mejor_combinacion = problema_mochila(objetos, capacidad_maxima)
    print(f"Dada la capacidad máxima: {capacidad_maxima}")
    print(f"El mejor valor es: {mejor_valor}")
    print(f"Con los objetos {indices_mejor_combinacion} que son {mejor_combinacion}")

if __name__ == '__main__':
    main()