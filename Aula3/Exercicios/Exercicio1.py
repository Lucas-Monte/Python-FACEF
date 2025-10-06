import random

def vectSum(vet):
    s = 0 
    for i in vet:
        s += i
    return s

vect = []
for i in range(5):
    vect.append(random.randint(0,100))

print(vect)

result = vectSum(vect)

print(f'A soma dos elementos do vetor é {result}')