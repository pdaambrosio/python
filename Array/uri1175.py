n_list = []
for i in range(20):
    n_list.append(int(input()))

n_list.reverse()

for index, value in enumerate(n_list):
    print(f'N[{index}] = {value}')
