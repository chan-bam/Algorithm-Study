import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input()) # 행성의 개수 N개
planet = [list(map(int, input().split())) + [i] for i in range(N)] # 행성의 x, y, z 좌표 + 입력된 순서
link = [[] for _ in range(N)]

# x => y => z 기준으로 "정렬"하여 계산
# N**2 => (N-1)*3
for i in range(3):
    planet.sort(key=lambda x: x[i]) # 0 => 1 => 2번째 요소를 기준으로 정렬
    for j in range(N - 1):
        link[planet[j][3]].append((abs(planet[j + 1][i] - planet[j][i]), planet[j + 1][3]))
        link[planet[j + 1][3]].append((abs(planet[j + 1][i] - planet[j][i]), planet[j][3]))

# prim
visited = [0] * N
hq = [(0, 0)]
cnt, result = N, 0
while cnt:
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
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input()) # 행성의 개수 N개
planet = [list(map(int, input().split())) + [i] for i in range(N)] # 행성의 x, y, z 좌표 + 입력된 순서
link = [[] for _ in range(N)]

# x, y, z 기준으로 "정렬"하여 계산
# N**2 => (N-1)*3
planet_x = sorted(planet, key=lambda x: x[0])
planet_y = sorted(planet, key=lambda x: x[1])
planet_z = sorted(planet, key=lambda x: x[2])

for j in range(N - 1):
    link[planet_x[j][3]].append((abs(planet_x[j + 1][0] - planet_x[j][0]), planet_x[j + 1][3]))
    link[planet_x[j + 1][3]].append((abs(planet_x[j + 1][0] - planet_x[j][0]), planet_x[j][3]))
    link[planet_y[j][3]].append((abs(planet_y[j + 1][1] - planet_y[j][1]), planet_y[j + 1][3]))
    link[planet_y[j + 1][3]].append((abs(planet_y[j + 1][1] - planet_y[j][1]), planet_y[j][3]))
    link[planet_z[j][3]].append((abs(planet_z[j + 1][2] - planet_z[j][2]), planet_z[j + 1][3]))
    link[planet_z[j + 1][3]].append((abs(planet_z[j + 1][2] - planet_z[j][2]), planet_z[j][3]))

visited = [0] * N
hq = [(0, 0)]
cnt, result = N, 0
while cnt:
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
# 메모리초과(7%)
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input()) # 행성의 개수 N개
planet = [list(map(int, input().split())) for _ in range(N)] # 행성의 x, y, z 좌표
link = [set() for _ in range(N)]

for i in range(N - 1):
    for j in range(i + 1, N):
        (x1, y1, z1), (x2, y2, z2) = planet[i], planet[j]
        w = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
        link[i].add((w, j))
        link[j].add((w, i))

visited = [0] * N
hq = [(0, 0)]
cnt, result = N, 0
while cnt:
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
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
'''