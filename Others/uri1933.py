def tri_du(n1, n2):
    larger_value = n1

    if n1 < n2:
        larger_value = n2

    return larger_value


def main():
    [c1, c2] = map(int, input().split())
    print(tri_du(c1, c2))


main()
