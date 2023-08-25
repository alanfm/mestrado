# Busca Binária
vet = [1, 2, 8, 10, 20, 40, 90, 99, 100, 106]
numberSearched = 2
start = 0
end = len(vet) - 1
half = -1
position = -1

while vet[half] != numberSearched:
    half = round((start + end) / 2)
    if vet[half] == numberSearched:
        position = half
        break
    if start >= end:
        break
    elif vet[half] < numberSearched:
        start = half + 1
    else:
        end = half - 1

print("Posição no vetor: ", position)