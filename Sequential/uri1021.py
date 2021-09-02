banknotes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

value = float(input())

print('NOTAS:')

for note in banknotes:
    amount_notes = int(value / note)
    print('{} nota(s) de R$ {:.2f}'.format(amount_notes, note))
    value = value % note

print('MOEDAS:')

for coin in coins:
    amount_coins = int(value / coin + 0.00001)
    print('{} moeda(s) de R$ {:.2f}'.format(amount_coins, coin))
    value = value % coin
