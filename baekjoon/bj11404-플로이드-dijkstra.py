# dijkstra
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def dijkstra(start):
    distance = [100_000_000] * (N + 1)
    hq = [(0, start)]
    distance[start] = 0
    while hq:
        cost, x = heappop(hq)
        if distance[x] < cost:
            continue
        for nc, nx in graph[x]:
            new_cost = cost + nc
            if distance[nx] > new_cost:
                distance[nx] = new_cost
                heappush(hq, (new_cost, nx))
    return distance

N, M = int(input()), int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    st, ed, co = map(int, input().split())
    graph[st].append((co, ed))

for i in range(1, N + 1):
    result = dijkstra(i)
    for j in range(1, N + 1):
        if result[j] == 100_000_000:
            print(0, end=' ')
        else:
            print(result[j], end=' ')
    print()