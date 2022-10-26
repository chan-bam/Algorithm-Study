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
    overlap = -1
    for i in range(n):
        if res and res[-1] > nums[i]:
            continue
        if overlap != nums[i] and not visited[i]:
            overlap = nums[i]
            visited[i] = 1
            res.append(nums[i])
            comb()
            res.pop()
            visited[i] = 0

comb()


'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
check = set()
res = []
visited = [0] * n

def comb():
    if len(res) == m:
        check.add(tuple(res)) # 문자열, 숫자, 튜플만 set에 넣으면 중복 제거가 가능
        return
    for i in range(n):
        if res and res[-1] > nums[i]:
            continue
        if not visited[i] :
            visited[i] = 1
            res.append(nums[i])
            comb()
            res.pop()
            visited[i] = 0

comb()
for i in sorted(check):
    print(*i)
'''

'''
import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for i in sorted(set(combinations(nums, m))):
    print(*i)
'''

# 조합 # 비내림차순 출력
# 중복되는 수열을 여러번 출력하면 안됨
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.
