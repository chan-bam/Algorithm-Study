# 조합
N, M = map(int, input().split())
def comb(cur, start):
    if cur == M:
        print(*result)
        return
    for i in range(start, N + 1):
        result[cur] = i
        comb(cur + 1, i + 1)
result = [0] * M
comb(0, 1)

'''
from itertools import combinations

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]
result = list(combinations(nums, M))
for r in result:
    print(*r, sep=' ')
'''
