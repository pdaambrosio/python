while True:
    try:
        number_slugs = int(input())
        slug_group = map(int, input().split())
        fast_slug = 0
        for slug in slug_group:
            if slug > fast_slug:
                fast_slug = slug
        if fast_slug < 10:
            print(1)
        elif fast_slug >= 10 and fast_slug < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break
