T = int(input())

for tc in range(1, T + 1):
    L, U, X = map(int, input().split())
    if X < L:
         res = L - X
    elif U < X:
        res = -1
    else:
        res = 0
    print('#{} {}'.format(tc, res))