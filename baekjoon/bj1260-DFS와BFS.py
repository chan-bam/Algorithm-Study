import sys
input = sys.stdin.readline
from collections import deque

visited = []
def dfs(start):
    if start not in visited:
        visited.append(start)
        print(start, end = ' ')
        for i in graph[start]:
            dfs(i)
    return

def bfs(start):
    Q = deque([start])
    visited = [start]
    while Q:
        n = Q.popleft()
        print(n, end = ' ')
        for i in graph[n]:
            if i not in visited:
                visited.append(i)
                Q.append(i)


N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for g in range(1, N + 1):
    graph[g].sort() # !!!

dfs(V)
print()
bfs(V)


'''
def bfs(start):
    Q = deque([start])
    visited.append(start)
    while Q:
        n = Q.popleft()
        print(n, end = ' ')
        for i in graph[n]:
            if i not in visited:
                visited.append(i)
                Q.append(i)
'''