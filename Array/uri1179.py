even_numbers = []
odd_numbers = []

for i in range(15):
    number = int(input())

    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
    
    if len(even_numbers) == 5:
        for n in range(len(even_numbers)):
            print(f'par[{n}] = {even_numbers[n]}')
        even_numbers.clear()

    if len(odd_numbers) == 5:
        for n in range(len(odd_numbers)):
            print(f'impar[{n}] = {odd_numbers[n]}')
        odd_numbers.clear()

for n in range(len(odd_numbers)):
    print(f'impar[{n}] = {odd_numbers[n]}')

for n in range(len(even_numbers)):
    print(f'par[{n}] = {even_numbers[n]}')
