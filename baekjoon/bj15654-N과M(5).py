import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = [0] * M
visited = [0] * N

def perm(idx):
    if idx == M:
        print(*result)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result[idx] = nums[i]
            perm(idx + 1)
            visited[i] = 0

perm(0)

# dfs, backtracking
'''
def solve():
    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        if nums[i] not in result: # nums에 동일한 숫자가 2개 이상 없을 때만 가능
            result.append(nums[i])
            solve()
            result.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []
visited = [0] * N

solve()
'''


'''
# 순열
from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = list(permutations(nums, M))

for r in result:
    print(*r)
'''