# tupla = ()
# print(type(tupla))

# tupla = (1)
# print(type(tupla))

# tupla = (1,)
# print(type(tupla))

# aluno1 = ("Ricardo", 1.85, 22)
# aluno2 = ("Luiza", 1.65, 23)

# alunos = aluno1 + aluno2

# print(aluno1)
# print(aluno2)
# print(alunos)

# print(alunos[1])
# alunos[1] = 1.95
# print(alunos)

# dic = {}

# dic = {"um": "one", "dois": "two", "tres": "three"}
# print(dic["dois"])

# dic["dois"] = 2

# print(dic)
# # clear(), copy(), get(chave, valor), items(), keys(), values()

# dic1 = dic.copy()
# print(dic)
# print(dic1)

# dic1["tres"] = 3
# print(dic1)

# print(dic.get("cinco", "Não encontrado!"))
# print(dic.get("dois", "Nao encontrado!"))

# print(dic1.keys())
# print(dic.items())
# print(dic1.values())

arquivo = open("D:/Usuários/25993/Desktop/Python-FACEF/Aula7/text.txt", "r")
for linha in arquivo:
    vetor = linha.split()
    for palavra in vetor:
        print(palavra)
