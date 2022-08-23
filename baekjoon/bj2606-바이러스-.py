import sys
input = sys.stdin.readline

def solve(n):
    global cnt
    visited.append(n)
    if coms[n]:
        for i in coms[n]:
            if i not in visited:
                solve(i)
                cnt += 1
    else:
        return

cnt = 0
visited = []

C = int(input().rstrip())
coms = [[] for _ in range(C + 1)]
N = int(input().rstrip())

for _ in range(N):
    c1, c2 = map(int, input().split())
    coms[c1].append(c2)
    coms[c2].append(c1) # !!!

solve(1)
print(cnt)

