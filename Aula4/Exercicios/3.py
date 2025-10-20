def verifica(cpf):
    s1 = 0
    aux1 = 10
    for i in range(9):
        s1 += int(cpf[i])*aux1
        aux1 -= 1

    resto1 = s1 % 11
    res1 = True
    res12 = True    
    s2 = 0
    aux2 = 11
    for i in range(10):
        s2 += int(cpf[i])*aux2
        aux2 -= 1

    resto2 = s2 % 11
    res2 = True
    res22 = True

    if (resto1 == 1 or resto1 == 0):
        if int(cpf[9]) != 0:
            res1 = False
    else:
        dig1 = 11 - resto1
        if int(cpf[9]) != dig1:
            res12 = False

    if (resto2 == 1 or resto2 == 0):
        if int(cpf[10]) != 0:
            res2 = False
    else:
        dig2 = 11 - resto2
        if int(cpf[10]) != dig2:
             res22 = False
    
    if res1 == True and res12 == True and res2 == True and res22 == True:
        return True
    else:
        return False

    
cpf = input('Digite o CPF: ')
print(cpf)
resultado = verifica(cpf)

print(resultado)    
    

    