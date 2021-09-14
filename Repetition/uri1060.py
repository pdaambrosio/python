positive_numbers = 0

for i in range(0, 6):
    numbers = float(input())
    if numbers > 0:
        positive_numbers += 1
        
print('{} valores positivos'.format(positive_numbers))
