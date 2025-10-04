vet1 = []

for i in range(30):
    vet1.append(int(input(f"Adicione o {i + 1}° numero: ")))

print(vet1)
vet2 = vet1.copy()
vet2.reverse()
print(vet2)

