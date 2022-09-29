import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

if house[-1][-1]:
    print(0)
    exit(0)

dp = [[[0] * N for _ in range(N)] for _ in range(3)]
# 0 : 가로, 1 : 세로, 2 : 대각

dp[0][0][1] = 1

for i in range(2, N):
    if not house[0][i]:
        dp[0][0][i] = dp[0][0][i - 1] # 가로

for i in range(1, N):
    for j in range(2, N):
        if not house[i][j] and not house[i - 1][j] and not house[i][j - 1]:
            # 대각선     # 가로에서 대각선으로 오는 경우  # 세로에서 대각선으로 오는 경우 # 대각선에서 대각선으로 오는 경우
            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
        if not house[i][j]:
            # 가로        # 가로에서 가로로 오는 경우 # 대각선에서 가로로 오는 경우
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            # 세로        # 세로에서 세로로 오는 경우 # 대각선에서 세로로 오는 경우
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

result = 0
for i in range(3):
    result += dp[i][-1][-1]
print(result)