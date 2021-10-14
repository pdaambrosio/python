n = int(input())

fibonacci_t1 = 0
fibonacci_t2 = 1
fibonacci_sequence = []

if n < 2:
    fibonacci_sequence.append(fibonacci_t1)
else:
    fibonacci_sequence.extend([fibonacci_t1, fibonacci_t2])

count = 3
while count <= n:
    count += 1
    fibonacci_t3 = fibonacci_t1 + fibonacci_t2
    fibonacci_sequence.append(fibonacci_t3)
    fibonacci_t1 = fibonacci_t2
    fibonacci_t2 = fibonacci_t3


print(' '.join(map(str, fibonacci_sequence)))
