n = int(input())

for i in range(n):
    sum_odd = 0
    [x, y] = map(int, input().split())
    for number in range(x, x + (y * 2)):
        if number % 2 != 0:
            sum_odd += number
    print(sum_odd)
