import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    for s in tree[start]:
        if not visited[s] and tree[s]:
            visited[s] = start
            dfs(s)

N = int(input())

tree = [[] for _ in range(N + 2)]
visited = [0] * (N + 2)
for _ in range(N - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
dfs(1)

print(*visited[2:-1], sep='\n', end='') # end='' 없으면 오답