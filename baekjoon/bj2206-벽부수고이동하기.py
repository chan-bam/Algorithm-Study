import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    Q = deque([(0, 0, 1)])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1
                 # 벽이 안 뚫린 상태가 1 뚫린 상태가 0

    while Q:
        x, y, wall = Q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][wall]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if ARR[nx][ny] and wall: # arr값이 1(벽)이고, 벽이 안 뚫린 경우
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    Q.append((nx, ny, 0))
                elif not ARR[nx][ny] and not visited[nx][ny][wall]: # 0이고 방문하지 않은 경우
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    Q.append((nx, ny, wall))
    return -1



N, M = map(int, input().split()) # 행, 렬
ARR = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())

'''
# 시간초과
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global result
    flag = 0
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    visited_1 = [[0] * M for _ in range(N)]
    Q = deque([(0, 0)])
    while Q:
        x, y = Q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if not ARR[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx, ny))
                elif not flag and not visited_1[nx][ny]:
                    flag = 1
                    tx, ty = nx, ny
                    visited[tx][ty] = visited[x][y] + 1
                    ARR[tx][ty] = 0
                    Q.append((tx, ty))
                    visited_1[tx][ty] = 1
        if not Q and flag == 1:
            if visited[N - 1][M - 1]:
                result = min(result, visited[N - 1][M - 1])
            flag = 0
            ARR[tx][ty] = 1
            visited = [[0] * M for _ in range(N)]
            Q.append((0, 0))
            visited[0][0] = 1
        elif not Q and flag == 0:
            if visited[N - 1][M - 1]:
                result = min(result, visited[N - 1][M - 1])
            break

N, M = map(int, input().split()) # 행, 렬
ARR = [list(map(int, input().rstrip())) for _ in range(N)]
result = 1_000_000

bfs()

if result:
    print(result)
else:
    print(-1)
    
'''



'''
6 4
0000
1110
1000
0000
0111
0010
    
정답: 9 
    
2 6
010001
000110
 
정답: 9

'''