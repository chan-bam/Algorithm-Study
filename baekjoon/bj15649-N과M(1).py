n, m = map(int, input().split())

res = []
visited = [0] * (n + 1)
def perm():
    if len(res) == m:
        print(*res)
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = 1
            res.append(i)
            perm()
            res.pop()
            visited[i] = 0
perm()

'''
# 순열
from itertools import permutations

n, m = map(int, input().split())
for p in permutations(range(1, n + 1), m):
    print(*p)
'''