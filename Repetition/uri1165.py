loop = int(input())

for i in range(loop):
    x = int(input())
    prime_number = (num for num in range(1, x + 1) if x % num == 0)
    print(f'{x} eh primo' if len(list(prime_number)) == 2 else f'{x} nao eh primo')
