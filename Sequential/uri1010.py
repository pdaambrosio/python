cod1, num1, value1 = input().split()
cod2, num2, value2 = input().split()

parts1_value = int(num1) * float(value1)
parts2_value = int(num2) * float(value2)

total_value = parts1_value + parts2_value

print('VALOR A PAGAR: R$ {:.2f}'.format(total_value))
