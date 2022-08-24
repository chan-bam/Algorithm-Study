import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 1

def dfs(start):
    global cnt
    cnt += 1
    for i in graph[start]:
        if i and not visited[i]:
            visited[i] = cnt
            dfs(i)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort()

visited[R] = 1
dfs(R)
visited.pop(0)
print(*visited, sep='\n')

'''
# 메모리 초과
N, M, R = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 2)]
visited = [0] * (N + 1)
cnt = 1

def dfs(start):
        global cnt
        cnt += 1
        for i in range(1, N + 1):
            if graph[start][i] and not visited[i]:
                visited[i] = cnt
                dfs(i)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v], graph[v][u] = 1, 1
visited[R] = 1
dfs(R)
visited.pop(0)
print(*visited, sep='\n')
'''