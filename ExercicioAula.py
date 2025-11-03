def mensagem():
    print("Escolha uma opção")
    print("1 - Tabuada")
    print("2 - IMC")
    print("3 - Fatorial")
    print("-1 para sair")

def tabuada(n):
    if n < 1 or n > 9:
        print("Erro")
    else:
        for i in range (1, 11):
            print(f"{i} x {n} = {n*i}")

def imc(p, a):
    r = p / (a**2)
    return r

def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

opcao = int(input())

while opcao != -1:
    if opcao == 1:
        print("Digite um numero")
        n = int(input())
        tabuada(n)
    elif opcao == 2:
        print("Digite o peso")
        p = float(input())
        print("Digite a altura")
        a = float(input())
        r = imc(p, a)
        print(f"IMC = {r}")
    elif opcao == 3:
        print("Digite um numero")
        num = int(input())
        res = fatorial(num)
        print(f"Fatorial = {res}")
    
    mensagem()
    opcao = int(input())


print("Você Saiu!")