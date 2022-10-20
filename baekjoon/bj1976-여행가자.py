import sys
input = sys.stdin.readline

N = int(input()) # 도시의 수
M = int(input()) # 여행계획에 속한 도시들의 수

parent = list(range(N))
def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(N):
    link = list(map(int, input().split()))
    for j in range(N):
        if link[j]: # 연결된 경로가 있으면
            union(i, j)

plan = list(map(int, input().split())) # 여행 경로
# parent = [-1] + parent
# print(parent)
# 경로 체크
start = parent[plan[0] - 1]
for i in range(1, M):
    if parent[plan[i] - 1] != start:
        print("NO")
        exit(0)
print("YES")

'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input()) # 도시의 수
M = int(input()) # 여행계획에 속한 도시들의 수
link = [list(map(int, input().split())) for _ in range(N)] # 도시간의 연결 여부
plan = list(map(int, input().split())) # 여행 경로

def bfs(start, end):
    if start == end:
        return True
    visited = [0] * N
    Q = deque([start])
    while Q:
        x = Q.popleft()
        visited[x] = 1
        for i in range(N):
            if link[x][i] and not visited[i]:
                if i == end:
                    return True
                Q.append(i)
    return False

for i in range(M - 1):
    if not bfs(plan[i] - 1, plan[i + 1] - 1):
        print("NO")
        exit(0)
print("YES")
'''

'''
4
4
0 0 0 1
0 0 1 0
0 1 0 1
1 0 1 0
3 1 2 4
ans: YES

3
2
0 0 0
0 0 1
0 1 0
1 1
ans : YES
'''
