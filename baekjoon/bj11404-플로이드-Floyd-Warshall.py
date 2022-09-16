import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
inf = float('inf')
city = [[inf] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    city[s][e] = min(city[s][e], c)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j and city[i][j] > city[i][k] + city[k][j]:
                city[i][j] = city[i][k] + city[k][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if city[i][j] != inf:
            print(city[i][j], end=' ')
        else:
            print(0, end = ' ')
    print()










'''
import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
inf = float('inf')
graph = [[inf] * N for _ in range(N)]

for _ in range(M):
    s, e, c = map(int, input().split())
    if graph[s - 1][e - 1] > c: # 적은 비용 입력
        graph[s - 1][e - 1] = c

for k in range(N): # k : 거쳐가는 정점
    for i in range(N): # i : 시작정점
        for j in range(N): # j : 도착정점
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]: # k 정점을 거쳐 가는 것이 비용이 적으면
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(N):
    for j in range(N):
        if graph[i][j] != inf:
            print(graph[i][j], end=' ')
        else:
            print(0, end=' ')
    print()
'''