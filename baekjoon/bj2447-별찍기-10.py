import sys
input = sys.stdin.readline

N = int(input())

def solve(n):
    if n == 3:
        return ['***', '* *', '***']
    star = solve(n // 3)
    stars = []
    for i in star:
        stars.append(i * 3)
    for i in star:
        stars.append(i + ' ' * (n // 3) + i)
    for i in star:
        stars.append(i * 3)
    return stars

result = solve(N)
for r in result:
    print(r)

'''
import sys
input = sys.stdin.readline

def solve(x, y, n):
    if n == 3:
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    continue
                star[x + i][y + j] = '*'
        return
    temp = (0, n // 3, n // 3 * 2)
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                continue
            solve(x + temp[i], y + temp[j], n // 3)

N = int(input())
star = [[' '] * N for _ in range(N)]
solve(0, 0, N)
for s in star:
    print(*s, sep='')
'''
