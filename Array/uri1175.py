n_list = []
for i in range(20):
    n_list.append(int(input()))

n_list.reverse()

for i in range(len(n_list)):
    print(f'N[{i}] = {n_list[i]}')
