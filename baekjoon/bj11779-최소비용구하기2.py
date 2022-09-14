import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start):
    hq = [(0, start)]
    visited[start] = 0
    while hq:
        cost, x = heappop(hq)
        if x == E:
            return
        if visited[x] < cost:
            continue
        for nc, nx in graph[x]:
            new_cost = cost + nc
            if visited[nx] > new_cost:
                visited[nx] = new_cost
                path[nx] = x # 이전 경로 저장
                heappush(hq, (new_cost, nx))

N, M = int(input()), int(input()) # 도시의 개수 N, 버스의 개수 M
graph = [[] for _ in range(N + 1)]
visited = [sys.maxsize] * (N + 1)

for _ in range(M):
    st, ed, co = map(int, input().split())
    graph[st].append((co, ed))

S, E = map(int, input().split())
path = [-1] * (N + 1)

dijkstra(S)

# 최단경로 역추적
result = [E]
prev = E
while path[prev] != -1:
    result.append(path[prev])
    prev = path[prev]

print(visited[E])
print(len(result))
print(*result[::-1])
