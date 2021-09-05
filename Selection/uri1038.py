[code, amount] = map(int, input().split())

snack_value = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}

for key, value in snack_value.items():
    if code == key:
        total = amount * value
        print('Total: R$ {:.2f}'.format(total))
