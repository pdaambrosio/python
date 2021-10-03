new_calculate = 1
while new_calc == 1:
    loop = 0
    average = 0
    while loop < 2:
        score = float(input())
        if score >= 0 and score <= 10:
            average += score / 2
            loop +=1
        else:
            print('nota invalida')
    print(f'media = {average:.2f}')
    
    print('novo calculo (1-sim 2-nao)')
    new_calc = int(input())

    while new_calc != 1 and new_calc != 2:
        print('novo calculo (1-sim 2-nao)')
        new_calculate = int(input())
