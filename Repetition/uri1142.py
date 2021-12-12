value = int(input())
total_sum = 1

loop = 0
while loop < value:
    print(f'{total_sum} {total_sum + 1} {total_sum + 2} PUM')
    total_sum += 4
    loop += 1
