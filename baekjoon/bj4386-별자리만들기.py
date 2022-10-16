import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]
link = [[] for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        # if i == j:
        #     continue
        (x1, y1), (x2, y2) = stars[i], stars[j]
        distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        link[i].append((distance, j))
        link[j].append((distance, i))

visited = [0] * n
hq = [(0, 0)]
cnt, result = n, 0
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
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())

stars = [tuple(map(float, input().split())) for _ in range(N)]
link = [[] for _ in range(N)]

# 거리(가중치, 비용)를 계산하여 인접리스트 생성 #i번째 별과 j번쨰 별의 거리
for i in range(N):
    x1, y1 = stars[i] # i번째 별
    for j in range(N):
        if i == j:
            continue
        x2, y2 = stars[j] # j번째 별
        link[i].append((((x1 - x2)**2 + (y1 - y2)**2)**0.5, j))

hq = [(0, 0)]
visited = [0] * N
cnt, result = 0, 0

# prim alogrithm
while hq:
    if cnt == N:
        break
    cost, node = heappop(hq)
    if visited[node]:
        continue
    visited[node] = 1
    cnt += 1
    result += cost
    for i in link[node]:
        if not visited[i[1]]:
            heappush(hq, i)

print(result)
'''