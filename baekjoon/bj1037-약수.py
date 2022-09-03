import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
if len(nums) == 1:
    print(nums[0] ** 2)
else:
    nums.sort()
    print(nums[0] * nums[-1]) # 가장 작은 약수 * 가장 큰 약수