import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    Q = deque([N])
    while Q:
        node = Q.popleft()
        if node == K:
            print(visited[K])
            return
        for n in (node + 1, node - 1, node * 2):
            if 0 <= n < 100001 and not visited[n]:
                visited[n] = visited[node] + 1
                Q.append(n)

N, K = map(int, input().split())
visited = [0] * 100001

bfs()