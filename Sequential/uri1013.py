[a, b, c] = map(int, input().split())

major_ab = (a + b + abs(a - b)) / 2
major_c = (c + major_ab + abs(c - major_ab)) / 2

print('{} eh o maior'.format(int(major_c)))
