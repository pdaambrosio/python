[a, b, c] = map(int, input().split())


def winter_is_comming(day1, day2, day3):
    climate_tendencies1 = day2 - day1
    climate_tendencies2 = day3 - day2

    if climate_tendencies2 > climate_tendencies1:
        print(':)')
    elif climate_tendencies2 < climate_tendencies1:
        print(':(')
    else:
        if climate_tendencies1 <= 0:
            print(':(')
        else:
            print(':)')


winter_is_comming(a, b, c)
