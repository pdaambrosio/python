t = int(input())
n_list = []

for i in range (1000):
    count = 0
    while count < t:
        n_list.append(count)
        count += 1
    print(f'N[{i}] = {n_list[i]}')
