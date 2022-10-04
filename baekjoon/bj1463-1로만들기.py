import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
visited = [0] * (N + 1)
Q = deque([(1, 0)])
# bfs
while Q:
    x, cnt = Q.popleft()
    if x * 3 == N or x * 2 == N or x + 1 == N:
        cnt += 1
        break
    for i in (x * 3, x * 2, x + 1):
        # visited를 확인하는 이유는 bfs 특성상 나중에 해당 idx에 방문한 것은 그만큼 cnt가 높기 때문에 굳이 방문할 필요가 없다
        if i < N and not visited[i]:
            visited[i] = 1
            Q.append((i, cnt + 1))
print(cnt)

'''
# DP
N = int(input())
D = [0] * (N + 1)

# for i in range(2, N + 1):
#     DP[i] = DP[i - 1] + 1
#     if not i % 3:
#         DP[i] = min(DP[i], DP[i // 3] + 1)
#     if not i % 2:
#         DP[i] = min(DP[i], DP[i // 2] + 1)

for i in range(2, N + 1):
    if not i % 6:
        D[i] = min(D[i - 1] + 1, D[i // 3] + 1, D[i // 2] + 1)
    elif not i % 3:
        D[i] = min(D[i - 1] + 1, D[i // 3] + 1)
    elif not i % 2:
        D[i] = min(D[i - 1] + 1, D[i // 2] + 1)
    else:
        D[i] = D[i - 1] + 1

print(D[N])

'''