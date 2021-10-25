x_array = []

for i in range(100):
    x = float(input())
    if x <= 10:
        x_array.append(x)
        print(f'A[{i}] = {x}')
