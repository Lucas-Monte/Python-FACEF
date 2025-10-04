notas = []
soma = 0
acima = 0
abaixo = 0
for i in range(5):
    notas.append(float(input(f"Adicione a {i+1}° nota: ")))

for i in notas:
    soma += i

media = soma / 5

print(f"Media: {media}")

for i in notas:
    if i > media*1.1:
        acima += 1
    elif i < media*0.90:
        abaixo += 1

print(f"Notas '10%' acima da média: {acima}")
print(f"Notas '10%' abaixo da média: {abaixo}")