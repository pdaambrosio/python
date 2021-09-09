[start_time, end_time] = map(int, input().split())

duration = end_time - start_time

if duration <= 0:
    duration += 24

print('O JOGO DUROU {} HORA(S)'.format(duration))
