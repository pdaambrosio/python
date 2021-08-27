# -*- coding: utf-8 -*-

pi = 3.14159
a = float(input())
area = pi * (a**2) # or area = pi * (a*a)

# print(f'A={area:.4f}') Not accepted by URI

print('A={:.4f}'.format(area))