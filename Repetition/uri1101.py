loop = 0
while loop == 0:
    numbers = list(map(int, input().split()))
    if min(numbers) > 0 and max(numbers) > 0:
        values = [num for num in range(min(numbers), max(numbers) + 1)]
        print(*values, 'Sum={}'.format(sum(values)))
    else:
        loop += 1

# Python 3.5+ Unpacking Generalizations (https://www.python.org/dev/peps/pep-0448/)
