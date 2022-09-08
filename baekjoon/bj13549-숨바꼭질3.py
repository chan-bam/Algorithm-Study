import sys
input = sys.stdin.readline
from collections import deque

N, X = map(int, input().split())
visited = [0] * 100_001
Q = deque([N])
visited[N] = 1

while Q:
    n = Q.popleft()
    if n == X:
        break
    for i in [n * 2, n - 1, n + 1]:
        if 0 <= i <= 100_000 and not visited[i]:
            Q.append(i)
            if i == n * 2:
                visited[i] = visited[n]
            else:
                visited[i] = visited[n] + 1

print(visited[X] - 1)
