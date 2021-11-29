[a, b] = map(int, input().split())


def quotient_division(a, b):
    for i in range(abs(b)):
        if (a - i) % b == 0:
            result = int((a - i) / b)
            print(result, i)
            break


quotient_division(a, b)
