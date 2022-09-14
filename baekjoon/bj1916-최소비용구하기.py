import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start):
    hq = []
    heappush(hq, (0, start))
    visited[start] = 0
    while hq:
        cost, x = heappop(hq)
        if x == E:
            return cost
        if visited[x] >= cost:
            for nc, nx in bus[x]:
                new_cost = nc + cost
                if visited[nx] > new_cost:   #  >= (<- 메모리초과)
                    visited[nx] = new_cost
                    heappush(hq, (new_cost, nx))

N, M = int(input()), int(input()) # 도시의 개수, 버스의 개수
bus = [[] for _ in range(N + 1)]
visited = [sys.maxsize] * (N + 1)

for _ in range(M):
    s, e, c = map(int, input().split()) # 버스의 시작점, 도착점, 버스비용
    bus[s].append((c, e))

S, E = map(int, input().split())

print(dijkstra(S))


'''
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
bus = [[] for _ in range(N + 1)]
visited = [sys.maxsize] * (N + 1)

for _ in range(M):
    s, e, c = map(int, input().split())
    bus[s].append((e, c))

start, end = map(int, input().split())

def dijkstra(x):
    hq = []
    heappush(hq, (0, x))
    visited[x] = 0
    while hq:
        cost, x = heappop(hq)
        if visited[x] >= cost:
            for nx, nc in bus[x]:
                nd = cost + nc
                if visited[nx] > nd:
                    heappush(hq, (nd, nx))
                    visited[nx] = nd

dijkstra(start)

print(visited[end])

'''


'''
# 메모리초과
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global result
    Q = deque([(S, 0)])
    while Q:
        node, cos = Q.popleft()
        if node == E:
            result = min(result, cos)
        for s in bus[node]:
            e, c = s
            Q.append((e, c + cos))

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
bus = [[] for _ in range(N + 1)]
result = 100_000 * N
for _ in range(M):
    start, end, cost = map(int, input().split())
    bus[start].append((end, cost))

S, E = map(int, input().split())

bfs()
print(result)
'''