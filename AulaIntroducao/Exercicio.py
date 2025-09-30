soma = 0
par = 0
for i in range (0, 10, 1):
    numero = int(input('digite o %i° numero: ' %(i)))
    if numero % 2 == 0:
        soma += numero
        par += 1

if par > 0:
    print('A média dos numeros pares é %.2f' %(soma/par))
else:
    print('Não teve numeros pares')
