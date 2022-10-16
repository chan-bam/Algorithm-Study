import sys
from heapq import heappush, heappop
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 입력
N, M = map(int, input().split()) # 세로 N 가로 M
world = [list(map(int, input().split())) for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 하 상 우 좌

# 섬에 번호 붙이기 # DFS
def dfs(x, y):
    global cnt
    visited[x][y] = 1
    world[x][y] = cnt
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and world[nx][ny] == 1:
            dfs(nx, ny)

# 한방향으로만 가는 다리를 만들고, 최소거리를 구함 # DFS
def dfs2(x, y, d, n, cost):
    if world[x][y] and world[x][y] != n: # 바다가 아니고, 다른 섬이면
        if cost != 1: # 길이가 1 이상이면
            link[world[x][y] - 1].add((cost, n - 1))
            # link[n - 1].add((cost, world[x][y] - 1))
        return
    dx, dy = dir[d]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < M and world[nx][ny] != n:
        dfs2(nx, ny, d, n, cost + 1)

visited = [[0] * M for _ in range(N)]
cnt = 2
for i in range(N):
    for j in range(M):
        if world[i][j] == 1:
            dfs(i, j)
            cnt += 1
cnt -= 2

link = [set() for _ in range(cnt + 1)] # 인접리스트
for i in range(N):
    for j in range(M):
        if world[i][j] != 0:
            for k in range(4):
                di, dj = dir[k]
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and not world[ni][nj]:
                    dfs2(ni, nj, k, world[i][j], 0)

# 최소 길이로 연결 # MST # Prim
visited = [0] * (cnt + 1)
hq = [(0, 1)]
result = 0
while hq:
    cost, node = heappop(hq)
    if visited[node]:
        continue
    visited[node] = 1
    cnt -= 1
    result += cost
    for i in link[node]:
        if not visited[i[1]]:
            heappush(hq, i)
if cnt:
    print(-1)
else:
    print(result)

'''
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 입력
N, M = map(int, input().split()) # 세로 N 가로 M
world = [list(map(int, input().split())) for _ in range(N)]

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 하 상 우 좌
# 섬에 번호 붙이기 # DFS
def dfs(x, y):
    global cnt
    visited[x][y] = 1
    world[x][y] = cnt
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and world[nx][ny] == 1:
            dfs(nx, ny)

# 한방향으로만 가는 다리를 만들고, 최소거리를 구함 # DFS
def dfs2(x, y, d, n, cost):
    if world[x][y] and world[x][y] != n: # 바다가 아니고, 다른 섬이면
        if cost != 1: # 길이가 1 이상이면
            link[world[x][y] - 1].add((cost, n - 1))
            link[n - 1].add((cost, world[x][y] - 1))
        return
    dx, dy = dir[d]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < M and world[nx][ny] != n: # !!!! world[nx][ny] != n <- 하지 않는 경우 같은 섬도 큐에 넣는 경우가 생김
        dfs2(nx, ny, d, n, cost + 1)

visited = [[0] * M for _ in range(N)]
cnt = 2
for i in range(N):
    for j in range(M):
        if world[i][j] == 1:
            dfs(i, j)
            cnt += 1
cnt -= 2

link = [set() for _ in range(cnt + 1)] # 인접리스트
for i in range(N):
    for j in range(M):
        if world[i][j] != 0:
            for k in range(4):
                di, dj = dir[k]
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and not world[ni][nj]:
                    dfs2(ni, nj, k, world[i][j], 0)

for i in range(1, cnt - 1):
    if not link[i]:
        print(-1)
        exit(0)

# 최소 길이로 연결 # MST # Prim
visited = [0] * (cnt + 1)
hq = [(0, 1)]
result = 0
while cnt:
    if not hq:
        print(-1)
        exit(0)
    cost, node = heappop(hq)
    if visited[node]:
        continue
    visited[node] = 1
    cnt -= 1
    result += cost
    for i in link[node]:
        if not visited[i[1]]:
            heappush(hq, i)
print(result)
'''

'''
# !!!
4 8
0 0 0 0 0 0 1 1
1 0 0 1 1 0 1 1
1 1 1 1 0 0 0 0 
1 1 0 0 0 1 1 0
answer: -1

8 8
1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1
1 0 0 1 1 0 0 1
1 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1
answer: 2

2 5
1 0 0 0 0
0 0 0 1 0
answer: -1

# !!!!
6 6
1 1 1 1 1 1
0 0 0 0 0 0
1 1 1 0 1 0
0 1 0 1 0 1
0 0 0 0 0 0
1 1 1 1 1 1
answer: -1

1 6
1 0 1 0 0 1
answer: -1
    
6 1
1
0
1
0
0
1
answer: -1
    
5 10
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
1 0 1 0 0 1 0 1 0 1
1 1 1 0 0 0 0 1 1 1
1 1 1 1 1 1 1 1 1 1 
answer: 2
    
5 5
1 0 1 0 1
0 1 1 0 0
0 0 1 1 0
0 0 0 1 1
0 0 0 0 1
answer: -1
    
10 10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
answer: 6
    
6 10
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 1 0 0 0
1 0 1 0 0 0 1 0 0 1
1 0 1 0 0 0 1 0 0 1
0 0 1 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
answer: 2
'''