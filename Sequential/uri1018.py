val = int(input())
banknotes = [100, 50, 20, 10, 5, 2, 1]

print(val)

for note in banknotes:
    amount_notes = int(val / note)
    print('%s nota(s) de R$ %s,00' %(amount_notes, note))
    val = val % note
