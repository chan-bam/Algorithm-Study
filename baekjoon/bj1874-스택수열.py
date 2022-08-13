import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(N)]

stk = [0]
res = []

n = 0
idx = 0

while idx < N and n <= N:
    if arr[idx] != stk[-1]:
        stk.append(n + 1)
        res.append('+')
        n += 1
    else:
        result = stk.pop()
        res.append('-')
        idx += 1

if stk != [0]:
    print("NO")
else:
    for r in res:
        print(r)