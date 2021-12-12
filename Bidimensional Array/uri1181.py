line = int(input())
character = input()
total_sum = 0
average = 0
count = 0

for list_x in range(12):
    for list_y in range(12):
        number = float(input())

        if list_x == line:
            count += 1
            total_sum += number
            average = total_sum / count

print(round(total_sum, 1) if character.upper() == 'S' else round(average, 1))
