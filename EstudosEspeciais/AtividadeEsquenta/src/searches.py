# searches
from array import array

# Busca binária
def binary(vector: array, search: int, start: int, end: int):    
    half = round((start + end) / 2)
    if vector[half] == search:
        return half
    if start >= end:
        return -1
    elif vector[half] < search:
        binary(vector, search, half + 1, end)
    else:
        binary(vector, search, start, half - 1)

# Busca cúbica
def cubic(vector: int, search: int):
    position = -1

    for key, value1 in enumerate(vector):
        for value2 in vector:
            for value3 in vector:
                if value3 == search and value2 == search and value1 == search:
                    position = key

    return position

# Busca quadrática
def quadratic(vector: int, search: int):
    counter = 0
    position = -1
    cameIn = False

    for key, value1 in enumerate(vector):
        for value2 in vector:
            if value1 == search:
                if not cameIn:
                    position = key
                    if value2 == search:
                        counter += 1

        if counter > 0:
            cameIn = True

    return position

# Busca sequencial versão 1
def sequentialV1(vector: int, search: int):
    position = -1
    for key, value in enumerate(vector):
        if value == search:
            position = key

    return position

# Busca sequencial versão 2
def sequentialV2(vector: int, search: int):
    position = -1
    for key, value in enumerate(vector):
        if value == search:
            position = key
            break

    return position

# Busca ternária
def ternary(vector: array, search: int):
    start = 0
    end = len(vector) - 1
    position = -1
    while start <= end:
        halfLeft = round(start + (end - start) / 3)
        halfRight = round(end - (end - start) / 3)

        if vector[halfLeft] == search:
            position = halfLeft
            break
        elif vector[halfRight] == search:
            position = halfRight
            break
        elif vector[halfLeft] > search:
            end = halfLeft - 1
        elif vector[halfRight] < search:
            start = halfRight + 1
        else:
            start = halfLeft + 1
            end = halfRight - 1

    return position