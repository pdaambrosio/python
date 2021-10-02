loop = int(input())

for i in range(loop):
    [x, y] = map(int, input().split())
    if y == 0:
        print('divisao impossivel')
    else:
        dividing = x / y
        print(round(dividing, 2))
