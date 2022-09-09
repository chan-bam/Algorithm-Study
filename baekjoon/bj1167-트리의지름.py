import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)
def dfs(node, sumV):
    if visited[node] == -1: # 방문하지 않은 노드이면
        visited[node] = sumV
        for n, w in tree[node]:
            dfs(n, sumV + w)

for _ in range(N):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp) - 1, 2):
        tree[temp[0]].append((temp[i], temp[i + 1])) # 간선의 정보, 간선의 가중치

dfs(1, 0)
maxIdx = visited.index(max(visited))
visited = [-1] * (N + 1)
dfs(maxIdx, 0)
print(max(visited))