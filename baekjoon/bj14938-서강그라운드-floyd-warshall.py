import sys
input = sys.stdin.readline

# 지역의 개수 N # 수색 범위 M # 길의 개수 R
N, M, R = map(int, input().split())
items = list(map(int, input().split())) # 구역에 있는 아이템 수
graph = [[sys.maxsize] * N for _ in range(N)]
for _ in range(R):
    s, e, c = map(int, input().split())
    # 양방향
    graph[s - 1][e - 1] = min(graph[s - 1][e - 1], c)
    graph[e - 1][s - 1] = min(graph[e - 1][s - 1], c)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

result = 0
for i in range(N):
    item_sum = 0
    for j in range(N):
        if graph[i][j] <= M or i == j:
            item_sum += items[j]
    result = max(result, item_sum)

print(result)