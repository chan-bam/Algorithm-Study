import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]

for i in range(1, N):
    dp.append(max(dp[i - 1] + nums[i], nums[i]))

print(max(dp))

'''
# 시간초과
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

maxV, sumV = -1000
for i in range(N):
    for j in range(N - i):
        maxV = max(maxV, sum(nums[j:j + i + 1]))
print(maxV)
'''

