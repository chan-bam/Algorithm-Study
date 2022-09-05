N = int(input())

def factorial(x):
    for i in range(1, x + 1):
        dp.append(dp[i - 1] * i)

for i in range(N):
    r, n = map(int, input().split())
    dp = [1]
    factorial(n)
    print(dp[n] // (dp[n - r] * dp[r]))