import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    Q = deque([(0, 0)])
    while Q:
        node = Q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = node[0] + dx, node[1] + dy
            if 0 <= nx < N and 0 <= ny < M and MAZE[nx][ny] == 1:
                MAZE[nx][ny] = MAZE[node[0]][node[1]] + 1
                Q.append((nx, ny))
            if nx == N - 1 and ny == M - 1:
                return MAZE[nx][ny]

N, M = map(int, input().split())
MAZE = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())