import random

def average(vet):
    s = 0
    for i in vet:
        s += i
    
   
    average = s / len(vet)
    return average

vector = []

for i in range(5):
    vector.append(random.randint(0,99))

print(vector)

result = average(vector)

print(result)