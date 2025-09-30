nome = input('nome: ')
idade = int(input('Idade: '))
nota = float(input('Digite sua nota: '))

print('%s possui %d anos e nota %.2f' %(nome, idade, nota))

print('{0} possui {1} anos e nota {2: .2f}' .format(nome, idade, nota))
print('{} possui {} anos e nota {: .2f}' .format(nome, idade, nota))

print(f'{nome} possui {idade} anos e nota {nota: .2f}')