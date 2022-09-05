from math import gcd

N = int(input())
nums = list(map(int, input().split()))

for i in range(1, N):
    g = gcd(nums[0], nums[i])
    print(f'{nums[0] // g}/{nums[i] // g}')