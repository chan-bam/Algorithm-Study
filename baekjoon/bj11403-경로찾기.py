import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
visited_i = [[0] * N for _ in range(N)]
visited_b = [0] * N
visited_bi = [[0] * N for _ in range(N)]

def dfs_i(x, idx):
    for n in range(N):
        if arr[x][n] and not visited_i[idx][n]:
            visited_i[idx][n] = 1
            dfs_i(n, idx)

def dfs(x):
    for n in range(N):
        if arr[x][n] and not visited[n]:
            visited[n] = 1
            dfs(n)

def bfs(x):
    Q = deque([x])
    while Q:
        nx = Q.popleft()
        for n in range(N):
            if arr[nx][n] and not visited_b[n]:
                visited_b[n] = 1
                Q.append(n)

def bfs_i(x, idx):
    Q = deque([x])
    while Q:
        nx = Q.popleft()
        for n in range(N):
            if arr[nx][n] and not visited_bi[idx][n]:
                visited_bi[idx][n] = 1
                Q.append(n)

for i in range(N):
    # dfs(i)
    # print(*visited)
    # visited = [0] * N # 초기화
    # dfs_i(i, i)
    # bfs(i)
    # print(*visited_b)
    # visited_b = [0] * N # 초기화
    bfs_i(i, i)

# for v in visited_i:
#     print(*v)
for v in visited_bi:
    print(*v)
