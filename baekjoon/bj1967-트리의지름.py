import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
tree = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

def dfs(x, sumV):
    if not visited[x]:
        visited[x] = sumV
        for i in tree[x]:
            dfs(i[0], sumV + i[1])

for _ in range(N - 1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

dfs(1, 1) # 루트노드에서 가장 먼 노드 구하기
idx = visited.index(max(visited))
visited = [0] * (N + 1) # 초기화
dfs(idx, 1) # 루트노드에서 가장 먼 노드에서 가장 먼 노드 구하기
print(max(visited) - 1)
