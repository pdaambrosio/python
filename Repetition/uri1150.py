x = int(input())
z = int(input())

while z <= x:
    z = int(input())

sum = x
count = 1

while sum <= z:
    sum += x + count
    count += 1

print(count)
