# Algoritmo de busca cúbica

vet = [2, 4, 5, 6, 2, 4, 9, 4, 5, 6]
numberSearched = 2
position = -1

for key1, value1 in enumerate(vet):
    for key2, value2 in enumerate(vet):
        for key3, value3 in enumerate(vet):
            if vet[key3] == numberSearched and vet[key2] == numberSearched and vet[key1] == numberSearched:
                position = key1

if position != 1:
    print("Posição: " + str(position))
