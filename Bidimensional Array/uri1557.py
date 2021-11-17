while True:
    num = int(input())

    if num == 0:
        break
    elif num == 1:
        print(num)
    else:
        matrix = []
        value = 1

        for line in range(num):
            matrix.append([])
            for column in range(num):
                matrix[line].append(value)
                value *= 2
            value = matrix[line][1]

        space = len(str(matrix[num - 1][num - 1]))

        for line in range(num):
            for column in range(num):
                matrix[line][column] = str(matrix[line][column])
                
                while len(matrix[line][column]) < space:
                    matrix[line][column] = ' ' + matrix[line][column]
                
            result = ' '.join(matrix[line])
            print(result)

    print()
