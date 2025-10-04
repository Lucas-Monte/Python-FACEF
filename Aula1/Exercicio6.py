import random

numero = random.randint(0, 100)

print("Escolha um numero")

chute = int(input())
tentativa = 1

while(chute != numero):
    if (chute > numero):
        print("O numero é menor!")
    else:
        print("O numero é maior!")
    tentativa += 1
    print("Tente novamente: ")
    chute = int(input())

print(f"Você acertou com {tentativa} tentativa(s)")