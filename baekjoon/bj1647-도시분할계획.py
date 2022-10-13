import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

def prim(start):
    hq = [(0, start)]
    total_cost, max_cost, cnt = 0, 0, N
    while cnt:
        cost, node = heappop(hq)
        if visited[node]:
           continue
        visited[node] = 1
        cnt -= 1
        total_cost += cost
        max_cost = max(max_cost, cost)
        for i in graph[node]:
            if not visited[i[1]]:
                heappush(hq, i)
    return total_cost - max_cost

print(prim(1))

'''
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

def prim(start):
    hq = [(0, start)]
    total_cost, max_cost, cnt = 0, 0, 0
    while hq:
        if cnt == N:
            break
        cost, node = heappop(hq)
        if visited[node]:
           continue
        visited[node] = 1
        cnt += 1
        total_cost += cost
        max_cost = max(max_cost, cost)
        for i in graph[node]:
            if not visited[i[1]]:
                heappush(hq, i)
    return total_cost - max_cost

print(prim(1))
'''
'''
import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

def prim(start):
    hq = graph[start]
    heapify(hq)
    visited[start] = 1
    total_cost, max_cost = 0, 0
    while hq:
        cost, node = heappop(hq)
        if visited[node]:
           continue
        visited[node] = 1
        total_cost += cost
        max_cost = max(max_cost, cost)
        for i in graph[node]:
            if not visited[i[1]]:
                heappush(hq, i)
    return total_cost - max_cost

print(prim(1))
'''

# 오답
'''
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split()) # 집의 개수 N, 길의 개수 M
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

def prim(start):
    maxC = 0
    visited = [0] * (N + 1)
    visited[start] = 1
    hq = []
    cnt, result = 0, 0
    for i in graph[start]:
        heappush(hq, i)
    while hq:
        if cnt == N - 1: # xxx
            return result - maxC # xxxx
        cost, node = heappop(hq)
        if visited[node]:
            continue
        visited[node] = 1
        maxC = max(maxC, cost)
        result += cost
        cnt += 1
        for i in graph[node]:
            new_cost, new_node = i
            if not visited[new_node]:
                heappush(hq, i)
print(prim(1))
'''

# 모든 집을 순회할 수 있는 길 합계의 최소값을 구한 후, 그 중 가장 긴 길을 끊어버리면 된다

