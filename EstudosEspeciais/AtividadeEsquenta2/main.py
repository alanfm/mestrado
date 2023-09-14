import src.searches as searches
import os
import time
import random
import tracemalloc
import csv
import re
import numpy as np

"""
    Pega todos os arquivos que estão no diretório
"""
def parseDirectory(directory):
    directory = os.listdir(directory)
    directory.sort()
    return directory

"""
    Gera um vetor com os dados do arquivo
"""
def generateArray(file):
    start = time.time()
    vector = np.loadtxt(file, dtype=np.int64, delimiter=',')
    result = vector.flatten()
    print('Tamanho do vetor: ' + str(len(result)), '| Tempo gasto para extrair: ' + str(f'{(time.time() - start):.7f}') + ' segundos')
    return result

"""
    Abre o arquivo e retorna os dados em forma de vetor
"""
def parseFile(file, directory = ''):    
    vector = []
    try:
        with open(directory + file, "r") as file:
            vector = generateArray(file)
        file.close()
    except FileNotFoundError:
        print(f"O arquivo {file} não foi encontrado.")
    
    return vector

"""
    Executa a função de busca e retorna o tempo gasto
"""
def runSearches(vector, nameFunction):
    print('Executando função: ' + nameFunction)
    memory = 0
    tracemalloc.start()
    startTime = time.time()
    iterations = 10

    for i in range(iterations):
        if nameFunction == 'maxVal1':
            result = searches.maxVal1(vector)
        elif nameFunction == 'maxVal2':
            result = searches.maxVal2(vector, 0, len(vector) - 1)
        else:
            result = 'Função não encontrada'

    memory += tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    tracemalloc.clear_traces()
    endTime = time.time()
    meddleTime = (endTime - startTime) / iterations

    print('Função: ' + nameFunction, ' | Tamanho do vetor: ' + str(len(vector)), ' | Resultado: ' + str(result))

    return [str(f'{meddleTime:.7f}'), (memory / iterations), nameFunction, str(len(vector)) + '.txt']

"""
    Executa todas as funções de busca e gera o arquivo de resultados
"""
def getResults(directory, algorithms):
    for algorithm in algorithms:
        resultFileName = 'results/' + algorithm + '.csv'

        with open(resultFileName, 'w') as resultFile:
            spamWriter = csv.writer(resultFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamWriter.writerow(['Tempo', 'Memória', 'Algoritmo', 'Arquivo'])

            for file in parseDirectory(directory):
                if (not file.endswith(".txt")):
                    continue
                vector = parseFile(file, directory)
                spamWriter.writerow(runSearches(vector, algorithm))

        resultFile.close()

def main():    
    directory = 'src/files/'
    getResults(directory, ['maxVal1', 'maxVal2'])

if __name__ == '__main__':
    main()