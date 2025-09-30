num1 = int(input())
num2 = int(input())
num3 = int(input())
soma12 = num1 + num2
soma13 = num1 + num3

soma23 = num2 + num3

if (num1 != 0 and num2 != 0 and num3 != 0):
    if num1 < soma23 and num2 < soma13 and num3 < soma12:
        print('É possível criar um triangulo')
        if (num1 == num2 and num2 == num3):
            print('O triangulo é equilatero')
        elif num1 == num2 or num2 == num3:
            print('O triangulo é isóceles')
        else:
            print('O triangulo é escaleno')
    else:
        print('Não é possivel formar um triangulo')
else:
    print('Algum ou todos os numeros são iguais a 0, não sendo possível formar triangulo')