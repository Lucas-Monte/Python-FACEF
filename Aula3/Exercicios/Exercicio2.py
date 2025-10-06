import random

def evenAverageVector(vet):
    s = 0
    average = 0
    even = 0
    for i in vet:
        if i % 2 == 0:
            s += i
            even += 1
    if s == 0:
        return 'Não houve numeros pares'
    else:
        average = s / even
        return average
    
vector = []

for i in range(10):
    vector.append(random.randint(1,99))

print(vector)

result = evenAverageVector(vector)

print(result)