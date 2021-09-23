value = int(input())

for num in range(1, value + 1):
    if num % 2 == 0:
        square = pow(num, 2)
        print('{}^2 = {}'.format(num, square))
