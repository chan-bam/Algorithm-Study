import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    visited[start] = 1
    for node in graph[start]:
        if not visited[node]:
            dfs(node)

N, M = map(int, input().split())

visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)