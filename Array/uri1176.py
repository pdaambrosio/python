fibonacci_t1 = 0
fibonacci_t2 = 1
fibonacci_sequence = [0, 1]

for i in range(60):
    fibonacci_t3 = fibonacci_t1 + fibonacci_t2
    fibonacci_sequence.append(fibonacci_t3)
    fibonacci_t1 = fibonacci_t2
    fibonacci_t2 = fibonacci_t3

loop = int(input())
for i in range(loop):
    n = int(input())
    print(f'Fib({n}) = {fibonacci_sequence[n]}')
