import sys
input = sys.stdin.readline
from math import gcd

N = int(input())
nums = [int(input()) for _ in range(N)]
temp = []
for i in range(N - 1):
    temp.append(abs(nums[i + 1] - nums[i]))
res_gcd = gcd(*temp)

res = [res_gcd]
for i in range(2, int(res_gcd ** 0.5) + 1):
    if not res_gcd % i:
        res.append(i)
        res.append(res_gcd // i)

print(*sorted(set(res))) # set도 sorted로 정렬할 수 있다

'''
# 시간초과
# 종이에 적은 N개의 숫자를 각각 M으로 나누었을때 나머지가 같게 되는 경우의 M을 모두 찾기

N = int(input())
nums = [int(input()) for _ in range(N)]
maxV = max(nums)
result = []

for i in range(2, maxV):
    temp = nums[0] % i
    for j in range(1, N):
        if temp != nums[j] % i:
            break
    else:
        result.append(i)

print(*result)
'''