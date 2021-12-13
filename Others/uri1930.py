def power_strip(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) - 3

def main():
    [t1, t2, t3, t4] = map(int, input().split())
    print(power_strip(t1, t2, t3, t4))

main()
