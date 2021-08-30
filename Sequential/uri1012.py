import math

[a, b, c] = map(float, input().split())
pi = 3.14159

triangle_rectangle = (a * c) / 2
circle = pi * math.pow(c, 2)
trapeze = ((a + b) * c) / 2.0
square = b * b
rectangle = a * b

print('TRIANGULO: {:.3f}'.format(triangle_rectangle))
print('CIRCULO: {:.3f}'.format(circle))
print('TRAPEZIO: {:.3f}'.format(trapeze))
print('QUADRADO: {:.3f}'.format(square))
print('RETANGULO: {:.3f}'.format(rectangle))
