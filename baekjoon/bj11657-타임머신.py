import sys
input = sys.stdin.readline
inf = int(1e9)

N, M = map(int, input().split()) # 도시의 개수 N, 버스의 개수 M
bus = []
distance = [inf] * (N + 1)

for _ in range(M):
    s, e, c = map(int, input().split())    # 시작도시, 도착도시, 걸리는 시간
    bus.append((s, e, c))

def bellman_ford(start):
    distance[start] = 0
    for i in range(N):
        for cur_x, next_x, cost in bus:
            if distance[next_x] > distance[cur_x] + cost:
                distance[next_x] = distance[cur_x] + cost
                if i == N - 1:
                    return True
    return False

result = bellman_ford(1)

if result:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == inf:
            print(-1)
        else:
            print(distance[i])

# import sys
# input = sys.stdin.readline
# inf = float('inf')
#
# N, M = map(int, input().split()) # 도시의 개수 N, 버스의 개수 M
# bus = [[] * (M + 1) for _ in range(M + 1)]
# distance = [inf] * (N + 1)
#
# for _ in range(M):
#     s, e, c = map(int, input().split())    # 시작도시, 도착도시, 걸리는 시간
#     bus[s].append((e, c))
#
# def bellman_ford(start):
#     distance[start] = 0
#     for i in range(N):
#         for cur_x in range(1, M + 1):
#             for next_x, cost in bus[cur_x]:
#                 if distance[next_x] > distance[cur_x] + cost:
#                     distance[next_x] = distance[cur_x] + cost
#                     if i == N - 1:
#                         return True
#     return False
#
# result = bellman_ford(1)
#
# if result:
#     print(-1)
# else:
#     for i in range(2, N + 1):
#         if distance[i] == inf:
#             print(-1)
#         else:
#             print(distance[i])

'''
import sys
input = sys.stdin.readline
inf = float('inf')

N, M = map(int, input().split())
edges = []
distance = [inf] * (N + 1)

for _ in range(M):
    s, e, c = map(int, input().split())    # 시작도시, 도착도시, 걸리는 시간
    edges.append((s, e, c))

def bellman_ford(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    # 전체 N - 1 번의 반복
    for i in range(N):
        # 매 반복마다 '모든 간선' 확인
        for j in range(M):
            cur_x, next_x, cost = edges[j]
            # 현재 간선을 거쳐 다른 노드로 이동하는 경우가 더 짧은 경우
            if distance[cur_x] != inf and distance[next_x] > distance[cur_x] + cost:
                distance[next_x] = distance[cur_x] + cost
                # N번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == N - 1:
                    return True
    return False


result = bellman_ford(1)

if result: # 음수 순환이 존재하면
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == inf: # 가는 경로가 없다면
            print(-1)
        else:
            print(distance[i])
'''