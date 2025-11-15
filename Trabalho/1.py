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

def criaVetor(qtdElementos) :
    vet = []
    for i in range(qtdElementos):
        vet.append(random.randint(0, 15))
    print(vet)
    return vet
    
   
def moda(vetor):
    vet = vetor
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
        return 0
    else:
        moda1 = item.popitem()
        return moda1[0]
    

def menorElemento(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    
    return menor

def mediaImpares(vetor):
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
        vetor = criaVetor(tamanho)
        resultado = moda(vetor)
        if resultado == 0:
            print("Não ha moda, pois existe mais de um elemento que se repete igualmente.")
        else:
            print(f"A moda é {resultado}")
    elif opcao == 2:
        tamanho = int(input("Digite o tamanho da lista: "))
        lista = criaVetor(tamanho)
        resultado = menorElemento(lista)
        print(f"O menor elemento é o {resultado}")

    elif opcao == 3:
        vetor = criaVetor(20)
        resultado = mediaImpares(vetor)
        print(f"A média dos valores nas posições impares do vetor é: {resultado}")
    else:
        print("Opção inválida, escolha novamente")

    menu()
    opcao = int(input("Escolha uma opção: "))

print("Você Saiu!")