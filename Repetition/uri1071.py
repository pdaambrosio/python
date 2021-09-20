number_1 = int(input())
number_2 = int(input())
sum_odd_numbers = 0

for num in range((min(number_1, number_2) + 1), max(number_1, number_2)):
    if num % 2 != 0:
        sum_odd_numbers += num

print(sum_odd_numbers)
