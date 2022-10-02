import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

if house[-1][-1]:
    print(0)
    exit(0)

def dfs(x, y, d): # d : 가로 1 세로 2 대각선 0
    global cnt
    if x == N - 1 and y == N - 1:
        cnt += 1
        return
    # 대각선방향 : 3방향 모두 가능
    if x + 1 < N and y + 1 < N and not house[x + 1][y + 1] and not house[x + 1][y] and not house[x][y + 1]:
        dfs(x + 1, y + 1, 0)
    # 가로방향 : 대각선, 가로방향에서 가능
    if (not d or d == 1) and x < N and y + 1 < N and not house[x][y + 1]:
        dfs(x, y + 1, 1)
    # 세로방향: 대각선, 세로방향에서 가능
    if (not d or d == 2) and x + 1 < N and y < N and not house[x + 1][y]:
        dfs(x + 1, y, 2)

cnt = 0
dfs(0, 1, 1)
print(cnt)

'''
# bfs 시간초과2
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

if house[-1][-1]:
    print(0)
    exit(0)

def bfs():
    Q = deque([(0, 1, 1)])
    global cnt
    while Q:
        x, y, d = Q.popleft() # d : 가로 1 세로 2 대각선 0
        if x == N - 1 and y == N - 1:
            cnt += 1
        # 대각선방향 : 3방향 모두 가능
        if x + 1 < N and y + 1 < N and not house[x + 1][y + 1] and not house[x + 1][y] and not house[x][y + 1]:
            Q.append((x + 1, y + 1, 0))
        # 가로방향 : 대각선, 가로방향에서 가능
        if (not d or d == 1) and x < N and y + 1 < N and not house[x][y + 1]:
            Q.append((x, y + 1, 1))
        # 세로방향: 대각선, 세로방향에서 가능
        if (not d or d == 2) and x + 1 < N and y < N and not house[x + 1][y]:
            Q.append((x + 1, y, 2))

cnt = 0
bfs()
print(cnt)
'''
'''
# dfs 시간초과
import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

if house[-1][-1]:
    print(0)
    exit(0)

def dfs(x, y, d):
    global cnt
    if x == N - 1 and y == N - 1:
        cnt += 1
    for dx, dy, nd in (0, 1, 1), (1, 0, 2), (1, 1, 3):
        if (d == 1 and nd == 2) or (d == 2 and nd == 1):
            continue
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and nd == 3 and not house[nx][ny]:
            if nd == 1 or nd == 2 or (nd == 3 and not house[nx - 1][ny] and not house[nx][ny - 1]):
                dfs(nx, ny, nd)
cnt = 0
dfs(0, 1, 1)
print(cnt)

'''
'''
# bfs 시간초과
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
# 빈칸은 0 / 벽은 1

# (0,1) 에서 한쪽 끝을 (N,N)로 보내는 방법의 수

# 이동시킬 수 없는 경우 0
# 방법의 수는 항상 1,000,000보다 작거나 같다

# 파이프를 밀 수 있는 방향 : →, ↘, ↓ (오른쪽, 오른쪽 아래 대각선, 아래)
# 가로로 놓여진 경우 이동 방법 2 (오른쪽(0, 1), 오른쪽 아래로 밀기(1, 1)) # 1
# 세로로 놓여진 경우 이동 방법 2 (아래(1, 0), 오른쪽 아래로 밀기(1, 1)) # 2
# 대각선으로 놓여진 경우(오른쪽(0, 1), 아래(1, 0), 오른쪽 아래 대각선(1, 1)) # 3

if house[-1][-1]:
    print(0)
    exit(0)

cnt = 0
Q = deque([(0, 1, 1)])
while Q:
    x, y, d = Q.popleft()
    if x == N - 1 and y == N - 1:
        cnt += 1
    for dx, dy, nd in (0, 1, 1), (1, 0, 2), (1, 1, 3): # d: 1-가로 2-세로 3-대각선
        if d == 1 and nd == 2:
            continue
        if d == 2 and nd == 1:
            continue
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not house[nx][ny]:
            if nd == 1 or nd == 2 or nd == 3 and not house[nx - 1][ny] and not house[nx][ny - 1]:
                Q.append((nx, ny, nd))
print(cnt)
'''
'''
6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
correct: 1

6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
correct: 5

6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 1 0 0
correct: 3

7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 1 0 0 0 1 0
0 0 0 0 0 0 0
1 0 0 0 1 1 0
0 0 0 0 0 0 0
0 1 0 0 0 0 0
correct: 9

7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
correct: 53

16
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 0
0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 1 0 0 0 1 0 1 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
correct: 109

16
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1
0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 1 1 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
correct: 664
'''