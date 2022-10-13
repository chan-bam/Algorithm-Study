import sys
input = sys.stdin.readline
from heapq import heappop, heappush

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append([C, B])
    graph[B].append([C, A])
visited = [0] * (V + 1)

def prim(start):
    hq = []
    visited[start] = 1
    for i in graph[start]:
        heappush(hq, i)

    cnt, total_cost = 0, 0
    while hq:
        if cnt == V - 1:
            break
        c, node = heappop(hq)
        if visited[node]:
            continue
        visited[node] = 1
        cnt += 1
        total_cost += c
        for i in graph[node]:
            new_c, new_node = i
            if not visited[new_node]:
                heappush(hq, i)
    return total_cost
print(prim(1))


'''
import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify

V, E = map(int, input().split())
visited = [0] * (V + 1)

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    # A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.
    graph[A].append([C, B])
    graph[B].append([C, B])

# 프림 알고리즘

visited[1] = 1
hq = []
# 임의의 정점(1)의 인접 간선을 heap에 넣음
for i in graph[1]:
    heappush(hq, i)
cnt, result = 0, 0
while hq:
    # 간선이 총 V - 1 개 이루어졌다면 종료
    if cnt == V - 1:
        break
    c, node = heappop(hq)
    if visited[node]: # 이미 방문한 노드이면
        continue
    # 방문한 노드가 아니면
    visited[node] = 1
    # 간선의 개수 추가
    cnt += 1
    # 가중치 누적
    result += c
    for i in graph[node]:
        new_c, new_node = i
        if not visited[new_node]:
            heappush(hq, i)
print(result)
'''

# 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
# 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

# 프림 알고리즘은 heap 자료구조를 이용한다는 점에서 다익스트라와 비슷하다.
# 단, heap에 넣는 가중치가 다익스트라는 시작 정점에서 현재까지 이어져 온 실제 길이라면,
# 프림은 그냥 간선 자체의 가중치를 넣는다
# visit 배열을 만들고 방문하지 않은 정점들을 탐색하며 연결된 간선들 중 방문하지 않은 정점과 연결된 간선을 heap에 넣는다
# 그리고 heap 자료구조이니, 가장 작은 가중치의 간선들을 순서대로 뽑ㄱ ㅔ된다.
# 여기서 방문하지 않은 정점들만 사용하여 또 다시 다른 정점들을 탐색한다.
# heap이 비게 되거나 위와 같은 탐색이 총 v-1번 진행되었다면, 반복을 종료한다
# 최소 스패닝 트리의 간선은 무조건 v-1개가 만들어지게 된다.