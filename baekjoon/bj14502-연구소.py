import copy, sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 지도의 세로크기 N, 가로크기 M
ARR_0 = [list(map(int, input().split())) for _ in range(N)] # 0은 빈칸, 1은 벽, 2는 바이러스가 있는 곳

vacant, virus = [], []
for i in range(N):
    for j in range(M):
        if not ARR_0[i][j]:   # 빈칸의 좌표
            vacant.append([i, j])
        elif ARR_0[i][j] == 2:    # 바이러스의 좌표
            virus.append([i, j])

def bfs():
    Q = deque(virus)
    while Q:
        x, y = Q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # 인접한 상하좌우
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not ARR[nx][ny]: # 0이면
                Q.append([nx, ny])
                ARR[nx][ny] = 2

result = 0
for wall in combinations(vacant, 3): # 벽을 세울 수 있는 좌표의 조합 # 재귀(dfs, backtracking)로 구할 수도 있음
    ARR = copy.deepcopy(ARR_0)
    for i, j in wall:
        ARR[i][j] = 1   # 벽 세우기
    bfs()
    total = 0
    for a in ARR:
        total += a.count(0) # 안전 영역의 크기 세기
    result = max(result, total)
print(result)

# bfs => dfs로도 가능