age_days = int(input())

years = int(age_days / 365)
age_days = age_days % 365
months = int(age_days / 30)
age_days = age_days % 30
days = age_days

print('{} ano(s)'.format(years))
print('{} mes(es)'.format(months))
print('{} dia(s)'.format(days))
