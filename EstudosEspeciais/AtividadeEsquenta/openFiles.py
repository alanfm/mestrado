# Lendo arquivo de texto
import os
import time
import random
import src.searches as searches
import tracemalloc
import csv

# Pega todos os arquivos que estão no diretório
def parseDirectory(directory):
    return os.listdir(directory)

# Executa a função de busca e retorna o tempo gasto
def runSearches(vector, value, sortFunction):
    tracemalloc.start()
    startTime = time.time()
    for i in range(20):
        if sortFunction == 'binary':
            searches.binary(vector, value, 0, len(vector) - 1)
        elif sortFunction == 'cubic':
            searches.cubic(vector, value)
        elif sortFunction == 'quadratic':
            searches.quadratic(vector, value)
        elif sortFunction == 'sequentialV1':
            searches.sequentialV1(vector, value)
        elif sortFunction == 'sequentialV2':
            searches.sequentialV2(vector, value)
        elif sortFunction == 'ternary':
            searches.ternary(vector, value)
    memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tracemalloc.clear_traces()
    endTime = time.time()
    meddleTime = (endTime - startTime) / 20
    result = [str(f'{meddleTime:.7f}'), (memory[1]), value, sortFunction, str(len(vector)) + '.txt']
    return result
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
        file.close()
        return vector
    except FileNotFoundError:
        print(f"O arquivo {file} não foi encontrado.")

# Percorre os arquivos encontrados no diretório
def iterationFiles(directory, algorithms, sorted):
    for sort in algorithms:
        if sorted:
            resultFileName = 'results/' + sort + '_sorted.csv'
        else:
            resultFileName = 'results/' + sort + '_unsorted.csv'
        with open(resultFileName, 'w') as resultFile:
            spamWriter = csv.writer(resultFile, dialect='excel')
            spamWriter.writerow(['Tempo', 'Memória', 'Valor', 'Algoritmo', 'Arquivo'])
            for file in parseDirectory(directory):
                if (not file.endswith(".txt")):
                    continue
                vector = parseFile(file, directory)        
                value = random.choice(vector)
                spamWriter.writerow(runSearches(vector, value, sort))
                print(f"Arquivo {file.split('/')[0]} processado.\nFunção de busca: {sort}")
        resultFile.close()

# Executa o programa
if __name__ == "__main__":
    directory = 'src/files/sorted/'
    iterationFiles(directory, ['quadratic', 'cubic'], True)
    directory = 'src/files/unsorted/'
    iterationFiles(directory, ['quadratic', 'cubic'], False)