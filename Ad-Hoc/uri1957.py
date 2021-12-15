def convert_hex(num):
    num = hex(num)
    return num[2:]


def main():
    value = int(input())
    result = convert_hex(value)
    return result.upper()


print(main())
