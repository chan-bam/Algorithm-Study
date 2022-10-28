import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def perm(ans, cnt):
    if cnt == m:
        print(ans.lstrip())
        return
    overlap = -1
    for i in nums:
        if i != overlap:
            overlap = i
            perm(ans + ' ' + str(i), cnt + 1)
perm('', 0)

'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
res = []

def perm():
    if len(res) == m:
        print(*res)
        return
    overlap = -1
    for i in nums:
        if i != overlap:
            overlap = i
            res.append(i)
            perm()
            res.pop()
perm()

'''
# 중복 순열