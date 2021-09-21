loop = int(input())

num_in = 0
num_out = 0

for i in range(loop):
    numbers = int(input())
    if 10 <= numbers <= 20:
        num_in += 1
    else:
        num_out += 1

print('{} in'.format(num_in))
print('{} out'.format(num_out))
