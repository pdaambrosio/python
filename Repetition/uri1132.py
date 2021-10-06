sum = 0
values = []
x = values.append(int(input()))
y = values.append(int(input()))

for value in range(min(values), max(values) + 1):
    if value % 13 != 0:
        sum += value

print(sum)
