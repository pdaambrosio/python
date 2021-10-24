x = int(input())
x_list = []
x_list.append(x)

for i in range(9):
    x *= 2
    x_list.append(x)

for num in range(len(x_list)):
    print(f'N[{num}] = {x_list[num]}')
