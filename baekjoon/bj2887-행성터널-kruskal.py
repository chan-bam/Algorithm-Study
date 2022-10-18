import sys
input = sys.stdin.readline

N = int(input()) # N개의 행성
planet = [list(map(int, input().split())) + [i] for i in range(N)] # 행성의 번호 추가 저장
parent = list(range(N))
result = 0 # 최소비용 누적값 저장
edge = [] # 간선, 비용 저장

# 정렬
for i in range(3):
    planet.sort(key=lambda x: x[i])
    for j in range(N - 1):
        edge.append([abs(planet[j][i] - planet[j + 1][i]), planet[j][3], planet[j + 1][3]])
edge.sort()

# kruskal
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

for cost, start, end in edge:
    if find(start) != find(end):
        union(start, end)
        result += cost
print(result)

'''
3
1 1 1
2 3 9
-1 9 5
answer : 3

6
0 0 0
1 1 1
-5 -5 -5
-6 -6 170
-1 -1 170
-4 -4 172
answer : 4
'''