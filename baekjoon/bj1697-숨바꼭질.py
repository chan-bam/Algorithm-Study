import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    Q = deque([start])
    while Q:
        node = Q.popleft()
        if node == K:
            return
        for new in (node - 1, node + 1, node * 2):
            if 0 <= new < 100001 and not visited[new]:
                visited[new] = visited[node] + 1
                Q.append(new)

N, K = map(int, input().split())
visited = [0] * (100001)
bfs(N)
print(visited[K])