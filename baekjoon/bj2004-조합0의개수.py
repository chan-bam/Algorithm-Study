n, r = map(int, input().split())

def solve(x, div):
    cnt = 0
    while x:
        x //= div
        cnt += x
    return cnt

result2 = solve(n, 2) - solve(r, 2) - solve(n - r, 2)
result5 = solve(n, 5) - solve(r, 5) - solve(n - r, 5)

print(min(result2, result5))
