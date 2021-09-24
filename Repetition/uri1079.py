loop = int(input())

for i in range(loop):
    [n1, n2, n3] = map(float, input().split())
    print('{:.1f}'.format((n1 * 2 + n2 * 3 + n3 * 5) / 10))
