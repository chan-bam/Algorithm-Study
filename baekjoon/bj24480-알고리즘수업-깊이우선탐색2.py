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
    g.sort(reverse = 1)

visited[R] = 1
dfs(R)
print(*visited[1:], sep='\n')

'''
# 순서가 안맞음
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

def dfs(start):
    cnt = 1
    visited = [0] * (N + 1)
    stk = [start]
    while(stk): # stack에 남은 것이 없을 때까지 반복
        node = stk.pop()
        if not visited[node]:
            visited[node] = cnt
            cnt += 1
            for n in graph[node]:
                stk.append(n)
    visited.pop(0)
    print(*visited, sep='\n')

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse = True)

dfs(R)
'''

