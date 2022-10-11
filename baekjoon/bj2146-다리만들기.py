import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

N = int(input())
ARR = [list(map(int, input().split())) for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, n):
    ARR[x][y] = n
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and ARR[nx][ny] == 1:
            dfs(nx, ny, n)

def bfs(x, y, n):
    Q = deque([(x, y)])
    distance = [[-1] * N for _ in range(N)]
    distance[x][y] = 0
    while Q:
        x, y = Q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                # 바다이고 방문한 적이 없다면
                if not ARR[nx][ny] and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    Q.append((nx, ny))
                # 다른 섬에 도착한 경우 # 최단거리
                elif ARR[nx][ny] and ARR[nx][ny] != n:
                    return distance[x][y]

# 섬을 다른 숫자로 구분
label = 2
for i in range(N):
    for j in range(N):
        if ARR[i][j] == 1:
            dfs(i, j, label)
            label += 1

answer = sys.maxsize

for i in range(N):
    for j in range(N):
        if ARR[i][j] != 0:
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and ARR[ni][nj] == 0:
                    result = bfs(i, j, ARR[i][j])
                    if result == 1:
                        print(1)
                        exit(0)
                    else:
                        answer = min(result, answer)
print(answer)

'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

N = int(input())
ARR = [list(map(int, input().split())) for _ in range(N)]

def dfs(x, y, n):
    ARR[x][y] = n
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and ARR[nx][ny] == 1:
            dfs(nx, ny, n)

def bfs(n):
    Q = deque()
    distance = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if ARR[i][j] == n:
                Q.append((i, j))
                distance[i][j] = 0
    while Q:
        x, y = Q.popleft()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                # 바다이고 방문한 적이 없다면
                if not ARR[nx][ny] and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    Q.append((nx, ny))
                # 다른 섬에 도착한 경우 # 최단거리
                elif ARR[nx][ny] and ARR[nx][ny] != n:
                    return distance[x][y]

# 섬을 다른 숫자로 구분
label = 2
for i in range(N):
    for j in range(N):
        if ARR[i][j] == 1:
            dfs(i, j, label)
            label += 1

result = sys.maxsize
for i in range(2, label):
    result = min(bfs(i), result)  # 최단거리 중 최솟값 찾기

print(result)
'''