from typing import Counter


[x, y] = map(int, input().split())

numbers = []
for i in range(1, y + 1):
    numbers.append(i)
    if len(numbers) == x:
        print(' '.join(map(str, numbers)))
        numbers = []
