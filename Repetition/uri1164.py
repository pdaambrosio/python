loop = int(input())

for n in range(loop):
    x = int(input())
    sum_num = 0
    for num in range(1, x):
        if x % num == 0:
            sum_num += num

    print(f'{x} eh perfeito' if x == sum_num else f'{x} nao eh perfeito')
