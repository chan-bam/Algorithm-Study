import copy
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs_3(x, y, color):
    picture[x][y] = 0
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and picture[nx][ny] == color:
            dfs_3(nx, ny, color)

def dfs_2(x, y, color):
    picture_2[x][y] = 0
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and color == 'B' and picture_2[nx][ny] == color:
            dfs_2(nx, ny, color)
        elif 0 <= nx < N and 0 <= ny < N and color != 'B' and picture_2[nx][ny] and picture_2[nx][ny] != 'B':
            dfs_2(nx, ny, color)

N = int(input()) # N * N
picture = [list(input().rstrip()) for _ in range(N)]
picture_2 = copy.deepcopy(picture)
cnt_3, cnt_2 = 0, 0

for i in range(N):
    for j in range(N):
        if picture[i][j]:
            cnt_3 += 1
            dfs_3(i, j, picture[i][j])
        if picture_2[i][j]:
            cnt_2 += 1
            dfs_2(i, j, picture_2[i][j])
print(cnt_3, cnt_2)