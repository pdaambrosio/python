types_fuel = {'Alcool': 0,'Gasolina': 0,'Diesel': 0}

control = 0
while control != 4:
    control = int(input())
    if control == 1:
        types_fuel['Alcool'] += 1
    elif control == 2:
        types_fuel['Gasolina'] += 1
    elif control == 3:
        types_fuel['Diesel'] += 1

print('MUITO OBRIGADO')
print(f"Alcool: {types_fuel['Alcool']}")
print(f"Gasolina: {types_fuel['Gasolina']}")
print(f"Diesel: {types_fuel['Diesel']}")
