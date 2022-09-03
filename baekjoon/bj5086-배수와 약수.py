while True:
    x, y = map(int, input().split())
    if not x and not y:
        exit(0)
    elif x > y and x % y == 0:
        print('multiple')
    elif x < y and y % x == 0:
        print('factor')
    else:
        print('neither')