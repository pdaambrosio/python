values = [int (x) for x in input().split(' ')]

values_sorted = values.copy()
values_sorted.sort()

print(*values_sorted, sep='\n')
print()
print(*values, sep='\n')