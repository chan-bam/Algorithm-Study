import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def bfs(start):
    Q = deque([start])
    if not visited[start]: # 방문하지 않은 정점인 경우
        visited[start] = 1 # 1
    while Q:
        x = Q.popleft()
        for nx in graph[x]:
            if not visited[nx]: # 한번도 방문하지 않음
                Q.append(nx)
                if visited[x] == 1: # 1인 경우
                    visited[nx] = 2 # 인접한 노드는 2로
                else: # 2인 경우
                    visited[nx] = 1 # 인접한 노드는 1로
            elif visited[nx] == visited[x]: # 인접한 노드의 visited값이 같으면 이분그래프가 아님
                return False
    return True

for _ in range(T):
    V, E = map(int, input().split()) # 정점의 개수 V, 간선의 개수 E
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    visited = [0] * V
    for s in range(V):
        if not bfs(s):
            print("NO")
            break
    else:
        print("YES")


# 틀린 풀이 - cycle의 유무를 확인하는 문제가 아님 : cycle이 있어도 이분그래프일 수 있음
'''
import sys
input = sys.stdin.readline

T = int(input())

def dfs(start):
    for i in graph[start]:
        if i == start:
            continue
        if visited[i]:
            return False
        if not visited[i]:
            visited[i] = 1
            dfs(i)
    return True


for _ in range(T):
    V, E = map(int, input().split()) # 정점의 개수 V, 간선의 개수 E
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    print(graph)
    for s in range(V):
        visited = [0] * V
        if not dfs(s):
            print(s)
            print("NO", end='')
            break
    else:
        print("YES", end='')
'''

'''
# 많이 틀리는 반례모음
1
6 6
1 3
3 4
4 2
2 5
5 6
6 1
YES

2
3 3
1 2
2 3
1 3
2 1
1 2
NO YES

1
5 4
1 2
2 3
3 1
4 5
NO

1
4 2
1 2
3 4
YES

1
5 4
1 2
3 4
4 5
3 5
NO

1
4 3
1 4
4 3
3 2
YES

1
5 4
1 2
1 3
2 4
3 5
YES

1
4 3
1 2
4 3
2 3
YES
'''