import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start):
    hq = [(0, start)]
    dist[start] = 0
    while hq:
        cost, x = heappop(hq)
        if x == E:
            return
        if dist[x] < cost:
            continue
        for nc, nx in graph[x]:
            new_cost = cost + nc
            if dist[nx] > new_cost:
                dist[nx] = new_cost
                path[nx] = x
                heappush(hq, (new_cost, nx))

N, M = int(input()), int(input()) # 도시의 개수 N , 버스의 개수 M
graph = [[] for _ in range(N + 1)]
dist = [sys.maxsize] * (N + 1)
path = [-1] * (N + 1)

for _ in range(M): # 버스 노선
    st, ed, co = map(int, input().split())
    graph[st].append((co, ed))

S, E = map(int, input().split())

dijkstra(S)

# 경로 추적
result = [E]
prev = E
while path[prev] != -1:
    prev = path[prev]
    result.append(prev)

print(dist[E])
print(len(result))
print(*result[::-1])

