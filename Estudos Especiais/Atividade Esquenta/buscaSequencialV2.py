# Busca sequencial V2

vet = [2, 4, 5, 6, 2, 4, 9, 4, 5, 6]
position = -1
numberSearched = 2

print("Valor buscado: " + str(numberSearched))

for key, value in enumerate(vet):
    if vet[key] == numberSearched:
        position = key
        break

if position < 0:
    print("Valor não encontrado no vetor.")
else:
    print("Posição no vetor: " + str(position))