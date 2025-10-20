import random

def bigger(vect):
    bigger = vect[0]
    for i in vect:
        if i > bigger:
            bigger = i
    
    return bigger

vect = []

for i in range(5):
    vect.append(random.randint(0,10))

print(vect)
result = bigger(vect)

print(f'O maior elemento do vetor é o {result}')