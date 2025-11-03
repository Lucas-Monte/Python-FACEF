nome = input("Digite o nome do arquivo: ")

arquivo = open(f"D:/Usuários/25993/Desktop/Python-FACEF/Aula7/{nome}.txt", "r")
dic = {}

for i in arquivo:
    palavra = i.split()
    for p in palavra:
        dic[p] = dic.get(p, 0) + 1


print(dic)