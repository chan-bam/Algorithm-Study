from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결할 수 있는 선의 수
net = [[] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    net[a - 1].append((c, b - 1))
    net[b - 1].append((c, a - 1))

# prim
visited = [0] * N
hq = [(0, 0)]
result, cnt = 0, N
while cnt:
    cost, node = heappop(hq)
    if visited[node]:
        continue
    visited[node] = 1
    result += cost
    cnt -= 1
    for i in net[node]:
        if not visited[i[1]]:
            heappush(hq, i)
print(result)