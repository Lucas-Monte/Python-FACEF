alunos = int(input("Digite a quantidade de alunos: "))
prova = []
trabalho = []

for i in range(alunos):
    prova.append(float(input("Digite a nota da prova: ")))
    trabalho.append(float(input("Digite a nota do trabalho: ")))
    

print(prova)
print(trabalho)

soma = 0
alunos6 = 0
alunosProva = 0
for i in range(alunos):
    if (prova[i] + trabalho[i]) > 6:
        alunos6 += 1
    if prova[i] > trabalho[i]:
        alunosProva += 1
    soma += prova[i] + trabalho[i]

media = soma / alunos
alunosMedia = 0
for i in range(alunos):
    if (prova[i] + trabalho[i]) > media:
        alunosMedia += 1

print(f"Alunos que tiveram nota da prova melhor que do trabalho: {alunosProva}")
print(f"Alunos com soma maior que 6: {alunos6}")
print(f"Média: {media}")
print(f"Alunos com nota maior que a média: {alunosMedia}")