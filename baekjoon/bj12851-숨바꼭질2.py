import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    Q = deque([(N, 0)])
    visited[N] = 1
    while Q:
        n, t = Q.popleft()
        for i in [n + 1, n - 1, n * 2]:
            if i == K:
                result.append(t + 1)
            if 0 <= i <= 100_000 and visited[i] <= 3: # ^^^^^^
                visited[i] += 1 # ^^^
                Q.append((i, t + 1))

N, K = map(int, input().split())
visited = [0] * 100_001
result = []
if N == K:
    print('0\n1')
else:
    bfs()
    answer = min(result)
    print(answer, result.count(answer), sep='\n')

'''
5 100000
19
4

5 237
10
5
'''