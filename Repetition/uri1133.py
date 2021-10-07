values = []

for i in range(2):
    values.append(int(input()))

for value in range(min(values) + 1, max(values)):
    if value % 5 == 2 or value % 5 == 3:
        print(value)
