while True:
    try:
        n = int(input())
        print('vai ter duas!' if n >= 1 else 'vai ter copa!')

    except EOFError:
        break
