import sys
input = sys.stdin.readline
from heapq import heappush, heappop

# 지역의 개수 N # 수색 범위 M # 길의 개수 R
N, M, R = map(int, input().split())
items = [0] + list(map(int, input().split())) # 구역에 있는 아이템 수
graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(R):
    s, e, c = map(int, input().split())
    # 양방향
    graph[s].append((c, e))
    graph[e].append((c, s))

def dijkstra(x):
    distance = [sys.maxsize] * (N + 1)
    distance[x] = 0
    hq = [(0, x)]
    while hq:
        cost, x = heappop(hq)
        if distance[x] < cost:
            continue
        for nc, nx in graph[x]:
            new_cost = cost + nc
            if distance[nx] > new_cost:
                distance[nx] = new_cost
                heappush(hq, (new_cost, nx))
    res = 0
    for i in range(1, N + 1):
        if distance[i] <= M:
            res += items[i]
    return res

result = 0
for i in range(N):
    result = max(result, dijkstra(i))

print(result)