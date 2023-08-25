# Busca quadrática

vet = [2, 4, 5, 6, 2, 4, 9, 4, 5, 6]
numberSearched = 4
counter = 0
position = -1
cameIn = False

for key1, value1 in enumerate(vet):
    for key2, value2 in enumerate(vet):
        if vet[key1] == numberSearched:
            if cameIn:
                position = key1
                if vet[key2] == numberSearched:
                    counter += 1
    if counter > 0:
        cameIn = True

if cameIn:
    print("Posição: " + str(position) + " - Contador de repetição: " + counter)