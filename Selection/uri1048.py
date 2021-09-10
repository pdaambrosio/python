salary = float(input())

if salary <= 400:
    readjustment = 15
elif salary <= 800:
    readjustment = 12
elif salary <= 1200:
    readjustment = 10
elif salary <= 2000:
    readjustment = 7
else:
    readjustment = 4

print('Novo salario: {:.2f}'.format(salary + (salary * readjustment/100)))
print('Reajuste ganho: {:.2f}'.format(salary * readjustment/100))
print('Em percentual: {} %'.format(readjustment))
