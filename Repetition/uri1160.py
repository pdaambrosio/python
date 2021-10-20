loop = int(input())

for i in range(loop):
    [pa, pb, g1, g2] = map(float, input().split())
    years = 0
    while pa <= pb:
        years += 1
        pa += int(pa * (g1 / 100))
        pb += int(pb * (g2 / 100))
        if years > 100:
            break
    print('Mais de 1 seculo.' if years > 100 else f'{years} anos.')
