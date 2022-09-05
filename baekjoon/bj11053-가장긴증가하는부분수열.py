import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [1] + [0] * (N - 1)

for i in range(1, N):
    maxV = 1 # !!! # 가장 적은 수열의 길이인 1로 초기화해야함 0으로 초기화하면 이후 값에 영향을 줌
                   # 또는 dp = [1] + [1] * (N - 1) 로 초기화한 뒤
                   # dp[i] = max(dp[i], dp[j] + 1) <- 이렇게 해야함
    for j in range(i):
        if nums[i] > nums[j]:
            maxV = max(maxV, dp[j] + 1)
    dp[i] = maxV
print(max(dp))


# for i in range(1, N):
#     maxV, maxIdx = 0, -1
#     for j in range(i):
#         if nums[i] > nums[j]:
#             if maxV < dp[j]:
#                 maxV = dp[j]
#                 maxIdx = j
#     if maxIdx >= 0:
#         dp[i] = dp[maxIdx] + 1
#     else:
#         dp[i] = 1 # 작은 값이 없을 때는 가장 적은 수열의 길이인 1 !!(이후 값에 영향을 줌)
# print(max(dp))
#
