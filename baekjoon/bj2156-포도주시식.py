import sys
input = sys.stdin.readline

N = int(input())
grape = [int(input()) for _ in range(N)]
dp = [0] * N

if N == 1:
    print(grape[0])
    exit()
elif N == 2:
    print(grape[0] + grape[1])
    exit()

dp[0], dp[1] = grape[0], grape[0] + grape[1]
dp[2] = max(grape[0] + grape[1], grape[1] + grape[2], grape[0] + grape[2])

for i in range(3, N):
    dp[i] = max(dp[i - 3] + grape[i - 1] + grape[i], dp[i - 2] + grape[i], dp[i - 1])
print(max(dp))