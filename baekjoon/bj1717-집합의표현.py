import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())     # n : {0}, {1}, {2}, ... {n} 이 각각 n+1개의 집합 / m: 입력으로 주어지는 연산의 개수
parent = list(range(n + 1))

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(m):
    command, a, b = map(int, input().split())
    if not command:     # 합집합
        union(a, b)
    # elif parent[a] == parent[b]: # XXXXXXXXX
    elif find(a) == find(b):    # 같은 집합에 속해있는지 확인
        print("YES")
    else:
        print("NO")

'''
5 6
0 5 4
0 4 2
0 2 0
0 5 3
0 3 1
1 0 1
'''