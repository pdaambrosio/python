def sunday_morning(woken_up):
    [hours, minutes] = map(int, str(woken_up).split(':'))
    hours_result = (hours * 60) + (minutes - 420)
    return max(0, hours_result)


def main():
    while True:
        try:
            bino_woken_up = sunday_morning(input())
            print(f'Atraso maximo: {bino_woken_up}')
        except EOFError:
            break


main()
