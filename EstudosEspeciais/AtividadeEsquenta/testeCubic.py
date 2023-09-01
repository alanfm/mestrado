import src.searches as searches
import random
import time

count = 1000

vector = random.sample(range(0, count * 10), count)

start = time.time()
print(searches.quadratic(vector, vector[10]))
end = time.time()

diff = end - start
print("Quadrático. Tempo gasto: " + str(diff))

start = time.time()
print(searches.cubic(vector, vector[10]))
end = time.time()

diff = end - start
print("Cúbico. Tempo gasto: " + str(diff))