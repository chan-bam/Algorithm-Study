import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start, end):
    visited = [sys.maxsize] * (N + 1)
    hq = [(0, start)]
    visited[start] = 0
    while hq:
        cost, x = heappop(hq)
        if x == end:
            return cost
        if visited[x] >= cost:
            visited[x] = cost
            for nc, nx in graph[x]:
                new_cost = nc + cost
                if visited[nx] > new_cost:
                    visited[nx] = new_cost
                    heappush(hq, (new_cost, nx))

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))
    graph[e].append((c, s))

U, V = map(int, input().split())

try:
    res1 = dijkstra(1, U) + dijkstra(V, N)
except:
    res1 = 0

try:
    res2 = dijkstra(1, V) + dijkstra(U, N)
except:
    res2 = 0

if res1 or res2:
    print(min(res1, res2) + dijkstra(U, V))
else:
    print(-1)