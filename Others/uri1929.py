def lengths(a, b, c):
    if abs((b - c)) < a < (b + c):
        if abs((a - c)) < b < (a + c):
            if abs((a - b)) < c < (a + b):
                return True
    return False


def triangle(a, b, c, d):
    if lengths(a, b, c) or lengths(a, b, d) or lengths(a, c, d) or lengths(b, c, d):
        return 'S'
    return 'N'


def main():
    [a, b, c, d] = map(int, input().split())
    print(triangle(a, b, c, d))


main()
