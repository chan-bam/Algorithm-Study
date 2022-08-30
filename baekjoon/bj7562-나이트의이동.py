import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    Q = deque([(curR, curC)])
    while Q:
        r, c = Q.popleft()
        if r == tarR and c == tarC:
            return
        for dr, dc in [(2, 1), (2, -1), (-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))

T = int(input())

for _ in range(T):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    curR, curC = map(int, input().split())
    tarR, tarC = map(int, input().split())
    bfs()
    print(visited[tarR][tarC])
