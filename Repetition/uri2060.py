def binos_challenge(loop: int, numbers: list[int]) -> str:
    multiple_two: int = 0
    multiple_tree: int = 0
    multiple_for: int = 0
    multiple_five: int = 0

    for i in range(loop):
        if numbers[i] % 2 == 0:
            multiple_two += 1
        if numbers[i] % 3 == 0:
            multiple_tree += 1
        if numbers[i] % 4 == 0:
            multiple_for += 1
        if numbers[i] % 5 == 0:
            multiple_five += 1

    return f'{multiple_two} Multiplo(s) de 2\n{multiple_tree} Multiplo(s) de 3\n{multiple_for} Multiplo(s) de 4\n{multiple_five} Multiplo(s) de 5'


if __name__ == '__main__':
    N: int = int(input())
    L: list = list(map(int, input().split()))
    print(binos_challenge(N, L))
