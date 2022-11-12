import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)] # !!!!!!
while True:
    A, B, C = map(int, input().split())
    if A == B == C == -1:
        exit()
    print(f'w({A}, {B}, {C}) = {w(A, B, C)}')



'''
1 1 1
2 2 2
10 4 6
50 50 50
-1 7 18
-1 -1 -1
'''

'''
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]
while True:
    A, B, C = map(int, input().split())
    dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
    if A == -1 and B == -1 and C == -1:
        exit()
    print(f'w({A}, {B}, {C}) = {w(A, B, C)}')
'''