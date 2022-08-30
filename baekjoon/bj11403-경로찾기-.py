import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N

def dfs(x):
    for i in range(N):
        if arr[x][i] and not visited[i]:
            visited[i] = 1
            dfs(i)

for i in range(N):
    dfs(i)
    print(*visited)
    visited = [0] * N