import numpy as np
import random
import src.searches as searches

def main():
    vector = np.array(range(100000000))
    value = random.choice(vector)
    print('Tamanho do vetor: ' + str(len(vector)), '| Valor pesquisado: ' + str(value), '| Resultado: ' + str(searches.binary(vector, value, 0, len(vector) - 1)))

if __name__ == "__main__":
    main()