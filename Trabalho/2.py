nome = input("Digite o nome do arquivo: ")
arquivo = open(f"C:/Users/Lucas Monteiro/Desktop/FACEF/Python - FACEF/Trabalho/{nome}.txt", "r")
arquivoStopWords = open("C:/Users/Lucas Monteiro/Desktop/FACEF/Python - FACEF/Trabalho/stopwords.txt", "r")

dic = {}
stopWords = []

for i in arquivo:
    palavra = i.split()
    for p in palavra:
        p = p.lower()
        dic[p] = dic.get(p, 0) + 1

for i in arquivoStopWords:
    words = i.split()
    for palavras in words:
        stopWords.append(palavras)

print(dic)
print("\n\nStopWords")
print(stopWords)

dicCerto = {palavra: rep for palavra, rep in dic.items() if palavra not in stopWords}

# for i in dic:
#     for p in stopWords:
#         if i == p:
#             dic.pop(i)

print(f"\n\n\n\n{dicCerto}")

maior = 0
palavra = {}
for i in dicCerto:
    if dicCerto[i] > maior:
        maior = dicCerto[i]
        palavra[i] = dicCerto.get(i, 0)

palavraMaisRepetida = palavra.popitem()

print(f"A palavra mais falada foi '{palavraMaisRepetida[0]}' repetida {palavraMaisRepetida[1]} vezes")