def simple_polygons(n, l):
    return n * l


def main():
    [n, l] = map(int, input().split())
    print(simple_polygons(n, l))


main()
