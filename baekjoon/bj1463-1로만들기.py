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
