import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 점의 개수 n , 진행된 차례의 수 m
parent = list(range(n + 1))

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

for i in range(m):
    s, e = map(int, input().split())
    if find(s) == find(e):
        print(i + 1)
        exit(0)
    else:
        union(s, e)
print(0)
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 점의 개수 n , 진행된 차례의 수 m
game = [list(map(int, input().split())) + [i] for i in range(1, m + 1)]
parent = list(range(n + 1))

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

result = 0
for s, e, cnt in game:
    if find(s) == find(e):
        result = cnt
        break # !!!
    else:
        union(s, e)
print(result)
'''