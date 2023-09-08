import random

"""
    Gera um arquivo com os dados
"""
def generate(max: int):
    count = 0
    result = ''
    iterations = 0
    file = open('files/' + str(max) + '.txt', 'w')
    while iterations < max:
        iterations += 1
        if count < 9 and iterations < max:
            result += str(random.randint(1, max)) + ', '
            count += 1
            continue
        else:
            result += str(random.randint(1, max)) + ' \n'
            file.write(result)
            result = ''
            count = 0

    return file.close()

"""
    Gera todos os arquivos
"""
def main():
    values = [100, 200, 2000, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000]

    for value in values:
        print('Gerando arquivo ' + str(value))
        generate(value)
    
    print('Arquivos gerados com sucesso!')

if __name__ == '__main__':
    main()