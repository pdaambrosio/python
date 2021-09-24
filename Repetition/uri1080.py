values = []

i = 0
while i < 100:
    i += 1
    values.append(int(input()))

print(max(values))
print(values.index(max(values)) + 1)
