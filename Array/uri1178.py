x_list = []
x = x_list.append(float(input()))

for i in range(100):
    x_list.append(x_list[i] / 2)
    print(f'N[{i}] = {x_list[i]:.4f}')
