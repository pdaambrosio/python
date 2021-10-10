loop = int(input())
seq_numbers = []

while loop != 0:
    for i in range(1, loop + 1):
        seq_numbers.append(i)
    print(' '.join(map(str, seq_numbers)))
    seq_numbers = []
    loop = int(input())
