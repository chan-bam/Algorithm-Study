import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[y] = x
        visited[x] += visited[y]
    return visited[x]
    # print(visited[x])   # == visited[find(x)] == visited[find(y)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

T = int(input())
for _ in range(T):
    F = int(input())
    parents = {}
    visited = {}
    for _ in range(F):
        a, b = input().split()
        if a not in parents:
            parents[a] = a
            visited[a] = 1
        if b not in parents:
            parents[b] = b
            visited[b] = 1
        print(union(a, b))
        # union(a, b)