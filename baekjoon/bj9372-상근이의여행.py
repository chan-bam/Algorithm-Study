import sys
input = sys.stdin.readline

T = int(input())

# 가장 적은 개수의 간선으로 모든 정점을 연결
# 선의 가중치가 같으면 스패닝 트리의 간선의 개수는 노드갯수 - 1
for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
    print(N - 1)
    
# MST관련 알고리즘 없이도 풀 수는 있는 문제
# 애초에 모든 국가가 연결되있기 때문에 N-1

# N개의 정점이 있을 때 최소 N-1개의 간선으로 연결이 될 수 있고 그렇다면 트리의 구조가된다. 
# 신장 트리는 모든 정점이 연결되어 있어야하고 사이클을 포함하지 않는다.

'''
# dfs
import sys
input = sys.stdin.readline

T = int(input())

def dfs(x, cnt):
    visited[x] = 1
    for nx in graph[x]:
        if not visited[nx]:
            cnt = dfs(nx, cnt + 1)
    return cnt
# 가장 적은 종류의 비행기를 타고 모든 국가를 여행
# 타야하는 비행기 종류의 최소의 개수
# 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다 # ...
# 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다. # <<<
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    visited = [0] * N
    for _ in range(M):
        # 왕복 비행기
        a, b = map(int, input().split())
        graph[a - 1].append((b - 1))
        graph[b - 1].append((a - 1))
    print(dfs(0, 0))
'''