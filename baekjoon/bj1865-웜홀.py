import sys
input = sys.stdin.readline
# inf = float('inf') # inf에 음수 가중치를 더해도 inf 그대로이기 때문에 inf를 쓰면 오답 / overflow가 발생하여 오답이라는 의견도 있음
inf = sys.maxsize # 5000 * 10000 이상이면 적당

def bellman_ford(): # 음의 cycle이 있는지 없는지 확인
    # distance[1] = 0 # 임의의 정점에서 시작해도 정답
    for i in range(1, N + 1):
        for cur_x, next_x, time in edges:
            if distance[next_x] > distance[cur_x] + time:
                distance[next_x] = distance[cur_x] + time
                if i == N:
                    return True # 음의 cycle이 있음
    return False

T = int(input())

for _ in range(T):
    N, M, W = map(int, input().split()) # 지점의 수 N, 도로의 개수 M, 웜홀의 개수 W
    distance = [inf] * (N + 1)
    edges = []
    # 도로의 정보 # 도로는 방향이 없음
    for _ in range(M):
        S, E, T = map(int, input().split()) # 시작점 S # 종료점 E # 걸리는 시간 T
        edges.append((S, E, T))
        edges.append((E, S, T))
    # 웜홀의 정보 # 웜홀은 방향이 있음
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    if bellman_ford():
        print("YES")
    else:
        print("NO")

# 플로이드 워셜로도 가능하다고 함