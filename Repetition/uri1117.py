average = 0
loop = 0

while loop < 2:
    score = float(input())
    if score >= 0 and score <= 10:
        average += score / 2
        loop += 1
    else:
        print('nota invalida')

print(f'media = {average:.2f}')
