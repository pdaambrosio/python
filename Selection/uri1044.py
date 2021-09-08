[a, b] = map(int, input().split())

are_multiples = ['Sao Multiplos' if a % b == 0 or b % a == 0 else 'Nao sao Multiplos']

print(are_multiples[0])