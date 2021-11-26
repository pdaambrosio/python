number_of_players = int(input())

for case in range(1, (number_of_players + 1)):
    [player1, player2] = input().split()

    if player1 == player2:
        print(f'Caso #{case}: De novo!')
    elif player1 == 'pedra':
        if player2 == 'tesoura' or player2 == 'lagarto':
            print(f'Caso #{case}: Bazinga!')
        else:
            print(f'Caso #{case}: Raj trapaceou!')
    elif player1 == 'papel':
        if player2 == 'pedra' or player2 == 'Spock':
            print(f'Caso #{case}: Bazinga!')
        else:
            print(f'Caso #{case}: Raj trapaceou!')
    elif player1 == 'tesoura':
        if player2 == 'lagarto' or player2 == 'papel':
            print(f'Caso #{case}: Bazinga!')
        else:
            print(f'Caso #{case}: Raj trapaceou!')
    elif player1 == 'lagarto':
        if player2 == 'Spock' or player2 == 'papel':
            print(f'Caso #{case}: Bazinga!')
        else:
            print(f'Caso #{case}: Raj trapaceou!')
    elif player1 == 'Spock':
        if player2 == 'tesoura' or player2 == 'pedra':
            print(f'Caso #{case}: Bazinga!')
        else:
            print(f'Caso #{case}: Raj trapaceou!')
