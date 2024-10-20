def problema_mochila(pesos_objetos, valores_objetos, capacidad_mochila, n):
    if n == 0 or capacidad_mochila == 0 or len(pesos_objetos) != len(valores_objetos):
        return 0
    
    if pesos_objetos[n-1] > capacidad_mochila:
        return problema_mochila(pesos_objetos, valores_objetos, capacidad_mochila, n-1)
    
    # 1. Llamada recursiva sin incluir el objeto.
    opcion1 = problema_mochila(pesos_objetos, valores_objetos, capacidad_mochila, n-1)
    # 2. Llamada recursiva incluyendo el objeto y restando su peso de la capacidad.
    opcion2 = valores_objetos[n-1] + problema_mochila(pesos_objetos, valores_objetos, capacidad_mochila - pesos_objetos[n-1], n-1)
    
    return max(opcion1, opcion2)

def main():
    print("\nProblema de la mochila\n")
    pesos = [2, 3, 4, 5]
    valores = [3, 4, 5, 8]
    capacidad = 8
    n = min(len(pesos),len(valores))

    resultado = problema_mochila(pesos, valores, capacidad, n)
    print(f"Dada la capacidad de peso máxima: {capacidad}\n")
    print(f"Y los {n} obejetos de peso: {pesos} y valor: {valores}\n")
    if resultado == 0:
        print("No se puede obtener un resultado!\n")
    else:
        print(f"El valor máximo que se puede obtener es: {resultado}\n")

if __name__ == '__main__':
        main()