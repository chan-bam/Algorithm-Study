import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []
visited = [0] * N

def solve():
    if len(result) == M:
        print(*result)
        return
    overlap = 0 # 초기값
    for i in range(N):
        if not visited[i] and overlap != nums[i]: # 전에 쓰인 변수값과 비교
            visited[i] = 1
            result.append(nums[i])
            overlap = nums[i] # 전에 쓰인 변수값을 저장
            solve()
            result.pop()
            visited[i] = 0

solve()

'''
# 시간초과2
import sys
input = sys.stdin.readline

def solve():
    if len(result) == M:
        r = ' '.join(map(str, result))
        if r not in answer:
            answer.append(r)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result.append(nums[i])
            solve()
            result.pop()
            visited[i] = 0

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []
answer = []
visited = [0] * N

solve()

for a in answer:
    print(a)
'''
'''
# 시간초과
import sys
input = sys.stdin.readline

def solve():
    if len(result) == M:
        r = tuple(result)
        if r not in answer:
            answer.append(r)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result.append(nums[i])
            solve()
            result.pop()
            visited[i] = 0

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []
answer = []
visited = [0] * N

solve()

for a in answer:
    print(*a)
'''

# dfs backtracking
'''
# 순열
from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = list(set(permutations(nums, M)))
result.sort()

for r in result:
    print(*r, sep=' ')
'''