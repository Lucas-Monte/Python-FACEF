lista = [1, 2, 3]
print(lista)
lista = lista + [4]
print (lista)
lista = lista + [0,0,4]
print (lista)


for i in range (0, 10, 1):
    print (i)

for i in range (10, 0, -2):
    print (i)

for i in range (10):
    print (i)

nome = ['pedro', 'Ana', 'Maria']
for n  in nome:
    print(n)
    #imprime os elementos da lista

i = 0
while(i < 10):
    print(i)
    i += 1
    #i++ não existe

conta = 0
x = 2

while (conta <= 5):
    print(x)
    conta += 1
else:
    print(f'Valor da variavel conta é {conta}')