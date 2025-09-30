for i in range (10, 0, -1):
    if i == 10:
        print('10:00')
    else:
        for j in range (59, 0, -1):
            if i == 10:
                j = 0
            print (f'{i}:{j}')