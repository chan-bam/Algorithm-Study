import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start):
    hq = [(0, start)]
    visited[start] = 0
    while hq:
        weight, x = heappop(hq)
        if visited[x] < weight:
            continue
        for nw, nx in graph[x]:
            nd = weight + nw
            if visited[nx] > nd:
                visited[nx] = nd
                heappush(hq, (nd, nx))

V, E = map(int, input().split()) # 정점의 개수 V # 간선의 개수 E
S = int(input()) # 시작 정점

graph = [[] for _ in range(V + 1)]
visited = [10_000_000] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v)) # 방향그래프

dijkstra(S)
for i in range(1, V + 1):
    if i == S:
        print(0)
    elif visited[i] == 10_000_000:
        print("INF")
    else:
        print(visited[i])