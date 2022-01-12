def pronalancia_puzzle(numbers):
    numbers = str(numbers)
    return numbers[::-1]


def main():
    number_found = int(input())
    print(pronalancia_puzzle(number_found))


main()
