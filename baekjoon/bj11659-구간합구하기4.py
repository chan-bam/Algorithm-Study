import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = [0] + list(map(int, input().split()))
nums_sum = [0] * (N + 1)

for n in range(1, N + 1):
    nums_sum[n] = nums_sum[n - 1] + nums[n]

for _ in range(M):
    i, j = map(int, input().split())
    print(nums_sum[j] - nums_sum[i - 1])