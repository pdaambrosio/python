from math import sqrt

while True:
    values = input()

    if values == '0':
        break

    [a, b, c] = map(int, values.split())

    meters = (a * b * 100) / c
    size_of_land = int(sqrt(meters))

    print(size_of_land)
