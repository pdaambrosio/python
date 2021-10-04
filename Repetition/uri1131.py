answer_loop = 0
count_departure = 0
count_draws = 0
victories_inter = 0
victories_gremio = 0

while answer_loop != 2:
    [inter_goals, gremio_goals] = map(int, input().split())
    count_departure += 1
    if inter_goals > gremio_goals:
        victories_inter += 1
    elif gremio_goals > inter_goals:
        victories_gremio += 1
    else:
        count_draws += 1

    print('Novo grenal (1-sim 2-nao)')
    answer_loop = int(input())

print(f'{count_departure} grenais')
print(f'Inter:{victories_inter}')
print(f'Gremio:{victories_gremio}')
print(f'Empates:{count_draws}')

if victories_inter > victories_gremio:
    print('Inter venceu mais')
elif victories_gremio > victories_inter:
    print('Gremio venceu mais')
