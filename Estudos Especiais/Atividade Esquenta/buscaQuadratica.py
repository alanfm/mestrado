# Busca quadrática

def quadraticSearch(vet, search):
    counter = 0
    position = -1
    comeIn = False

    for key, value1 in enumerate(vet):
        for value2 in enumerate(vet):
            if value1 == search:
                if not cameIn:
                    position = key
                    if value2 == search:
                        counter += 1

        if counter > 0:
            cameIn = True

    if cameIn:
        print("Posição: " + str(position) + " - Contador de repetição: " + str(counter))

    return position

vet = [2, 4, 5, 6, 2, 4, 9, 4, 5, 6]

quadraticSearch(vet, 2)
