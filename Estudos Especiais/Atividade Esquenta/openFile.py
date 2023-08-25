# Lendo arquivo de texto
fileName = "teste.txt"
vet = []
try:
    with open(fileName, "r") as file:
        contentLine = file.readline()
        while contentLine:
            vetStr = contentLine.split(', ')
            vet += [int(element) for element in vetStr if element.isdigit()]
            contentLine = file.readline()
        print(vet)

except FileNotFoundError:
    print(f"O arquivo {fileName} não foi encontrado.")