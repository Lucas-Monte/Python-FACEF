alunos = int(input('Informe a quantidade de alunos: '))
soma = 0
nota = []
acimaMedia = 0

for i in range(alunos):
    nota.append(float(input(f"Informe a nota do {i + 1}° aluno: ")))
    while (nota[i] < 0) or (nota[i] > 10):
        print("Nota inválida!")
        nota[i] = (float(input(f"\nInforme a nota do {i + 1}° aluno: ")))

for i in range(alunos):
    print(nota[i])
    
        
    soma += nota[i]

media = soma / alunos
print(f"Média: {media}")

for i in range(alunos):
    if (nota[i] > media):
        acimaMedia += 1

if acimaMedia == 1:
    print(f"Teve ao todo {acimaMedia} nota acima da média")
elif acimaMedia > 1:
    print(f"Tiveram ao todo {acimaMedia} notas acima da média")
else:
    print(f"Todas as notas são iguais, não tendo ninguem acima da média.")