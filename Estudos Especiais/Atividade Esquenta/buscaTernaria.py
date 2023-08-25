# Busca ternária

vet = [1, 2, 8, 10, 20, 40, 90, 99, 100, 106, 109, 112]
start = 0
end = len(vet) - 1
numberSearched = 109
position = -1

while start <= end:
    halfLeft = round(start + (end - start) / 3)
    halfRight = round(end - (end - start) / 3)

    if vet[halfLeft] == numberSearched:
        position = halfLeft
        break
    elif vet[halfRight] == numberSearched:
        position = halfRight
        break
    elif vet[halfLeft] > numberSearched:
        end = halfLeft - 1
    elif vet[halfRight] < numberSearched:
        start = halfRight + 1
    else:
        start = halfLeft + 1
        end = halfRight - 1

print("Posição no vetor: ", position)
    