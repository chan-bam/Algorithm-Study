import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    visited = [0] * (N + 1)
    Q = deque([x])
    sum_v = 0
    while Q:
        n = Q.popleft()
        for i in user[n]:
            if not visited[i]:
                visited[i] = visited[n] + 1
                sum_v += visited[n] + 1
                Q.append(i)
    return sum_v

N, M = map(int, input().split())
user = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    user[a].append(b)
    user[b].append(a)

min_v = 10000000
min_idx = 0
for i in range(1, N + 1):
    result = bfs(i)
    if min_v > result:
        min_v = result
        min_idx = i

print(min_idx)
'''
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    visited = [0] * (N + 1)
    Q = deque([x])
    while Q:
        n = Q.popleft()
        for i in user[n]:
            if not visited[i]:
                visited[i] = visited[n] + 1
                Q.append(i)
    return sum(visited)

N, M = map(int, input().split())
user = [[] for _ in range(N + 1)]
result = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    user[a].append(b)
    user[b].append(a)

for i in range(1, N + 1):
    result[i] = bfs(i)

result.pop(0)
print(result.index(min(result)) + 1)
'''