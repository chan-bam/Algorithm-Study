import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split()) # 우주신들의 개수 N # 이미 연결된 신들과의 통로의 개수 M
# 우주신들의 좌표
pos = [tuple(map(int, input().split())) for _ in range(N)]

# 이미 연결된 통로 # 번호는 입력받은 좌표들의 순서
connect = [[] for _ in range(N)]
link = [[] for _ in range(N)] # 인접 리스트
for _ in range(M):
    p, q = map(int, input().split())
    connect[p - 1].append(q - 1)
    connect[q - 1].append(p - 1)
    # link[p - 1].append((0, q - 1))
    # link[q - 1].append((0, p - 1))

for i in range(N - 1):
    for j in range(i + 1, N):
        if i == j:
            continue
        elif i in connect[j] or j in connect[i]: # 이미 연결된 통로
            link[i].append((0, j))
            link[j].append((0, i))
        else:
            (x1, y1), (x2, y2) = pos[i], pos[j]
            distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            link[i].append((distance, j))
            link[j].append((distance, i))

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
    for i in link[node]:
        if not visited[i[1]]:
            heappush(hq, i)
print(f'{result:.2f}') # 소수점 둘째자리까지 출력(셋째짜리에서 반올림)