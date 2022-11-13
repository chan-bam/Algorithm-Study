import sys
input = sys.stdin.readline

N = int(input())
dp = [1, 2]     # 1, 2, 3, 5, ...
for i in range(N - 2):
    dp.append((dp[i] + dp[i + 1]) % 15746) # !!!!!
print(dp[N - 1])