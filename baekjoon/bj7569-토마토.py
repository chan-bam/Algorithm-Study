import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while Q:
        z, x, y = Q.popleft()
        for dz, dx, dy in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and not tomatoes[nz][nx][ny]:
                Q.append((nz, nx, ny))
                tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1

M, N, H = map(int, input().split())
tomatoes = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
Q = deque([])
max_v = 1
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomatoes[k][i][j] == 1:
                Q.append((k, i, j))
bfs()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomatoes[k][i][j] == 0:
                print(-1)
                exit(0)
        max_v = max(max(tomatoes[k][i]), max_v)
print(max_v - 1)
