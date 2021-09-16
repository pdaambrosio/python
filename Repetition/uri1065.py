even_number = 0

for i in range(5):
    number = int(input())
    if number % 2 == 0:
        even_number += 1

print('{} valores pares'.format(even_number))
