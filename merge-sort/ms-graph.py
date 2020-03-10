from random import sample
from matplotlib import pyplot as plt
from math import log

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
    "y": [],
    "l": []
}
# Contador de iteraciones
i = 1
# Escala para generar listas
listScale = input(">>> Ingrese la escala para las listas: ")

while i <= 20:
    # Reinicicar el contador
    compareCount = 0

    # Definir el tamaño de la lista en base a el contador de iteración
    # como: [contador]*[escala]
    radomListLength = int(listScale) * i

    print(">>> Generando la lista aleotoria #{0} de tamaño {1} ...".format(i, radomListLength))
    randomList = sample(range(radomListLength * 2), radomListLength)

    # Ordernar la lista aleatoria
    mergeSort(randomList)

    # Guardar los datos: - x :Tamaño de la lista, - y : Número de comparaciones, -l : función x*log[2](x)
    compareGraph["y"].append(compareCount)
    compareGraph["x"].append(radomListLength)
    compareGraph["l"].append(radomListLength * log(radomListLength, 2))

    i += 1


# Implementación de la gráfica

# -- alimentar los datos
plt.plot(compareGraph["x"], compareGraph["y"], label="n * C(n)")
plt.plot(compareGraph["x"], compareGraph["l"], label="n * log[2](n)")

# -- configurar los ejes y la grillas
plt.xlabel("Tamaño de la lista")
plt.ylabel("Comparaciones")
plt.legend()
plt.grid(True)

# -- mostrar la gráfica
plt.show()
