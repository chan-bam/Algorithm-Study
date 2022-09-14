import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 물품의 수 N # 최대 무게 K
stuff = [list(map(int, input().split())) for _ in range(N)]
knapsack = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight, value = stuff[i - 1]
        if weight > j:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(knapsack[i - 1][j], value + knapsack[i - 1][j - weight])

print(knapsack[N][K])









'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 물품의 수 N # 버틸 수 있는 무게 K
stuff = [[0, 0]]
for _ in range(N):
    stuff.append(list(map(int, input().split())))
knapsack = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight, value = stuff[i]
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])


'''