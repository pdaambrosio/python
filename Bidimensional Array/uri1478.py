while True:
    number = int(input())

    if number == 0:
        break

    matrix = []

    for line in range(number + 1):
        count = line
        matrix.append([])
        for column in range(number):
            matrix[line].append(abs(count))

            if count == 1:
                count -= 3
            else:
                count -= 1

    for line in range(1, (number + 1)):
        result = ''
        for column in range(number):
            result += f' {matrix[line][column]:3d}'  # 3d: display an integer and reserve 3 spaces for it
        print(result[1:])
    print()
