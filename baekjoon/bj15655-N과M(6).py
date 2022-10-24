import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

res = []
visited = [0] * n
def comb():
    if len(res) == m:
        print(*res)
        return
    for i in range(n):
        if not visited[i]:
            if res and res[-1] > nums[i]:
                continue
            visited[i] = 1
            res.append(nums[i])
            comb()
            res.pop()
            visited[i] = 0
comb()
'''
# 조합
import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for i in combinations(nums, m):
    print(*i)
'''