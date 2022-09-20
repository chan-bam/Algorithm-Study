import sys
input = sys.stdin.readline
import heapq

# N개의 숫자로 구분된 각각의 마을(마을마다 한명의 학생이 삼 => 총 N명의 학생)
# X번 마을에서 파티
# M개의 단방향 도로
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

def dijkstra(start, end):
    distance = [sys.maxsize] * (N + 1)
    distance[start] = 0
    hq = [(0, start)]
    while hq:
        cost, x = heapq.heappop(hq)
        if x == end:
            return cost
        if distance[x] < cost:
            continue
        for nc, nx in graph[x]:
            new_cost = cost + nc
            if distance[nx] > new_cost:
                distance[nx] = new_cost
                heapq.heappush(hq, (new_cost, nx))

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((t, e))

result = 0
for i in range(1, N + 1):
    result = max(result, dijkstra(i, X) + dijkstra(X, i))

print(result)