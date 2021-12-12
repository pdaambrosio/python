even_numbers = []
odd_numbers = []

for i in range(15):
    number = int(input())

    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

    if len(even_numbers) == 5:
        for index, value in enumerate(even_numbers):
            print(f'par[{index}] = {value}')
        even_numbers.clear()

    if len(odd_numbers) == 5:
        for index, value in enumerate(odd_numbers):
            print(f'impar[{index}] = {value}')
        odd_numbers.clear()

for index, value in enumerate(odd_numbers):
    print(f'impar[{index}] = {value}')

for index, value in enumerate(even_numbers):
    print(f'par[{index}] = {value}')