import random

def media(vect):
    s = 0
    q = 0
    for i in range(1, len(vect), 2):
        s += vect[i]
        q += 1

    media = s / q
    return media

vect = []

for i in range(5):
    vect.append(random.randint(0,99))

print(vect)

result = media(vect)

print(f'A média dos elementos nas posições impares é de {result}')