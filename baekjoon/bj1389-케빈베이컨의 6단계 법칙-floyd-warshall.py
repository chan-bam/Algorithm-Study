import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 유저의 수 N, 친구관계의 수 M
inf = float('inf')
user = [[inf] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    user[s][e] = 1
    user[e][s] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j and user[i][j] > user[i][k] + user[k][j]:
                user[i][j] = user[i][k] + user[k][j]

minV = inf
for i in range(1, N + 1):
    sumV = 0
    for j in range(1, N + 1):
        if user[i][j] != inf:
            sumV += user[i][j]
    if minV > sumV:
        minV = sumV
        minIdx = i

print(minIdx)

# bfs보다 빠르진 않음