salary = float(input())

if salary <= 2000:
    print('Isento')
elif salary <= 3000:
    taxes = (salary - 2000) * 0.08
    print('R$ {:.2f}'.format(taxes))
elif salary <= 4500:
    taxes = ((salary - 3000) * 0.18) + (1000 * 0.08)
    print('R$ {:.2f}'.format(taxes))
else:
    taxes = ((salary - 4500) * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print('R$ {:.2f}'.format(taxes))
