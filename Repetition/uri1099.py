loop = int(input())

for i in range(loop):
    sum_odd = 0
    numbers = list(map(int, input().split()))
    for odd_number in range(min(numbers) + 1, max(numbers)):
        if odd_number % 2 != 0:
            sum_odd += odd_number
    print(sum_odd)
