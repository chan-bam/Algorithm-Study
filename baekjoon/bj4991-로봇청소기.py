import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations

def bfs(x, y):
    Q = deque([(x, y)])
    distance = [[-1] * w for _ in range(h)]
    distance[x][y] = 0
    while Q:
        cur_x, cur_y = Q.popleft()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = cur_x + dx, cur_y + dy
            if 0 <= nx < h and 0 <= ny < w and distance[nx][ny] == -1 and room[nx][ny] != 'x':
                Q.append((nx, ny))
                distance[nx][ny] = distance[cur_x][cur_y] + 1
    return distance

while True:
    # 가로, 세로 크기
    w, h = map(int, input().split())
    if w + h == 0:
        break
    room = [list(input()) for _ in range(h)]
    targets = []
    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o':
                start_x, start_y = i, j
            elif room[i][j] == '*':
                targets.append((i, j))
    dist = bfs(start_x, start_y)
    impossible = False

    # 시작지부터 target간의 거리 구하기
    start_to_target = []
    for i, j in targets:
        if dist[i][j] == -1: # 청소할 수 없는 target
            print(-1)
            impossible = True
            break # 종료
        else:
            start_to_target.append(dist[i][j])

    # 갈수 없는 타겟이 있다면
    if impossible:
        continue

    # target과 target 간의 거리 구하기
    target_to_target = [[0] * len(targets) for _ in range(len(targets))]
    # for i in range(len(targets)):
    #     j, k = targets[i]
    #     dist = bfs(j, k)
    #     for l in range(len(targets)):
    #         n, m = targets[l]
    #         target_to_target[i][l] = dist[n][m]
    for i in range(len(targets) - 1):
        j, k = targets[i]
        dist = bfs(j, k)
        for l in range(i + 1, len(targets)):
            n, m = targets[l]
            target_to_target[i][l] = dist[n][m] # i에서 l로 가는 거리
            target_to_target[l][i] = dist[n][m]

    min_value = sys.maxsize
    for p in permutations(range(len(targets))): # 경로별(순열) 최소값 구하기
        start = p[0]
        total = start_to_target[start]
        for i in range(1, len(targets)):
            end = p[i]
            total += target_to_target[start][end]
            start = end
        min_value = min(min_value, total)

    print(min_value)




'''
import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations

def bfs(x, y):
    distance = [[-1] * w for _ in range(h)]
    Q = deque([(x, y)])
    distance[x][y] = 0
    while Q:
        x, y = Q.popleft()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and room[nx][ny] != 'x' and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                Q.append((nx, ny))
    return distance # 갈 수 있는 경로 없는 것

while True:
    w, h = map(int, input().split()) # 가로크기 w 세로크기 h
    if w + h == 0:
        break
    room = [list(input().rstrip()) for _ in range(h)]
    sx, sy = 0, 0
    dust = []
    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o':
                sx, sy = i, j
            elif room[i][j] == '*':
                Q = dust.append((i, j))
    # 시작지점에서 더러운 칸까지의 거리 구하기
    dist = bfs(sx, sy)
    start_to_dust = []  # 시작지점에서 먼지까지의 거리 저장
    is_possible = True
    for i, j in dust:
        temp = dist[i][j]
        if temp == -1: # 방문할 수 없는 수 없는 칸이 존재
            print(-1)
            is_possible = False
            break
        else:
            start_to_dust.append(temp)
    # print(start_to_dust)

    if not is_possible:
        continue
    # 더러운 칸들 간의 거리 구하기
    dust_to_dust = [[0] * len(dust) for _ in range(len(dust))]
    for i in range(len(dust)):
        j, k = dust[i]
        dist = bfs(j, k)
        for l in range(len(dust)):
            if l != i:
                m, n = dust[l]
                dust_to_dust[i][l] = dist[m][n]
    # print(dust_to_dust)
    result = sys.maxsize # 거리의 최소값 저장
    # 이동하는 경우의 수
    for p in permutations(range(len(dust))): # !!! range => iterable
        start = p[0]
        total = start_to_dust[start] # 누적값 초기화
        for idx in range(1, len(dust)):
            end = p[idx]
            total += dust_to_dust[start][end] # 시작위치 => 목표위치간의 거리를 누적
            start = end # 시작점 갱신
        result = min(result, total)
    print(result)
'''



# 로봇 청소기가 처음 청소할 칸을 정하게 되면 남은 모든 더러운 칸들을 청소하는데 소요되는 거리는 각 칸의 거리의 총합이다.
# 따라서, 모든 더러운 칸 사이의 거리를 구한다.

'''
# 시간초과
import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations

def bfs(start_x, start_y, target_x, target_y):
    distance = [[-1] * w for _ in range(h)]
    Q = deque([(start_x, start_y)])
    distance[start_x][start_y] = 0
    while Q:
        x, y = Q.popleft()
        if x == target_x and y == target_y:
            return distance[x][y]
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and room[nx][ny] != 'x' and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                Q.append((nx, ny))
    return False # 갈 수 있는 경로 없는 것

while True:
    w, h = map(int, input().split()) # 가로크기 w 세로크기 h
    if w + h == 0:
        break
    room = [list(input().rstrip()) for _ in range(h)]
    sx, sy = 0, 0
    dust = []
    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o':
                sx, sy = i, j
            elif room[i][j] == '*':
                Q = dust.append((i, j))
    result = sys.maxsize
    for per in permutations(dust, len(dust)):
        si, sj = sx, sy
        dist = 0
        for i, j in per:
            temp = bfs(si, sj, i, j)
            if temp:
                dist += temp
                si, sj = i, j
            else:
                break
        else:
            result = min(result, dist)
    if result != sys.maxsize:
        print(result)
    else:
        print(-1)
'''
'''
3 3
***
xox
*..
0 0
answer : 8
'''