import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while Q:
        x, y = Q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not tomato[nx][ny]:
                tomato[nx][ny] = tomato[x][y] + 1
                Q.append((nx, ny))

M, N = map(int, input().split())
tomato = [list(map(int, input().rstrip().split())) for _ in range(N)]
Q = deque([])

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1: # 1일때만 # -1, 0은 X
            Q.append((i, j))

bfs()
max_v = 0

for tom in tomato:
    for t in tom:
        if not t:
            print(-1)
            exit(0)
    max_v = max(max_v, max(tom))

print(max_v - 1)