import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited = [0] * (N + 1)
    cnt = 1
    Q = deque([start])
    while Q:
        node = Q.popleft()
        if not visited[node]:
            visited[node] = cnt
            cnt += 1
            for n in graph[node]:
                Q.append(n)

    print(*visited[1:], sep='\n')

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse = True)

bfs(R)