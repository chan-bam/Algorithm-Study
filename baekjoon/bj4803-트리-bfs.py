import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    Q = deque([(0, x)])
    visited[x] = 1
    while Q:
        prev, node = Q.popleft()
        for n in tree[node]:
            if n == prev: # 직전 노드와 같은경우 - 방문여부 체크 X Q에 추가 X
                continue
            if visited[n]: # 이전에 방문한 노드를 다시 방문한 경우 - cycle이 있음 == tree가 아님
                return False
            else:
                Q.append((node, n)) # 직전 노드를 함께 저장
    return True # cycle 없이 탐색 완료시

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
            if bfs(v):
                cnt += 1
    if not cnt:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')