def scientific_notation(number):
    from decimal import Decimal

    if Decimal(number) >= 0 and '-' != number[0]:
        print('+', end='')

    print('%.4E' % Decimal(number))


def main():
    value = input()
    scientific_notation(value)


main()
