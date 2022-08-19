T = int(input())

DP = [1, 2, 4]

for _ in range(T):
    n = int(input())
    if len(DP) < n:
        for i in range(len(DP), n):
            DP.append(DP[i - 1] + DP[i - 2] + DP[i - 3])
    print(DP[n - 1])


# 1 : (1) -- 1
# 2 : (1, 1) (2) -- 2
# 3 : (1, 1, 1) (1, 2) (2, 1) (3) -- 4
# 4 : (1, 3) -- 1
#     (1, 1, 2) (2, 2) -- 2
#     (1, 1, 1, 1) (1, 2, 1) (2, 1, 1) (3, 1) -- 4

'''
DP = [1, 2, 4]

for _ in range(T):
    n = int(input())
    if n > len(DP):
        for i in range(len(DP), n):
            DP.append(DP[i - 1] + DP[i - 2] + DP[i - 3])
    print(DP[n - 1])
'''