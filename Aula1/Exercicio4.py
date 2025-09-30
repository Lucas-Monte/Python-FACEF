lista = []
for i in range (0, 10, 1):
    lista.append(int(input()))

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