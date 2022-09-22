import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def bfs(start):
    Q = deque([start])
    if not visited[start]:
        visited[start] = 1
    while Q:
        x = Q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = -visited[x] # 1, -1 # -1로 초기화하고 0, 1을 xor 하거나 +1 해서 %2 하는 방법도 있음
                Q.append(nx)
            elif visited[x] == visited[nx]:
                return False
    return True

for _ in range(T):
    V, E = map(int, input().split()) # 정점의 개수 V, 간선의 개수 E
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    visited = [0] * V
    for s in range(V):
        if not bfs(s):
            print("NO")
            break
    else: # flag변수로 판단해도 됨
        print("YES")