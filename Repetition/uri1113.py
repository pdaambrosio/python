loop = 0
while loop == 0:
    x, y = map(int, input().split())
    if x > y:
        print('Decrescente')
    elif y > x:
        print('Crescente')
    else:
        loop += 1
