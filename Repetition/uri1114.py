loop = 0
while loop == 0:
    password = int(input())
    if password != 2002:
        print('Senha Invalida')
    else:
        loop += 1
        print('Acesso Permitido')
