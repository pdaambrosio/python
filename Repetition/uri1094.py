loop = int(input())

test_cases = []
for i in range(loop):
    [num_animal, animal_type] = input().split(' ')
    test_cases.extend([animal_type, int(num_animal)])

rabbits = [test_cases[i + 1] if test_cases[i] == 'C' else 0 for i in range(0, len(test_cases), 2)]
rats = [test_cases[i + 1] if test_cases[i] == 'R' else 0 for i in range(0, len(test_cases), 2)]
frogs = [test_cases[i + 1] if test_cases[i] == 'S' else 0 for i in range(0, len(test_cases), 2)]
total = sum(rabbits + rats + frogs)

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(sum(rabbits)))
print('Total de ratos: {}'.format(sum(rats)))
print('Total de sapos: {}'.format(sum(frogs)))
print('Percentual de coelhos: {:.2f} %'.format((100 * sum(rabbits)) / total))
print('Percentual de ratos: {:.2f} %'.format((100 * sum(rats)) / total))
print('Percentual de sapos: {:.2f} %'.format((100 * sum(frogs)) / total))
