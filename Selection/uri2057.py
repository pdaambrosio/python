def mobile_time_zone(departure, travel_time, time_zone):
    if departure == 0:
        departure = 24
    
    arrival_time = departure + travel_time + time_zone
    
    if arrival_time > 24:
        return arrival_time - 24
    elif arrival_time == 24:
        return 0
    return arrival_time


def main():
    [s, t, f] = map(int, input().split())
    print(mobile_time_zone(s, t, f))


main()
