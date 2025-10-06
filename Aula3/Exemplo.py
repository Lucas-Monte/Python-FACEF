def lowestValue(a, b):
    if (a < b):
        return f'{a} é o menor valor'
    elif (b < a):
        return f'{b} é o menor valor'
    else:
        return 'Ambos são iguais'
    
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

resultado = lowestValue(x, y)

print(resultado)