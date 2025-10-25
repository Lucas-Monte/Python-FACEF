numeros = [0,0,0,0,0,5,6,3,2,1,8,9,4,5,6,1,2,8,7,15,-2,-9,-6,-5,-4,-1]

zeros = numeros.count(0)

print(zeros)

numeros = [n for n in numeros if n!=0]

numeros.extend([0] * zeros)

print(numeros)