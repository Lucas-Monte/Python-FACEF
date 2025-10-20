def somatorio(n):
    s = 1
    for i in range (2, n + 1, 1):
        s += (i / i**2)
    
    return s

n = int(input('Digite um numero: '))

result = somatorio(n)
print(f'Resultado = {result}')
