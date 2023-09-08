# Lendo arquivo de texto
import os
import time
import random
import src.searches as searches
import tracemalloc
import csv
import re
import numpy as np

# Pega todos os arquivos que estão no diretório
def parseDirectory(directory):
    return os.listdir(directory)

# Executa a função de busca e retorna o tempo gasto
def runSearches(vector, value, sortFunction):
    tracemalloc.start()
    startTime = time.time()
    for i in range(2):
        if sortFunction == 'binary':
            result = searches.binary(vector, value, 0, len(vector) - 1)
        elif sortFunction == 'cubic':
            result = searches.cubic(vector, value)
        elif sortFunction == 'quadratic':
            result = searches.quadratic(vector, value)
        elif sortFunction == 'sequentialV1':
            result = searches.sequentialV1(vector, value)
        elif sortFunction == 'sequentialV2':
            result = searches.sequentialV2(vector, value)
        elif sortFunction == 'ternary':
            result = searches.ternary(vector, value)
    memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tracemalloc.clear_traces()
    endTime = time.time()
    meddleTime = (endTime - startTime) / 2
    print('Função: ' + sortFunction, ' | Valor pesquisado: ' + str(value), ' | Tamanho do vetor: ' + str(len(vector)), ' | Resultado: ' + str(result))
    return [str(f'{meddleTime:.7f}'), (memory[1]), value, sortFunction, str(len(vector)) + '.txt']
# Gera um vetor com os dados do arquivo
def generateArray(file):
    start = time.time()
    vector = np.loadtxt(file, dtype=np.int64, delimiter=',')
    result = vector.flatten()
    print('Vetor gerado em: ' + str(time.time() - start) + ' segundos')
    return result

# Abre o arquivo e retorna os dados em forma de vetor
def parseFile(file, directory = ''):
    vector = []
    try:
        with open(directory + file, "r") as file:
            vector = generateArray(file)
        file.close()
    except FileNotFoundError:
        print(f"O arquivo {file} não foi encontrado.")
    
    return vector

# Percorre os arquivos encontrados no diretório
def iterationFiles(directory, algorithms, sorted):
    for sort in algorithms:
        if sorted:
            resultFileName = 'results/' + sort + '_sorted.csv'
        else:
            resultFileName = 'results/' + sort + '_unsorted.csv'
        with open(resultFileName, 'w') as resultFile:
            spamWriter = csv.writer(resultFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamWriter.writerow(['Tempo', 'Memória', 'Valor', 'Algoritmo', 'Arquivo'])
            for file in parseDirectory(directory):
                if (not file.endswith(".txt")):
                    continue
                vector = parseFile(file, directory)        
                value = random.choice(vector)
                spamWriter.writerow(runSearches(vector, value, sort))
        resultFile.close()

# Executa o programa
if __name__ == "__main__":
    directory = 'src/files/sorted/'
    iterationFiles(directory, ['cubic', 'quadratic', 'sequentialV1', 'sequentialV2', 'binary', 'ternary'], True)
    directory = 'src/files/unsorted/'
    iterationFiles(directory, ['cubic', 'quadratic', 'sequentialV1', 'sequentialV2'], False)