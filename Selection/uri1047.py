[start_hour, start_minute, end_hour, end_minute] = map(int, input().split())

duration = ((end_hour * 60) + end_minute) - ((start_hour * 60) + start_minute)

if duration <= 0:
    duration += 24 * 60

hour = duration // 60
minute = duration % 60

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hour, minute))
