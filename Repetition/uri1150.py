x = int(input())
z = int(input())

while z <= x:
    z = int(input())

total_sum = x
count = 1

while total_sum <= z:
    total_sum += x + count
    count += 1

print(count)
