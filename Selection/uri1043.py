[a, b, c] = map(float, input().split())

if (a + b) > c and (a + c) > b and (b + c) > a:
    perimeter = a + b + c
    print('Perimetro = {:.1f}'.format(perimeter))
else:
    area = 0.5 * (a + b) * c
    print('Area = {:.1f}'.format(area))
