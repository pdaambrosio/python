x = int(input())

while x != 0:

    even_numbers = []
    loop = 0
    while loop < 5:
        if x % 2 == 0:
            even_numbers.append(x)
            loop += 1
        x += 1

    print(sum(even_numbers))
    x = int(input())
