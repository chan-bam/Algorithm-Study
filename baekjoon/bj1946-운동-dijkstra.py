# dictionary
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

inf = sys.maxsize
V, E = map(int, input().split())
graph = [{} for _ in range(V)]  # V개의 마을

def dijkstra(start):
    distance = [inf] * V
    hq = []
    for next, dist in graph[start].items():
        distance[next] = dist
        heappush(hq, (dist, next))
    while hq:
        cost, x = heappop(hq)
        if x == start:
            return distance[x]
        if distance[x] < cost:
            continue
        for nx, nc in graph[x].items():
            new_cost = cost + nc
            if distance[nx] > new_cost:
                distance[nx] = new_cost
                heappush(hq, (new_cost, nx))
    return inf

# (a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.
for _ in range(E):
    a, b, c = map(int, input().split())
    # a -> b 임에 주의
    graph[a - 1][b - 1] = c

result = inf
for i in range(V):
    result = min(dijkstra(i), result)
if result == inf:
    print(-1)
else:
    print(result)

'''
# list
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

inf = sys.maxsize
V, E = map(int, input().split())
graph = [[] for _ in range(V)] # V개의 마을

def dijkstra(start):
    distance = [inf] * V
    hq = []
    for next, dist in graph[start]: # !!!!
        distance[next] = dist
        heappush(hq, (dist, next))
    while hq:
        cost, x = heappop(hq)
        if x == start: # !!
            return distance[x]
        if distance[x] < cost:
            continue
        for nx, nc in graph[x]:
            new_cost = cost + nc
            if distance[nx] > new_cost:
                distance[nx] = new_cost
                heappush(hq, (new_cost, nx))
    return inf

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))

result = inf
for i in range(V):
    result = min(dijkstra(i), result)
if result == inf:
    print(-1)
else:
    print(result)

'''

'''
# 시간초과
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

inf = sys.maxsize
V, E = map(int, input().split())
graph = [[] for _ in range(V)] # V개의 마을

def dijkstra(start):
    distance = [inf] * V
    hq = [(0, start)]
    while hq:
        cost, x = heappop(hq)
        if distance[x] < cost:
            continue
        for nx, nc in graph[x]:
            new_cost = cost + nc
            if distance[nx] > new_cost:
                distance[nx] = new_cost
                heappush(hq, (new_cost, nx))
    # ......
    return distance[start] 

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))

result = inf
for i in range(V):
    result = min(dijkstra(i), result)
if result == inf:
    print(-1)
else:
    print(result)
'''