import sys
input = sys.stdin.readline

def solve(x, y, n): # 행, 열
    global res
    while n >= 1:
        n -= 1
        if x < 2 ** n and y < 2 ** n: # *0
            res += (2 ** n) ** 2 * 0
        elif x < 2 ** n  and 2 ** n <= y: # *1
            res += (2 ** n) ** 2 * 1
            y -= (2 ** n)
        elif 2 ** n <= x and y < 2 ** n : # *2
            res += (2 ** n) ** 2 * 2
            x -= (2 ** n)
        elif 2 ** n <= x and 2 ** n <= y: # *3
            res += (2 ** n) ** 2 * 3
            x -= (2 ** n)
            y -= (2 ** n)

N, R, C = map(int, input().split())

res = 0
solve(R, C, N)
print(res)

'''
# 시간초과
def solve(x, y, n):
    global num
    # print(x, y, n, num)
    if n != 1:
        solve(x, y, n // 2)
        solve(x, y + n // 2, n // 2)
        solve(x + n // 2, y, n // 2)
        solve(x + n // 2, y + n // 2, n // 2)
        return
    if R == x and C == y:
        print(num)
        exit(0)
    else:
        num += 1

N, R, C = map(int, input().split())
num = 0
solve(0, 0, 2**N)
'''