positives = []

for i in range(6):
    number = float(input())
    if number > 0:
        positives.append(number)
    
average = sum(positives) / len(positives)

print("{} valores positivos".format(len(positives)))
print('{:.1f}'.format(average))
