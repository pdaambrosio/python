def sequence_of_sequence(case, number):
    result = [0]
    
    for i in range(0, number + 1):
        result += [i] * i
    
    if len(result) > 1:
        print(f'Caso {case}: {len(result)} numeros')
    else:
        print(f'Caso {case}: {len(result)} numero')
    
    print(*result)
    print()


def main():
    case = 1
    while True:
        try:
            input_number = int(input())
            sequence_of_sequence(case, input_number)
        except EOFError:
            break
        case += 1


main()
