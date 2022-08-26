import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while Q:
        x, y = Q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and not tomato[nx][ny]:
                tomato[nx][ny] = tomato[x][y] + 1
                Q.append((nx, ny))

def check():
    max_v = 1
    for i in range(N):
        for j in range(M):
            if not tomato[i][j]: # 0
                return -1
            elif tomato[i][j] > max_v:
                max_v = tomato[i][j]
    return max_v - 1


M, N = map(int, input().split())
tomato = [list(map(int, input().rstrip().split())) for _ in range(N)]
Q = deque([])

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            Q.append((i, j))

bfs()
print(check())