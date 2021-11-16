while True:
    try:
        n = int(input())
        matrix = [[] for num in range(n)]

        for line in range(len(matrix)):
            for column in range(len(matrix)):
                matrix[column].append('3')
            
            count = n - 1

        for i in range(n):
            matrix[i][i] = '1'
            matrix[i][count] = '2'
            count -= 1

            format_print = ''.join(matrix[i])
            print(format_print)

    except EOFError:
        break
