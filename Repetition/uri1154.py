# from functools import reduce

data = 0
ages = []

while data >= 0:
    data = int(input())
    ages.append(data)

ages = list(filter(lambda n: n >= 0, ages))
# average = reduce(lambda n1, n2: n1 + n2, ages) / len(ages)
average = sum(ages) / len(ages)

print(f'{average:.2f}')
