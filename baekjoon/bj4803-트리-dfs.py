import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(prev, node):
    visited[node] = 1
    for n in tree[node]:
        if prev == n:
            continue
        if visited[n]:
            return False
        if not dfs(node, n):
            return False
    return True

for tc in range(1, 501):
    N, M = map(int, input().split())
    if not N and not M:
        break
    tree = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        p, q = map(int, input().split())
        tree[p].append(q)
        tree[q].append(p)
    cnt = 0
    for v in range(1, N + 1):
        if not visited[v]:
            if dfs(0, v):
                cnt += 1
    if not cnt:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')