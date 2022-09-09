import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    Q = deque([(0, 0, 0, 1)])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]    # visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    visited[0][0][0] = 1
    while Q:
        x, y, crash, cnt = Q.popleft()
        if x == N - 1 and y == M - 1:
            return cnt
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if ARR[nx][ny] and not crash: # 벽이고 안부서졌다면
                    Q.append((nx, ny, 1, cnt + 1))
                    visited[nx][ny][1] = 1
                elif not ARR[nx][ny] and not visited[nx][ny][crash]: # 통로고 방문한적이 없다면
                    Q.append((nx, ny, crash, cnt + 1))
                    visited[nx][ny][crash] = 1
    return -1

N, M = map(int, input().split())
ARR = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())
'''
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    Q = deque([(0, 0, 0)])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while Q:
        x, y, crash = Q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][crash]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if ARR[nx][ny] and not crash: # 벽이고 안부서졌다면
                    Q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][crash] + 1
                elif not ARR[nx][ny] and not visited[nx][ny][crash]: # 통로고 방문한적이 없다면
                    Q.append((nx, ny, crash))
                    visited[nx][ny][crash] = visited[x][y][crash] + 1
    return -1

N, M = map(int, input().split())
ARR = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())
'''