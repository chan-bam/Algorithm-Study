import sys
input = sys.stdin.readline
from collections import deque

def bfs(r, c): # 상어 거리 재기
    global size
    sea[r][c] = 0 # ^^^^^^^^^^^
    visited = [[0] * N for _ in range(N)]
    able = []
    Q = deque([(r, c)])
    while Q:
        x, y = Q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and sea[nx][ny] <= size:
                if sea[nx][ny] == size or sea[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx, ny))
                    able.append((visited[nx][ny], nx, ny))
    return able

def eat(able):
    global size, time, cnt
    if not len(able):
        print(time)
        exit(0)
    else:
        able.sort(key=lambda x:(x[0], x[1], x[2]))
        a, b = able[0][1], able[0][2]
        time += able[0][0]
        cnt += 1
        if cnt % size == 0: # !!!
            size += 1
            cnt = 0
        sea[a][b] = 9
        return a, b


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
size = 2
time = 0
cnt = 0

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            able = bfs(i, j)

while True:
    x, y = eat(able)
    able = bfs(x, y)