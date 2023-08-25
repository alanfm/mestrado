# Busca sequencial V1

vet = [2, 4, 5, 6, 2, 4, 9, 4, 5, 6]
position = -1
numberSearched = 2

for key, value in enumerate(vet):
    if vet[key] == numberSearched:
        position = key

if position < 0:
    print("Nenhum valor encontrado.")
else:
    print("Posição: " + str(position))