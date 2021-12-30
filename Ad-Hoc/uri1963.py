def the_motion_picture(a, b):
    return f'{(((b - a) / a) * 100):.2f}%'


def main():
    [old_price, new_price] = map(float, input().split())
    print(the_motion_picture(old_price, new_price))


main()
