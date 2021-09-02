duration = int(input())

hours = int(duration / 3600)
minutes = int((duration % 3600) / 60)
seconds = int(duration % 60)

print('{}:{}:{}'.format(hours, minutes, seconds))
