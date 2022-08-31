import sys
input = sys.stdin.readline

def solve(r, c, n):
    global result
    status = tree[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if tree[i][j] != status:
                result += '('
                solve(r, c, n // 2)
                solve(r, c + n // 2, n // 2)
                solve(r + n // 2, c, n // 2)
                solve(r + n // 2, c + n // 2, n // 2)
                result += ')'
                return
    result += str(status)

result = ''
N = int(input())
tree = [list(map(int, input().rstrip())) for _ in range(N)]
solve(0, 0, N)
print(result)