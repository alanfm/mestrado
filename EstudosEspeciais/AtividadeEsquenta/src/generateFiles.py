# Gera o arquivo com os dados
import random

def vector(max: int, sorted: bool):
    count = 0
    result = ''
    iteration = 0
    if sorted:
        file = open('files/sorted/' + str(max) + '.txt', 'w')
        while iteration < max:
            iteration += 1
            if count < 9 and iteration < max:
                result += str(iteration + random.randint(1, 2)) + ', '
                count += 1
            else:
                result += str(iteration + random.randint(1, 2)) + ' \n'
                file.write(result)
                result = ''
                count = 0
    else:        
        file = open('files/unsorted/' + str(max) + '.txt', 'w')
        while iteration < max:
            iteration += 1
            if count < 9 and iteration < max:
                result += str(random.randint(1, max)) + ', '
                count += 1
            else:
                result += str(random.randint(1, max)) + ' \n'
                file.write(result)
                result = ''
                count = 0

    return file.close()

values = [100, 200, 2000, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000]

for key, value in enumerate(values):
    vector(value, True)
    vector(value, False)