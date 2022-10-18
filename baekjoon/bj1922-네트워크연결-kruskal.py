import sys
input = sys.stdin.readline

N = int(input())    # 컴퓨터의 수 N
M = int(input())    # 연결할 수 있는 간선의 수 M
net = [tuple(map(int, input().split())) for _ in range(M)]
net.sort(key=lambda x: x[2])
parent = list(range(N + 1))
result = 0

# kruskal
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

for start, end, cost in net:
    if find(start) != find(end):
        union(start, end)
        result += cost
print(result)
