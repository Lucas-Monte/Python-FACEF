soma = 0
for i in range (1, 500, 1):
    if i % 3 == 0:
        if i % 2 != 0:
            soma += i

print(f'A quantidade de numeros multiplos de 3 e impares é de {soma}')