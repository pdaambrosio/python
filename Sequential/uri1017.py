hour = int(input())
speed = int(input())

total_distance = hour * speed
fuel = total_distance / 12

print('{:.3f}'.format(fuel))