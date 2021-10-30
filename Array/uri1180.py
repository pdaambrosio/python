n = int(input())
x_list = list(map(int, input().split()))

print(f'Menor valor: {min(x_list[:n])}')
print(f'Posicao: {x_list.index(min(x_list[:n]))}')
