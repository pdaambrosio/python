values = list(map(int, input().split()))
a = values.pop(0)
n = [num for num in values if num > 0]

total = 0
for i in range(int(*n)):
    total += a + i

print(total)
