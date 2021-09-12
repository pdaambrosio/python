value = int(input())

reference_table = {61: 'Brasilia', 71: 'Salvador', 11: 'Sao Paulo', 21: 'Rio de Janeiro', 32: 'Juiz de Fora', 19: 'Campinas', 27: 'Vitoria', 31: 'Belo Horizonte'}

for ddd, city in reference_table.items():
    if value == ddd:
        print(city)
        break
else:
    print('DDD nao cadastrado')
