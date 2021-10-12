import sys
sys.stdin = open("11671in.txt")

def cover(x, y, coverRange):
    for a in range(1, coverRange):
        if 0 <= x-a and region[x-a][y] == 'H':
            region[x-a][y] = 'X'
        if 0 <= y-a and region[x][y-a] == 'H':
            region[x][y-a] = 'X'
        if x+a < N and region[x+a][y] == 'H':
            region[x+a][y] = 'X'
        if y+a < N and region[x][y+a] == 'H':
            region[x][y+a] = 'X'
# delta는 반복문으로 이 과정 줄이는 것

def coverD(r, c, coverR):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for s in range(1, coverR):
        for d in range(4):
            nr = r + dr[d]*s # 커버 범위까지 반복
            nc = c + dc[d]*s # 커버 범위까지 반복
            if 0 <= nr < N and 0 <= nc < N:
                if region[nr][nc] == 'H':
                    region[nr][nc] = 'X'

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    region = [list(input()) for _ in range(N)]
    # H : 집
    # X : 아무 것도 없다!
    # A : 동서남북으로 1개 커버하는 기지국
    # B : 동서남북으로 2개 커버하는 기지국
    # C : 동서남북으로 3개 커버하는 기지국


    # for i in range(N):
    #     for j in range(N):
    #         if region[i][j] in ('A', 'B', 'C'):
    #             cover(i, j, ord(region[i][j])-63)

    for i in range(N):
        for j in range(N):
            if region[i][j] in ('A', 'B', 'C'):
                coverD(i, j, ord(region[i][j])-63)

    home = 0
    for k in range(len(region)):
        home += region[k].count('H')

    print(f'#{tc} {home}')