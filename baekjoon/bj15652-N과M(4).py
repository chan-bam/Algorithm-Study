N, M = map(int, input().split())
result = [0] * M

def comb(cur, start):
    if cur == M:
        print(*result)
        return
    for i in range(start, N + 1): # 1부터 N까지
        result[cur] = i
        comb(cur + 1, i)

comb(0, 1)

'''
# 중복조합
from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]
result = list(combinations_with_replacement(nums, M))

for r in result:
    print(*r)
'''
