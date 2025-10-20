alunos = int(input("Digite a quantidade de alunos: "))

notas = []
for i in range(0, alunos):
    notas.append(float(input(f"Digite a {i+1}° nota: ")))

soma = 0
for i in notas:
    soma += i

if alunos == 0:
    print('Não houve alunos')
else:
    media = soma / len(notas)
    print(f"A média das notas é {media}")
    print("Notas acima da média: ")
    for i in notas:
        if i > media:
            print(i)