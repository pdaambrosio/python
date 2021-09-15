start_day = int(input().split()[1])
[start_hour, start_minute, start_second] = map(int, input().split(':'))
end_day = int(input().split()[1])
[end_hour, end_minute, end_second] = map(int, input().split(':'))

duration_hours = ((end_hour * 60) + end_minute) - ((start_hour * 60) + start_minute)
days = end_day - start_day

if duration_hours < 0:
    duration_hours += 24 * 60
    days -= 1

if days < 0:
    days = 0

hours = duration_hours // 60
minutes = duration_hours % 60
seconds = end_second - start_second

if seconds < 0:
    seconds += 60
    minutes -= 1

print('{} dia(s)'.format(days))
print('{} hora(s)'.format(hours))
print('{} minuto(s)'.format(minutes))
print('{} segundo(s)'.format(seconds))
