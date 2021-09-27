I = 0
J = 1

while I <= 2:
    for l in range(3):
        if I > 2.19:
            print('I={:.0f} J={:.0f}'.format(2, J))
        elif I == 1.0 or I == 0.0 or I > 1.8:
            print('I={:.0f} J={:.0f}'.format(I, J))
        else:
            print('I={:.1f} J={:.1f}'.format(I, J))
        J += 1
    I += 0.2
    J = I + 1
