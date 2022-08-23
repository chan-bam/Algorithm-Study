import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    field[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr <= R and 0 <= nc <= C and field[nr][nc]:
            dfs(nr, nc)
    return

T = int(input().rstrip())

for _ in range(T):
    cnt = 0
    C, R, N = map(int, input().split())
    field = [[0] * (C + 1) for _ in range(R + 1)]
    for _ in range(N):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    for i in range(R):
        for j in range(C):
            if field[i][j]:
                cnt += 1
                dfs(i, j)
    print(cnt)