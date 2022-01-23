def honey_reservoir(height, area):
    r_area = area / 2
    area = 3.14 * r_area * r_area
    height = height / (r_area * r_area * 3.14)
    
    return f'ALTURA = {height:.2f}\nAREA = {area:.2f}'


def main():
    while True:
        try:
            v = float(input())
            d = float(input())
            print(honey_reservoir(v, d))
        except EOFError:
            break


main()
