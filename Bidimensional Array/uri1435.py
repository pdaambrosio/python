while True:
    number = int(input())

    if number == 0:
        break

    if number % 2 == 0:
        square = number // 2
    else:
        square = (number + 1) // 2

    matrix = []

    for line in range(number):
        matrix.append([])
        for column in range(number):
            matrix[line].append(1)

    first = 0
    last = number
    count = 0

    for increment in range(square):
        count += 1
        for line in range(first, last):
            for column in range(first, last):
                matrix[line][column] = count
                
        first += 1
        last -= 1
    
    for line in range(number):
        result = ''
        for column in range(number):
            result += f' {matrix[line][column]:3d}'  # 3d: display an integer and reserve 3 spaces for it
        print(result[1:])
    print()
