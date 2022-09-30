import sys
input = sys.stdin.readline

N = int(input())
star = [[' '] * (N * 2) for _ in range(N)]

def solve(x, y, n):
    if n == 3:
        star[x][y] = star[x + 1][y - 1] = star[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            star[x + 2][y + i] = '*'
        return
    temp = n // 2
    solve(x, y, temp)
    solve(x + temp, y - temp, temp)
    solve(x + temp, y + temp, temp)

solve(0, N - 1, N)

for s in star:
    print(*s, sep='')