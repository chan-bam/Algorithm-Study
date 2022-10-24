n, m = map(int, input().split())
res = []
def perm():
    if len(res) == m:
        print(*res)
        return
    for i in range(1, n + 1):
        res.append(i)
        perm()
        res.pop()
perm()

# 중복순열