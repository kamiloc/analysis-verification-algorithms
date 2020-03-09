import matplotlib.pyplot as plt
from random import sample

# En esta variable se lleva el conteo de comparaciones
compareCount = 0


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


# Datos para la gráfica
compareGraph = {
    "x": [],
    "y": []
}
# Contador de iteraciones
i = 1

while i <= 20:
    # Reinicicar el contador
    compareCount = 0
    print(">>> Generando la lista aleotoria #{0} ...".format(i))

    # Definir el tamaño de la lista en base a el contador de iteración
    # como: [contador]*1000
    radomListLength = int(i*1e3)
    randomList = sample(range(radomListLength * 2), k=radomListLength)

    # Ordernar la lista aleatorio
    mergeSort(randomList)

    # Guardar los datos: - x : Número de lista, - y : Número de comparaciones
    compareGraph["y"].append(compareCount)
    compareGraph["x"].append(i)

    i += 1


# Implementación de la gráfica

# -- alimentar los datos
plt.plot(compareGraph["x"], compareGraph["y"])

# -- configurar los ejes y la grillas
plt.xlabel("Número de lista")
plt.ylabel("Comparaciones")
plt.grid(True)

# -- mostrar la gráfica
plt.show()