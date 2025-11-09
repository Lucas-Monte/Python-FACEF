# Lucas Antonio Monteiro
import random
def menu():
    print("MENU DE OPÇÕES")
    print("--------------")
    print("   1 - MODA   ")
    print("   2 - MENOR  ")
    print("   3 - MÉDIA  ")
    print("  -1 - SAIR  ")
    print("--------------")

def moda(tamanhoVetor):
    vet = []
    for i in range(tamanhoVetor):
        vet.append(random.randint(0, 10))
    
    print(vet)
    dic = {}
    for i in vet:
        dic[i] = dic.get(i, 0) + 1
    print(dic)

    maior = 0
    item = {}
    iguais = 0
    for i in dic:
        if dic[i] > maior:
            maior = dic[i]
            item[i] = dic.get(i, 0)
    
    for i in dic.values():
        if i == maior:
            iguais += 1

    if iguais > 1:
        return print("Não possui moda, pois existem mais de 1 valor que se repete igualmente.")
    else:
        moda1 = item.popitem()
        return print(f"A moda é {moda1[0]}")
    

def menorElemento(tamanhoLista):
    lista = []
    for i in range(tamanhoLista):
        lista.append(random.randint(-99, 99))
    
    print(lista)

    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    
    return menor

def mediaImpares():
    vetor = []
    for i in range(20):
        vetor.append(random.randint(0,99))
    print(vetor)
    soma = 0
    quantidade = 0
    for i in range(1, len(vetor), 2):
        soma += vetor[i]
        quantidade += 1

    media = soma/quantidade
    return media

menu()
opcao = int(input("Escolha uma opção: "))
while (opcao != -1):
    if opcao == 1:
        tamanho = int(input("Digite o tamanho do vetor: "))
        moda(tamanho)
    elif opcao == 2:
        tamanho = int(input("Digite o tamanho da lista: "))
        resultado = menorElemento(tamanho)
        print(f"O menor elemento é o {resultado}")

    elif opcao == 3:
        resultado = mediaImpares()
        print(f"A média dos valores nas posições impares do vetor é: {resultado}")
    else:
        print("Opção inválida, escolha novamente")

    menu()
    opcao = int(input("Escolha uma opção: "))

print("Você Saiu!")