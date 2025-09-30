lista = []
num = int(input())
i = 0
while num != 0:
    lista.append(int(input()))
    num = lista[i]
    if num == 0:
        lista.pop()
    i += 1
soma = 0
quant = 0
for i in lista:
    if i % 2 == 0:
        soma += i
        quant += 1

if quant > 0:
    media = soma / quant
    print(f'A médias dos numeros pares é {media}')
else:
    print('Não houve numeros pares')