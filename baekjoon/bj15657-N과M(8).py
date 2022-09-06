import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []

def solve(start, num):
    if num == M: # num == len(result)
        print(*result)
        return
    for i in range(start, N):
        result.append(nums[i])
        solve(i, num + 1)
        result.pop()

solve(0, 0)

'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []

def solve():
    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        if not result or nums[i] >= result[-1]:
            result.append(nums[i])
            solve()
            result.pop()
solve()

#dfs
'''


'''
# 중복조합
from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = combinations_with_replacement(nums, M)

for r in result:
    print(*r)
'''
