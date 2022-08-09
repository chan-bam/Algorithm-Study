import sys
sys.stdin = open("1258in.txt")

def clear(r1, r2, c1, c2):
    for i in range(r1, r2):
        for j in range(c1, c2):
            ARR[i][j] = 0
    return

def matrix(r, c):
    x = r
    y = c
    while 0 <= x < N and ARR[x][y] != 0:
        x += 1
    h = x - r
    x -= 1
    while 0 <= y < N and ARR[x][y] != 0:
        y += 1
    w = y - c
    result.append([h * w, h, w])
    clear(r, r + h, c, c + w)
    return


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if ARR[i][j] != 0:
                matrix(i, j)
    result.sort()
    print(f'#{tc} {len(result)}', end = ' ')
    for res in result:
        print(res[1], res[2], end=' ')
    print()