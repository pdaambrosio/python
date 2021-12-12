x = int(input())
x_list = []
x_list.append(x)

for i in range(9):
    x *= 2
    x_list.append(x)

for num, value in enumerate(x_list):
    print(f'N[{num}] = {x_list[num]}')
