import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []

def solve(start):
    if len(result) == M:
        print(*result)
        return
    overlap = 0
    for i in range(start, N):
        if overlap != nums[i]:
            overlap = nums[i]
            result.append(nums[i])
            solve(i)
            result.pop()

solve(0)

'''
# 중복조합
from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = list(set(combinations_with_replacement(nums, M)))
result.sort()

for r in result:
    print(*r, sep=' ')

'''

