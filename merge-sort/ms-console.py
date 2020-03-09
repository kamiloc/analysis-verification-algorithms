from random import sample
from time import time

# Aquí solicitamos el tamaño de la lista aleatoria
print("Escribe el tamaño de la lista (número entero):")
radomListLength = int(input())

compareCount = 0  # En esta variable se lleva el conteo de comparaciones
startTime = time()  # Con esto se mide el tiempo de ejecución del programa


# Función mergeSort
def mergeSort(baseList):
    # Comprueba que la lista contenga al menos 2 elementos
    # Si es menor se retorna la lista de entrada
    if len(baseList) < 2:
        return baseList
    # De lo contrario, se divide en 2
    else:
        middle = len(baseList) // 2
        right = mergeSort(baseList[:middle])
        left = mergeSort(baseList[middle:])
        return merge(right, left)


# Función merge
def merge(list_1, list_2):
    global compareCount  # Variable de conteo global
    i, j = 0, 0  # Variables de incremento
    result = []  # Lista de resultado

    # En este punto se hacen las comparaciones,
    # para ordenar las listas por mezcla
    while (i < len(list_1) and j < len(list_2)):
        if (list_1[i] < list_2[j]):
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    # Agregamos los valores restantes a la lista resultados
    result += list_1[i:]
    result += list_2[j:]

    # Se agrega el número de comparaciones a la variable global
    compareCount += (i + j)

    # Retornamos el resultados
    return result


# Generar una lista aleatoria de n elementos con números hasta 100
# Siendo n el tamaño definido por el usuario
randomList = sample(range(radomListLength * 2), k=radomListLength)
orderedList = mergeSort(randomList)
totalTime = time() - startTime

# Prueba del algoritmo
print("Deses imprimir las listas (S/n):")
printList = str(input())

if (printList == "S" or printList == "s"):
    print(
        "Lista original: {0}\nLista ordenada: {1}\nNúmero de comparaciones: {2}"
        .format(randomList, orderedList, compareCount))
else:
    print("Número de comparaciones: {0}".format(compareCount))

print("El programa tardó {0:.10f} segundos en finalizar".format(totalTime))