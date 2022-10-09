import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = [(0, start)]
    distance[start] = 0
    while hq:
        cost, x = heapq.heappop(hq)
        if distance[x] < cost:
            continue
        for nx, nc in graph[x].items():
            new_cost = nc + cost
            if distance[nx] > new_cost:
                distance[nx] = new_cost
                heapq.heappush(hq, (new_cost, nx))

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())     # 교차로, 도로, 목적지 후보의 개수
    graph = [{} for _ in range(n + 1)]
    s, g, h = map(int, input().split())     # 예술가들의 출발지, g와 h 교차로 사이에 있는 도로를 지나감
    # g와 h 사이의 도로는 반드시 존재 / 목적지 후보들 중 적어도 1개로 향하는 최단 경로의 일부
    for _ in range(m): # m개의 도로
        a, b, d = map(int, input().split()) # a와 b 사이에 길이 d의 양방향 도로가 있다.
        if (a == g and b == h) or (b == g and a == h):
            d -= 0.1    # 해당 경로를 거쳐간 경우 결과값이 실수가 되도록
        graph[a][b] = d
        graph[b][a] = d
    candidate = [int(input()) for _ in range(t)] # t개의 목적지 후보들 # t개의 지점들은 서로 다른 위치이며 모두 s와 같지 않다
    result = []
    distance = [sys.maxsize] * (n + 1)
    dijkstra(s)
    # 목적지 후보들 중 불가능한 경우들을 제외한 목적지 찾기 (오름차순 출력)
    for c in candidate:
        if int(distance[c]) != distance[c]: # 최단경로가 실수이면
            result.append(c)
    print(*sorted(result)) # 오름차순 정렬

'''
import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [sys.maxsize] * (n + 1)
    distance[start] = 0
    hq = [(0, start)]
    while hq:
        cost, x = heapq.heappop(hq)
        if distance[x] < cost:
            continue
        for nx, nc in graph[x].items():
            new_cost = nc + cost
            if distance[nx] > new_cost:
                distance[nx] = new_cost
                heapq.heappush(hq, (new_cost, nx))
    return distance

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())     # 교차로, 도로, 목적지 후보의 개수
    graph = [{} for _ in range(n + 1)]
    s, g, h = map(int, input().split())     # 예술가들의 출발지, g와 h 교차로 사이에 있는 도로를 지나감
    # g와 h 사이의 도로는 반드시 존재 / 목적지 후보들 중 적어도 1개로 향하는 최단 경로의 일부
    for _ in range(m): # m개의 도로
        a, b, d = map(int, input().split()) # a와 b 사이에 길이 d의 양방향 도로가 있다.
        graph[a][b] = d
        graph[b][a] = d
    candidate = [int(input()) for _ in range(t)] # t개의 목적지 후보들 # t개의 지점들은 서로 다른 위치이며 모두 s와 같지 않다
    # 목적지 후보들 중 불가능한 경우들을 제외한 목적지 찾기 (오름차순 출력)
    result = []
    s_dist, g_dist, h_dist = dijkstra(s), dijkstra(g), dijkstra(h)
    # 최단거리와 g-h 경로를 거쳐가는 경로의 거리가 같은지 비교
    for c in candidate:
        if s_dist[c] == g_dist[s] + h_dist[c] + g_dist[h] or s_dist[c] == g_dist[c] + h_dist[s] + g_dist[h]:
            result.append(c)
    print(*sorted(result)) # 오름차순 정렬
'''

'''
# 오답
import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [sys.maxsize] * (n + 1)
    distance[start] = 0 # 해당 코드 없는 경우는 시간초과 있으면 오답처리됨 # cycle 때문인것으로 추측됨

    hq = [(0, start)]
    while hq:
        cost, x = heapq.heappop(hq)
        if distance[x] < cost:
            continue
        for nx, nc in graph[x].items():
            new_cost = nc + cost
            if distance[nx] > new_cost:
                distance[nx] = new_cost
                # 경로 저장
                trace[nx] = x
                heapq.heappush(hq, (new_cost, nx))

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())     # 교차로, 도로, 목적지 후보의 개수
    graph = [{} for _ in range(n + 1)]
    s, g, h = map(int, input().split())     # 예술가들의 출발지, g와 h 교차로 사이에 있는 도로를 지나감
    # g와 h 사이의 도로는 반드시 존재 / 목적지 후보들 중 적어도 1개로 향하는 최단 경로의 일부
    for _ in range(m): # m개의 도로
        a, b, d = map(int, input().split()) # a와 b 사이에 길이 d의 양방향 도로가 있다.
        graph[a][b] = d
        graph[b][a] = d
    candidate = [int(input()) for _ in range(t)] # t개의 목적지 후보들 # t개의 지점들은 서로 다른 위치이며 모두 s와 같지 않다
    # 목적지 후보들 중 불가능한 경우들을 제외한 목적지 찾기 (오름차순 출력)
    result = []
    trace = [-1] * (n + 1)
    dijkstra(s)
    # trace[s] = -1
    # 경로 추적
    for c in candidate:
        idx = trace[c]
        while trace[idx] != -1:
            if (trace[idx] == g and idx == h) or (trace[idx] == h and idx == g):
                result.append(c)
                break
            idx = trace[idx]
    print(*sorted(result))
'''