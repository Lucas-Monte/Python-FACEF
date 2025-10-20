import random

def maior(vetor):
    maior = vetor[0]
    for i in vetor:
        if i > maior:
            maior = i

    return maior

def segMaior(vetor):
    maior1 = maior(vetor)
    seg = vetor[0]
    if maior1 == seg:
        seg = vetor[1]

    for i in vetor:
        if i > seg and i < maior1:
            seg = i

    return seg

vetor = []

for i in range(5):
    vetor.append(random.randint(0,99))

print(vetor)

maiorV = maior(vetor)
segMaiorV = segMaior(vetor)

print(f'Maior valor = {maiorV} e segundo maior {segMaiorV}')