# pypy3만 통과
import sys
input = sys.stdin.readline

inf = sys.maxsize
V, E = map(int, input().split())
graph = [[inf] * V for _ in range(V)] # V개의 마을

# (a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.
for _ in range(E):
    a, b, c = map(int, input().split())
    # a -> b 임에 주의
    graph[a - 1][b - 1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            # if i != j <- XXXXXX cycle 확인해야함
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# cycle은 출발지와 도착지가 같은 것이므로 i -> i를 확인
result = inf
for i in range(V):
    if graph[i][i] != inf:
        result = min(result, graph[i][i])
if result != inf:
    print(result)
else:
    print(-1)
