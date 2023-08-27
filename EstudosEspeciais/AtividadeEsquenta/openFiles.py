# Lendo arquivo de texto
import os
import time
import random
import src.searches as searches

# Pega todos os arquivos que estão no diretório
def parseDirectory(directory):
    return os.listdir(directory)

# Executa a função de busca e retorna o tempo gasto
def runSearches(vector):
    startTime = time.time()
    searches.ternary(vector, random.randint(vector[0], vector[len(vector) - 1]))
    endTime = time.time()
    return endTime - startTime

# Gera um vetor com os dados do arquivo
def generateArray(file):
    vector = []
    contentLine = file.readline()
    while contentLine:
        vector += [int(element) for element in contentLine.split(',') if element.isdigit()]
        contentLine = file.readline()

    return vector

# Abre o arquivo e retorna os dados em forma de vetor
def parseFile(file, directory = ''):
    vector = []
    try:
        with open(directory + file, "r") as file:
            vector = generateArray(file)
        return vector
    except FileNotFoundError:
        print(f"O arquivo {file} não foi encontrado.")

def interationFiles(directory):
    for file in parseDirectory(directory):
        runSearches(parseFile(file, directory))

if __name__ == "__main__":
    directory = 'files/'
    interationFiles(directory)