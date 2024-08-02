def conteo_de_elementos(matriz):
    vistos = []
    repetidos = []
    #Recorre la matriz y actualiza las listas de vistos y repetidos
    for fila in matriz:
        for num in fila:
            if num in vistos:
                if num not in repetidos:
                    repetidos.append(num)
            else:
                vistos.append(num)
    #Calcula el número de elementos únicos (vistos una vez)
    una_vez = len([num for num in vistos if num not in repetidos])
    
    #Calcula el número de elementos repetidos
    conteo_repetidos = len(repetidos)
    
    #Retorna el arreglo con los dos valores
    return [una_vez, conteo_repetidos]

# Ejemplos
print(conteo_de_elementos([[2, 2], [2, 2]]))       #Salida: [0, 1]
print(conteo_de_elementos([[2, 1, 3], [4, 5, 2], [6, 6, 6]])) #Salida: [4, 2]
